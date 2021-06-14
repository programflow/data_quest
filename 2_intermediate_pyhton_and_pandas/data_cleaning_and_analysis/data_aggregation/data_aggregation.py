# data_aggregation.py
# module 1 out of 6 on data cleaning and analysis

# 1. Introduction
# So far, we've learned how to use the pandas library and how to create
# visualizations with data sets that didn't require much cleanup. Now we need
# to learn how to properly clean up the data in order to be able to manipulate
# data quickly and efficiently.

# We'll learn how to:
# - Data aggregation
# - how to combine data
# - how to transform data
# - how to clean strings with pandas
# - how to handle missing and duplicate data

# Prerequiste knowledge:
# -basic knowledge of pandas dataframes and series
# - how to select values and filter a dataframe
# - knowedge of data exploration methods in pandas
# - how to create visualizations in pandas and matplotlib

# The data we'll work with an annual report created by the UN Sustainable Developement
# Solutions Network called the World Happiness Report. It's intent is to guide policy.
# It assigns each country a Happiness score based on answers to poll questiolns.
# It includes factors that may contribute to each country's Happiness. The factors
# aren't necessarily used in the calculation but can help us undesrstand why
# a certain score was given.

# we want to answer the following Questions:
# 1) How can aggregating data give us more insight into happiness scores?
# 2) How did world happiness change from 2015 to 2017?
# 3 Which factors contribue the most to the happiness score?

# In this module we'll learn how to aggregate data.


# 2. Introduction to the Data
# The data we'll be working with is called 'World_Happiness_2015.csv'

# Here are the columns we'll be working with:
# - Country - Name of the country.
# - Region - Name of the region the country belongs to.
# - Happiness Rank - The rank of the country, as determined by its happiness score.
# - Happiness Score - A score assigned to each country based on the answers to a poll question that asks respondents to rate their happiness on a scale of 0-10.
# - Family - The estimated extent to which family contributes to the happiness score.
# - Freedom - The estimated extent to which freedom contributes to the happiness score.
# - Generosity - The estimated extent to which generosity contributes to the happiness score.

# We're going to start by reading in our data set
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

happiness2015 = pd.read_csv('World_Happiness_2015.csv')

first_5 =happiness2015.head(5)
happiness2015.info()
