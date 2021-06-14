# bar_plots_and_scatter_plots_notes.py
# We want to investigate the potential bias that movie review sites have so we
# took compiled data of 147 films in 2015 from FiveThirtyEight which contains
# both critic and consumer reviews. This data set will used to investigate
# Fandango's ratings. Fangango has aggregate ratings but also sells movie
# tickets so there is a direct commercial interest in showing higher ratings.
# The file i'll be working with is fandango_scores.csv

#The columns in this data set:
# -FILM -film name
# -RT_user_norm - average user rating from Rotten Tomatoes, normalized to a 1-5
# -Metacritic_user_nom - average user rating from Metacritic, normalized to 1 to 5 point scale
# -IMDB_norm - average user rating from IMDB, normalized to a 1 to 5 point scale
# -Fandango_Ratingvalue - average user rating from Fandango, normalized to a 1 to 5 scale
# -Fandango_Stars - th rating displayed on the Fandango website(rounded to nearest star)


# Objective: investigate the potential bias that movie review sites have
# Goal: Practice visualizing data as bar and scatter plots in order to more
# easily analyze the data


# WE'll start off by first reading in the data set
import pandas as pd

reviews = pd.read_csv('fandango_scores.csv')

norm_reviews = reviews[['FILM','RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']]

# We're going to create a verticle bar plot in matplotlib that represents the different user scores for Avengers: Age of Ultron(2015)

# We can use pylot.bar() or Axes.bar()
# Axes.bar() has 2 parameters left and height.
# left specifies the x coordinates of the left sides of the bar
# height specifies the height of each bar
# they both accept a list like object

# np.arange() function returns evenly space values which can be used to help with
# our left parameter
# this function requires a parameter that specifies the number of values we want to generate

# We also want to add space between our bars for better readability

#Positions of the left sides of the 5 bars. [0.75, 1.75, 2.75, 3.75, 4.75]
from numpy import arange
bar_positions = arange(5) + 0.75

# Heights of the bars. In our case the average rating for the first movie in the dataset.
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)

plt.show()

# an optional parameter is width which specifies the width of each bar

#Now we're going practice adjusitng the tick labels and positions
tick_positions = range(1,6)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=90)

ax.set_xlabel("Rating Source")
ax.set_ylabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")

plt.show()

# We can create a horizontal bar plot in matplotlib in a similar fashion. Instead of using
# Axes.bar() we use Axes.barh()
# this has two required parameters which and are bottom and width
# bottom specifies the y coordinates for the bottom sids for the bars
# width specifies the length of the bars

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
ax.barh(bar_positions, bar_widths, 0.5)

# we need to be conscious of what we map on the y and x axis labels since what
# is on them is now switched

tick_positions = range(1, 6)
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm',
 'Fandango_Ratingvalue', 'Fandango_Stars']
 ax.set_yticks(tick_positions)
 ax.set_yticklabels(num_cols)

# Bar plots are good for quickly comparing a few data points but we can use
# scatter plots use visualize many data points.
# Scatter plots are helpful in seeing if 2 columns are weakly or strongly correlated
# It can help us find outliers, and can give us a more intuitive sense of how
# spread out the data is and compare more easily.

# We use Axes.scatter() to generate a scatter plot which has 2 required parameters:
# x and y are the parameters

# We'll create a scatter plot that visualizes the relationship between
# Fandango_Ratingvalue and RT_user_norm

fig, ax = plt.subplots()
ax.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["RT_user_norm"])
ax.set_xlabel("Fandango")
ax.set_ylabel("Rotten Tomatoes")
plt.show()

# Now we want to see how the plot compares if we switched the axis of the data points
# we want to compare them so we need to plot them both

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]

ax1.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')

ax2.scatter(norm_reviews['RT_user_norm'],norm_reviews['Fandango_Ratingvalue'])
ax2.set_xlabel('Rotten Tomatoes')
ax2.set_ylabel('Fandango')
plt.show()

# Now we want to compare all 3 of the other review sites with Fandango
# We will use Axes.set_xlim() and Axes.set_ylim() to limit the range
# of what's visualized in the plots

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
ax1.set_xlim(0,5)
ax1.set_ylim(0,5)

ax2.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['Metacritic_user_nom'])
ax2.set_xlabel('Fandango')
ax2.set_ylabel('Metacritic')
ax2.set_xlim(0,5)
ax2.set_ylim(0,5)

ax3.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['IMDB_norm'])
ax3.set_xlabel('Fandango')
ax3.set_ylabel('IMDB')
ax3.set_xlim(0,5)
ax3.set_ylim(0,5)

plt.show()

# From the scatter plots, we can conclude that user ratings from Metacritic and Rotten Tomatoes span a larger range of values than those from IMDB or Fandango. User ratings from Metacritic and Rotten Tomatoes range from 1 to 5. User ratings from Fandango range approximately from 2.5 to 5 while those from IMDB range approximately from 2 to 4.5.
#
# The scatter plots unfortunately only give us a cursory understanding of the distributions of user ratings from each review site. For example, if a hundred movies had the same average user rating from IMDB and Fandango in the dataset, we would only see a single marker in the scatter plot. In the next mission, we'll learn about two types of plots that help us understand distributions of values.
