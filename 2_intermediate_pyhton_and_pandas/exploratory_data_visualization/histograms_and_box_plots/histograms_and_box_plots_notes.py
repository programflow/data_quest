# histograms_and_box_plots_notes.py

# We are going to learn how to visualize the distributions of user ratings using
# histograms and box plots. We're going to work with the same data set as
# the bar_plots_and_scatter_plots_notes.py file i.e. fandango_scores.csv

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
print(norm_reviews[:5])

# Frequency distributions
# We want to compare the freq distributions of user ratings from Fandango and IMDB
# We'll use Series.value_counts()

fandango_freq_counts = norm_reviews["Fandango_Ratingvalue"].value_counts()

# This ordering isn't the most helpful when trying to understand the range that
# valeus span
# We can use Series.sort_index() to sort the Frequency distributions

fandango_distribution = fandango_freq_counts.sort_index()

imdb_freq_counts = norm_reviews['IMDB_norm'].value_counts()
imdb_distribution = imdb_freq_counts.sort_index()

print(fandango_distribution)
print(imdb_distribution)

# To make our analysis easier we have to make the two series comparable. So are
# going to use a technique called binning. So that both series data points are
# easier to compare.

#We are going to use this with a histogram which automatically does the binning
# Axes.hist()
# has only 1 required parameter, an iterable object containing the values we
# want a histogram for

# we want to specify the range though so other wise there would 10 bins arranged
# in a way we don't necessarily want
fig, ax = plt.subplots()
ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(0,5))
plt.show()

# Question: What percent of the ratings are contained in the 2.0 to 4.0 range?
# For increased resolution we will use 20 bins instead of 10
# and we use multiple histograms

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews['Fandango_Ratingvalue'], bins=20, range=(0, 5))
ax1.set_title('Distribution of Fandango Ratings')
ax1.set_ylim(0, 50)

ax2.hist(norm_reviews['RT_user_norm'], bins=20, range=(0, 5))
ax2.set_title('Distribution of Rotten Tomatoes Ratings')
ax2.set_ylim(0, 50)

ax3.hist(norm_reviews['Metacritic_user_nom'], bins=20, range=(0, 5))
ax3.set_title('Distribution of Metacritic Ratings')
ax3.set_ylim(0, 50)

ax4.hist(norm_reviews['IMDB_norm'], bins=20, range=(0, 5))
ax4.set_title('Distribution of IMDB Ratings')
ax4.set_ylim(0, 50)

plt.show()

# From the histograms, we can make the following observations:
#
# Around 50% of user ratings from Fandango fall in the 2 to 4 score range
# Around 50% of user ratings from Rotten Tomatoes fall in the 2 to 4 score range
# Around 75% of the user ratings from Metacritic fall in the 2 to 4 score range
# Around 90% of the user ratings from IMDB fall in the 2 to 4 score range

#Now we are going to try to analyze using quartiles using box plots(box and whisker)

fig, ax = plt.subplots()
ax.boxplot(norm_reviews['RT_user_norm'],)
ax.set_ylim(0,5)
ax.set_xticklabels(['Rotten Tomatoes'])
plt.show()

# We create a single subplot generate a box plot containing a box and whisker
# diagram for each column

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

fig, ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,5)
plt.show()
