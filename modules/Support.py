import emoji
from nltk.stem import PorterStemmer
from string import punctuation
from nltk.corpus import stopwords
import pandas as pd
import sqlite3
import re


class TokenCleaner():
    def __init__(self, remove_stopwords=True, return_as_string=True):

        # Some punctuation variations
        self.punctuation = set(punctuation)  # speeds up comparison
        self.punct_set = self.punctuation - {"#"}
        self.punct_pattern = \
            re.compile("[" + re.escape("".join(self.punct_set)) + "]")
        self.stemmer = PorterStemmer()
        self.ZERO_WIDTH_JOINER = '\u200d'

        # Stopwords
        if remove_stopwords:
            self.sw = stopwords.words("english") + ['️', '', ' ']
        else:
            self.sw = ''

        # Two useful regex
        self.whitespace_pattern = re.compile(r"\s+")
        self.hashtag_pattern = re.compile(r"^#[0-9a-zA-Z]+")
        self.CleanText_return_format = return_as_string

    def CleanText(self, _text):
        # if _text is has nothing in it then return none
        if _text is None:
            return ''

        # decode bytes to string if necessary
        if isinstance(_text, str):
            self.text = _text
        elif isinstance(_text, float):
            self.text = str(_text)
        else:
            # this is for the case of tweets which are saved as bytes
            self.text = _text.decode("utf-8")

        self.__add_space_before_and_after_emoji()
        self.__RemovePunctuation()
        self.__TokenizeText()
        self.__StemEachToken()
        self.__RemoveStopWords()

        if self.CleanText_return_format:
            return ' '.join(self.tokens)
        else:
            return self.tokens

    def __StemEachToken(self):
        """
        Perform Stemming on each token (i.e. working, worked, works are all converted to work)<
        """

        self.tokens = [self.stemmer.stem(token) for token in self.tokens]

    def __add_space_before_and_after_emoji(self):
        text_section = list()
        for i, char in enumerate(self.text):
            if emoji.is_emoji(char):
                text_section.append(' ' + self.text[i] + ' ')
            else:
                text_section.append(self.text[i])

            if self.ZERO_WIDTH_JOINER in text_section:
                text_section.remove(self.ZERO_WIDTH_JOINER)

        return ''.join(text_section)

    def __RemovePunctuation(self):
        """
        Loop through the original text and check each character,
        if the character is a punctuation, then it is removed.
        ---------------------------------------------------------
        input: original text
        output: text without punctuation
        """
        self.text = \
            "".join([ch for ch in self.text if ch not in self.punct_set])

        self.text = re.sub(self.punct_pattern, '', self.text)

    def __TokenizeText(self):
        """
        Tokenize by splitting the text by white space
        ---------------------------------------------------------
        input: text without punctuation
        output: A list of tokens
        """
        self.tokens = \
            [item for item in self.whitespace_pattern.split(self.text)]

    def __RemoveStopWords(self):
        """
        Tokenize by splitting the text by white space
        ---------------------------------------------------------
        input: text without punctuation
        output: A list of tokens with all token as lower case
        """
        self.tokens = [token.lower() for token in self.tokens]

        self.tokens = \
            [token for token in self.tokens if not token in self.sw]


def add_space_after_emoji(text):

    text_section = list()
    for i, char in enumerate(text):
        if emoji.is_emoji(char):
            text_section.append(' ' + text[i] + ' ')
        else:
            text_section.append(text[i])

        if self.ZERO_WIDTH_JOINER in text_section:
            text_section.remove(self.ZERO_WIDTH_JOINER)

    return ''.join(text_section)


def clean_string(text):
    if pd.isnull(text):
        return text

    remove_words = stopwords.words("english") + ['️', '', ' ']
    text = text.replace('|', ' ').replace('\n', ' ')

    text = re.sub(punct_pattern, '', text)
    text = add_space_after_emoji(text)
    text_tokens = text.split(' ')
    text = [word.lower() for word in text_tokens]
    text = [word for word in text if not word in remove_words]
    return text


class Database():
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)

    def query(self, statement):
        return pd.read_sql(statement, self.conn)


class Business():
    def __init__(self, info, reviews):
        self.name = info['name'].iloc[0]
        self.info = info
        self.reviews = reviews

    def __set_months(self):
        # resturant_data['serial_date'] is Year-Month
        self.data['serial_date'] = \
            pd.to_datetime(self.data['date']).dt.strftime('%Y-%m')

        # min, max date in the dataset
        self.__min_date = self.data['serial_date'].min()
        self.__max_date = self.data['serial_date'].max()

        # create a list of all the months in the dataset
        self.months = \
            pd.date_range(start=self.__min_date,
                          end=self.__max_date,
                          freq='MS')

        self.months = self.months.strftime('%Y-%m')
        self.months = self.months.tolist()
        self.stat_df = pd.DataFrame()

    @property
    def stat(self):
        if self.stat_df.empty:
            self.__gather_stat()

        return self.stat_df

    def __gather_stat(self):

        for month in self.months:
            df_month = self.data.query('serial_date == @month')
            self.stat_df.loc[month, 'row_count'] = \
                len(df_month)

            self.stat_df.loc[month, 'stars_mean'] = \
                df_month['stars'].mean()

            self.stat_df.loc[month, 'avg_text_length'] = \
                df_month['text'].str.len().mean()

            self.stat_df.loc[month, 'avg_word_count'] = \
                df_month['text'].str.split().str.len().mean()

        # interpolate missing values with linear method
        self.stat_df = self.stat_df.interpolate(method='linear')


class Corpus:

    def __init__(self):
        self.__business = dict()

    @property
    def business_names(self):
        return self.data['name'].unique().tolist()

    def add_business(self, business: Business):
        self.__business[business.name] = business

    def __getitem__(self, business_name):
        return self.__business[business_name]
