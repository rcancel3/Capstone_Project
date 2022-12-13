# ADS-599: Capstone - An Evaluation of Strategies Using Natural Language Processing and Yelp for Detecting and Mitigating Crisis-Related Reputational Damage for Restaurants


Capstone project for Team-12 the University of San Diego's M.S. in Applied Data Science program Fall-2022

## Project Status: Complete
</br>

## Installation

To use this project, first clone the repo on your device using the commands below:

`git init`

`git clone https://github.com/nimaamintaghavi/599CapstoneProject.git`

## Authors  

[Martin Zagari ](https://github.com/mzagari) 

[Nima Amin Taghavi](https://github.com/nimaamintaghavi) 

[Roberto Cancel ](https://github.com/rcancel3)


</br>

# Table of Contents
--------
1. [Methods](#Methods)
2. [Technologies](#Technologies)
3. [Project Description](#Project_Description)
4. [Limitations and Challenges](#Limitations_and_Challenges)
5. [Database](#Database)
6. [Visualization](#code-library)
7. [Conclusion](#Conclusion)
8. [References](#References)
9. [License](#License)
10. [Acknowledements](#Acknowledgements)

--------

### Methods  
* Data Ingestion
* Data Cleaning and Sufficiency
* Geospatial Analysissss
* Star Rating and Sentiment Analysis
* Text-based Exploratory Data Analysis
  - Manual Human Labeling of Reviews
  - Exploration  of  keywords  for  food-borne  illness
  - Visual examination of time series and descriptive  analysis
  
* NLP and Topic Modeling
  
--------

### Technologies  
* [Python](https://www.python.org)
* [Modin](https://modin.readthedocs.io/en/stable/) and [Ray](https://docs.ray.io/en/latest/index.html) (for utilizing multi-cores during tokinization)
* [Flask](https://flask.palletsprojects.com/)
* [AWS SageMaker](https://aws.amazon.com/pm/sagemaker/)

--------

## Project Description

This study used Yelp review data to detect and mitigate crisis-related reputational damage for foodborne illness outbreaks. During the exploratory data analysis phase, the distribution changes of star ratings over time were used to successfully detect foodborne illness outbreaks. A foodborne illness-related lexicon was developed and validated using Naive Bayes, and topic modeling via Latent Dirichlet Association (LDA) was used to measure reputational damage by the number of topics required to generate a separate foodborne illness topic. The researchers believe that restaurant chains could benefit from using natural language processing analysis on Yelp reviews to identify topics of negative reviews and determine whether critical topics such as foodborne illness are rising in importance.

<br>

### Limitations and Challenges
> * Limited data available (7 million of 244 million reviews)
> * Small number of metro areas, missing some metros with outbreaks
> * Limited opportunity to do time series
> * Only looked at one type of “crisis” for a single chain
> * With more data, it will be possible to introduce specific features for restaurant location (e.g. crime stats or HH income) and users (e.g. elite user, number of reviews, quality > of * reviews, etc.)
> * Small number of labeled reviews, single-reviewer labeling, and class imbalance
> * Did not harness corroborating data from CDC, health authority, etc.


--------


### Database

<p align = "left">
  <img src="https://i.ibb.co/w6Q8m6h/table.jpg" style = "width: 650px; height: 400px; margin-right: 50px;">

</p>

## Visualizations
<br>

### Map of PA, NJ, and DE locations within the Philadelphia metropolitan area.

<p align = "left">
  <img src="https://i.ibb.co/cxKGgHK/m3.png" style = "width: 500px; height: 200px; margin-right: 50px;">
  <img src="https://i.ibb.co/mtwPqh6/map.jpg" style = "width: 200px; height: 200px">  
</p>

<br>

### Minimum Topic Number Required to Include an Illness Topic: Outbreak Period and 2015 through 2021

<p align = "left">
  <img src="https://i.ibb.co/34h6Zy8/t5.jpg" style = "width: 400px; height: 200px; margin-right: 50px;">
  <img src="https://i.ibb.co/sJZMFjd/topic.jpg" style = "width: 430px; height: 200px">  
</p>

--------

## Conclusion

Companies spend billions of dollars annually on traditional consumer-based market research and analysis. By contrast, comparatively few studies have used a time-based NLP approach to examine and potentially harness social media sentiments for corporate crisis management, mitigation, and monitoring. This is perhaps the result of an existing bias that social media has less of an impact on and is less relevant for chain businesses. Using Chipotle as a documented crisis management subject area, this study examined the results of various common strategies (rating analysis, sentiment analysis, text-based classification, lexicon/dictionary extraction, and topic modeling) to extract potential managerial insights from store reviews. The results using a limited, but publicly available sample of Yelp data suggests that a review-centered, NLP-based analysis of thousands of written reviews has the potential to allow for better detection, monitoring, management, and mitigation of events such as food-borne illness and could be extended to other types of crises as well.

--------

## References

References 
Fang, A., & Ben-Miled, Z. (2017). Does bad news spread faster? In: 2017 International Conference on Computing, Networking and Communications (ICNC) (pp. 793–797). https://doi.org/10.1109/ICCNC.2017.7876232Al

Luca, M. (2016). Reviews, Reputation, and Revenue: The Case of Yelp.com. Harvard Business Review.Working Paper 12-016

Ajrawi, S., Agrawal, A., Mangal, H., Putluri, K., Reid, B., Hanna, G., & Sarkar, M. (2021). Evaluating business yelp's star ratings using sentiment analysis. Materials Today: Proceedings. https://doi.org/10.1016/j.matpr.2020.12.137

Chung, S., Chong, M., Chua, J. S., & Na, J. C. (2019). Evolution of corporate reputation during an evolving controversy. Journal of Communication Management, 23(1), 52–71. https://doi.org/10.1108/jcom-08-2018-0072

Estes, A. C. (2011, October 3). How Yelp helps steer people away from fast food chains. The Atlantic. Retrieved November 7, 2022, from https://www.theatlantic.com/business/archive/2011/10/how-yelp-helps-steer-people-away-fast-food-chains/337181/
Hutto, C., & Gilbert, E. (2014). Vader: A parsimonious rule-based model for sentiment analysis of social media text. Proceedings of the International AAAI Conference on Web and Social Media, 8(1), 216–225. https://doi.org/10.1609/icwsm.v8i1.14550 

Li, H. and Hecht, B. 2020. 3 Stars on Yelp, 4 Stars on Google Maps: A Cross-Platform Examination of Restaurant Ratings. In Proceedings of the ACM on Human-Computer Interaction, CSCW4, Article 254 (December 2020). 24 pages.
https://www.psagroup.org/static/publications/cscw2020-rating-camera-ready-Li-Hanlin.pdf

Liu, S. (2020). Sentiment Analysis of Yelp Reviews: A Comparison of Techniques and Models. ArXiv, abs/2004.13851. https://www.semanticscholar.org/paper/Sentiment-Analysis-of-Yelp-Reviews%3A-A-Comparison-of-Liu/d1889363bd7219105d734c434efac6b83e9bdb61

Luca, M. (2016). Reviews, reputation, and revenue: The case of yelp.com. Harvard Business Review. Retrieved November 7, 2022, from https://hbswk.hbs.edu/item/reviews-reputation-and-revenue-the-case-of-yelp-com

Opuszko, M., Berger, G., & Ruhland, J. (2019). The impact of public scandals on Social Media - A Sentiment Analysis on YouTube to Detect the Influence on Reputation. Conference: In ECSM 2019 6th European Conference on Social Media.

Schlosser, E. (2012). Fast Food Nation: The dark side of the all-american meal. Mariner Books/Houghton Mifflin Harcourt.
Yelp. (2022, February 10). 2022 Investor Presentation - February 2022. Retrieved November 7, 2022, from https://s24.q4cdn.com/521204325/files/doc_presentations/2022/Yelp-Investor-Presentation-Feb-2022.pdf.

Yelp Academic Dataset. https://www.yelp.com/dataset

--------


## License

Copyright (c) 2022, , Roberto Cancel, Nima Tamin Taghavi, Martin Zagari.

All source code and software in this repository are made available under the terms of the MIT license.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, and publish.

THE SOFTWARE IS PROVIDED "AS IS"
<br>

--------

## Acknowledgements
We would like to acknowledge our families for their patience as we complete this program. We would also like to acknowledge the professors throughout the program including Erin Cooke, M.S. and Anna Marbut, PhD(c) for their guidance throughout the capstone project. Additionally, we would like to acknowledge the SOLES Writing Center at the University of San Diego for their thorough review. 
