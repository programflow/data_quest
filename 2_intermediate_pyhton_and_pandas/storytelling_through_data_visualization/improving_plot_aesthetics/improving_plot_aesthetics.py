# improving_plot_aesthetics.py
# These are notes on data_quest module from storytelling through data visualization
# course. This will expand on the information learned in Exploratory Data visualization.

# 1. Aesthetics
# We've already learned how to use visualization to explore and understand data.
# We now need to focus a bit on the presentation instead in order to make it more
# palatable for others. This will help communicate insights  and tell stories.

# We going to start with a standard matplotlib plot and improve it's appearance
# to better communicate the patterns we want the audience to understand.


# 2-3. Introduction to the Data
# The department of Educaiton Statistics releases a data set annually containing
# the percentage of bachelor's degrees granted to women from 1970 to 2012. The
# data set is broken up into 17 categories of degrees, with each column as a
# sepearate category.

# Randal Olson, a data scientist at University of Pensylvani, has cleaned the
# data set and made it available on his personal website.
# percent-bachelors-degrees-women-usa.csv

# He explored the the data set to explore the gender gap in STEM fields, which
# stands for science, technology, engineering, and mathematics. The gap is reported
# on often in the news and is controversial.

# We are going to explore how we can communicate the nuanced narrative of gender
# gap using effective data visualization.

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

# We want to generate a line chart that visualizes the historical percentage of
# Bio degrees awarded to women.
plt.plot(women_degrees['Year'], women_degrees['Biology'])
plt.xlabel('Year')
plt.ylabel('Biology')
plt.show()


# 4. Visualizing The Gender Gap

# From the plot we see a steady increase in degrees from 1970 to early 2000.
# The percentage has stayed above 50% since around 1987
# We need to something that makes the gender gap to be apparent and emphasized
# in the plot.

# If we visualize the trend of Biology degrees awarded to men on the same plot.
# we can see a relative change by observing the space between the lines for each
# gender. We can calculate the percentages of Bio degrees awarded to men by
# subtracting each value in the Bio column from 100. Once we have the male %
# we can generate the 2 line charts in the same diagram.

fig = plt.figure()
plt.plot(women_degrees['Year'], women_degrees['Biology'], c ='blue', label ='Women')
plt.plot(women_degrees['Year'], 100 - women_degrees['Biology'], c = 'green', label='Men')
plt.xlabel('Year')
plt.ylabel('Biology Degrees (%)')
plt.legend(loc='upper right')
plt.title('Percentage of Biology Degrees Awarded By Gender')
plt.show()


# 5. Data-Ink Ratio
# We get a more complete story when the 2 line charts are included.
# We can see that there were 2 periods. From 1970-1987 women were a minority the
# minority in bio. In 1987-2012 they became a majority.

# Our plot contains some extra visual elements that aren't necessary to understand
# the data. We are interested in helping people understand the gender gap in
# different fields across time.

# These excess elements, sometimes known as chartjunk, increase as we add
# more plots for visualizing the other degrees, making it harder for anyone
# trying to interpret our charts. In general, we want to maximize the data-ink
# ratio, which is the fractional amount of the plotting area dedicated to
# displaying the data.

# Non-data ink includes any elements in the chart that don't directly display
# data points. We need to be mindful to make sure to tell the write stor with
# our data having the a good data-ink ratio

# We want to improve our data-ink ratio, so we'll do:
# 1) remove all of the axis tick marks
# 2) hide the spines on each axis


# 6. Hiding Tick Marks
# We want use Axes.tick_params() method to modify the appearance of our tick
# marks. the parameters are bottom, top, left, right

fig = plt.figure()
plt.plot(women_degrees['Year'], women_degrees['Biology'], c ='blue', label ='Women')
plt.plot(women_degrees['Year'], 100 - women_degrees['Biology'], c = 'green', label='Men')
plt.tick_params(bottom = 'off', top = 'off', left = 'off', right = 'off')
plt.title('Percentage of Biology Degrees Awarded By Gender')
plt.legend(loc='upper right')
plt.show()

# 7. Hiding Spines
# In matplotlib spines are represented using matplotlib.spines.Spine class.
# In order to hide spines we need to:
# - access each Spine object in the dictionary
# - call the Spine.set_visible() method
# - pass in the Boolean value False
# ax.spines['right'].set_visible(False) removes the spine for the right axis

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], c='green', label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")

for key,spine in ax.spines.items():
    spine.set_visible(False)

ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()

# 8. Comparing Gender Gap Across Degree Categories
# so far matplotlib has set the limites automatically for each axis. We need to
# make sure that the axis ranges are consistent for the charts we are comparing.

# We are going generate line charts for 4 STEM degree categories on a grid to
# encourage comparison.

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    # Add your code here.
    ax.set_xlim(1968,2011)
    ax.set_ylim(0, 100)

    ax.tick_params(bottom="off", top="off", left="off", right="off")
    for key,spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_title(sp)
    if sp == 3:
        ax.legend(loc='upper right')

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()


# Looking at the charts we can conclude that the Gender Gap is large in CS and
# Engineering while the gap in Biology and Math and Statistics is quite small.
# The 1st 2 are dominated by men where the latter 2 are more balanced.

#
