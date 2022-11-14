import matplotlib.pyplot as plt
import pandas as pd
import boto3, os
from botocore.config import Config
from dotenv import load_dotenv
load_dotenv('env')



def s3_client():
    config = Config(s3={"use_accelerate_endpoint": True, "addressing_style": "path"})
    s3_resource = boto3.resource("s3", config=config,
                                 aws_access_key_id = os.getenv('aws_access_key_id'),             
                                 aws_secret_access_key = os.getenv('aws_secret_access_key'),
                                 region_name = os.getenv('region_name'))

    return s3_resource.meta.client


def export_data(load_local=True):
    if load_local:
        return pd.read_parquet('data/resturant_data.parquet')

    business = pd.read_parquet('data/business.parquet')
    review = pd.read_parquet('data/review.parquet')

    resturant_data = business.merge(review, on='business_id')
    # remove business and review dataframes from memory
    del business
    del review
    # remove business_id and review_id from resturant_data
    resturant_data.drop(['business_id', 'review_id'], axis=1, inplace=True)
    # convert date to date only
    resturant_data['date'] = pd.to_datetime(resturant_data['date']).dt.date
    resturant_data.to_parquet(
        'data/resturant_data.parquet', index=False, compression='gzip')
    return resturant_data


def get_db_file_from_s3():
    # Code take from stackoverflow forum below
    # www.stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests
    # This will download file and show progress bar while downloading

    response = requests.get(self.s3_folder + 'database.zip', stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(self.db_name + '.zip', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")

# get_db_file_from_s3()
# decompress the zip file
# !unzip database.zip


def chart_date(df, resturant_name):
    # convert df.date to date only
    df['date'] = pd.to_datetime(df['date']).dt.date

    # sort by date
    df = df.sort_values(by='date')

    # set month and year
    df['month'] = pd.to_datetime(df['date']).dt.month
    df['year'] = pd.to_datetime(df['date']).dt.year

    df_group = pd.DataFrame()

    # group by month and year and add mean and std of stars
    df_group['mean'] = df.groupby(['year', 'month'])['stars'].mean()
    df_group['std'] = df.groupby(['year', 'month'])['stars'].std()

    # place count of stars for each month and year
    df_group['count'] = df.groupby(['year', 'month'])['stars'].count()

    # set two ax with figure size 12, 8 with bottom margin 0.2 with grid false
    fig, ax = plt.subplots(2, 1, figsize=(
        12, 8), sharex=True, gridspec_kw={'hspace': 0.4})

    # boxplot of average stars over each year
    df_group.boxplot(column='mean', by='year', ax=ax[0])

    # plot count of total stars over each year
    df_group.boxplot(column='count', by='year', ax=ax[1])

    # hide grid lines for both ax
    ax[0].grid(False)
    ax[1].grid(False)

    ax[0].set_title('Average Stars Over Each Year\nResturant: %s' %
                    resturant_name)
    ax[1].set_title(
        'Count of Reviews Over Each Year\nResturant: %s' % resturant_name)

    # set y axis labels
    ax[0].set_ylabel('Average Stars')
    ax[1].set_ylabel('Count of Reviews')

    print("\nResturant Name: %s" % resturant_name)
    plt.show()
