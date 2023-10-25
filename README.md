# Predicting Funding Flows in Public and Private Markets

## Overview
This GitHub repository contains the culmination of months of intensive research, analysis, and collaboration by a team of four students pursuing their Master of Science in Data Science at Michigan State University under the expert guidance of Professor Mohammad Ghassemi.

## Project Description
The world of finance is characterized by ever-shifting dynamics, where investors and decision-makers strive to anticipate market trends and make informed decisions. Predicting funding flows is a critical aspect of this process, as it can offer invaluable insights into market sentiment, economic conditions, and investment opportunities.

Our project aims to provide a robust framework for forecasting funding flows in public and private markets by harnessing the power of data science, time series analysis, and NLP. We understand that predicting funding flows is a challenging task due to the multifaceted nature of market data and the influence of external factors. However, we believe that a combination of advanced data analysis and machine learning techniques can help us make significant strides in this domain.

## Dataset
### Data Collection
We have collected data from various sources encompassing both open and proprietary datasets. In the academic domain, our sources include well-known repositories like Arxiv, S2ORC, and Crossref. In the financial domain, we have accessed data from Refinitive Workspace, Pitchbook, Crunchbase, and others.

For a comprehensive list of the datasets we have explored and detailed information about their features, please refer to the table available in [Datasets](static/datasets.md).

After conducting a thorough analysis of these datasets, taking into account factors such as feature richness and data update frequency, we have made the strategic decision to primarily utilize S2ORC for academic data, which comprises an extensive collection of research papers. Additionally, we have chosen to incorporate data from Refinitive Workspace to provide comprehensive coverage of the financial domain. The resources used to collect these two datasets are provided in the aforementioned Datasets table.

### Data Preprocessing
- @Vishal and @Parth data joining or any inital Steps taken. 
- Mention about which specific fields are being used from the dataset and their explanation 

## Algorithm
### 1. Keyword/Topic/Phrase Identification
This step focuses on the automatic identification of keywords, topics, and phrases that serve as the core elements within research papers and company overviews. This critical step aims to extract and highlight the central themes and concepts present in textual documents. This process lays the groundwork for comprehensive data analysis and deeper insights into the relationships between financial data and research findings.

Below are the methods we are experimenting with for this step :  
1. **Noun Phrase Identification** : Unsupervised noun phrase identification using the Gensim and NLTK libraries. 
2. **BertTopic** : Using BertTopic package to identify topics using pretrained language models.

### 2. Cross Domain Topic Mapping
This step is designed to facilitate the mapping of keywords and topics extracted from academic research papers to the financial domain. By doing so, it empowers researchers and analysts to delve into the intricate relationships between funding flows and ongoing academic research. Through this mapping process, we aim to gain deeper insights into how financial factors intersect with and influence the world of academia.

We are experimenting with the below methods to create this mapping 
1. Word Embedding with Cosine Similarity
2. Word Embedding and Char-Based Features with Cosine Similarity
3. DBPedia Concept Normalization and Relationship Graph

### 3. Time Series Modelling
### 4. Visualization
**Basic Plotting** : @Nithya add the visualizations you have done till now 

[Team](static/Teams.md)

[Updates](static/Updates.md)

[Tutorials/Examples](static/Tutorials.md)


