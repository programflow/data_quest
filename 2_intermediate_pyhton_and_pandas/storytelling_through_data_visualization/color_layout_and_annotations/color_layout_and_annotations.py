# color_layout_and_annotations.py
# 1. Introduction
# Previously we've learned some basic techniques and principles for making our plots
# more aesthetic. We will now focus on customizing colors, line widths, layout,
# and color_layout_and_annotations to improve the ability for a viewer to extract
# insights from the charts
# We will use the same data as improving_plot_aesthetics.py (percent-bachelors-degrees-women-usa.csv)

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']

fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

plt.legend(loc='upper right')
plt.show()

# 2. Color
# We need to be mindful of color blindness so we need to make sure that our
# data representations are made of specific palettes. One specific palette is
# called colorblind 10.

# 3. Setting Line Color Using RGB
# The colors use RGB values. The RGB color model describes how the three primary
# colors can be combined to form any secondary color. The values range from 0 to
# 255
# The 10 colors are
# 1) 0.107.164
# 2) 255.128.14
# 3) 89.89.89
# 4) 95.158.209
# 5) 200.82.0
# 6) 137.137.137
# 7) 162.200.236
# 8) 255.188.121
# 9) 171.171.171
# 10) 207.207.207

# We need to scale the color range so that vlaues are mapped in between 0 and 1.

# THe dark blue color code is going to be used and the orange color.
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    # The color for each line is assigned here.
    cb_dark_blue = (0/255, 107/255, 164/255)
    cb_orange = (255/255, 128/255, 12/255)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c=cb_dark_blue, label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_orange, label='Men')
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

plt.legend(loc='upper right')
plt.show()

# 4. Setting Line width
# We want to increase the line width of the plots to emphasize them more.
# in the Axes.plot() method we can use a parameter called linewidth.

cb_dark_blue = (0/255, 107/255, 164/255)
cb_orange = (255/255, 128/255, 14/255)

fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    # Set the line width when specifying how each line should look.
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

plt.legend(loc='upper right')
plt.show()

# 5. Improve the Layout and Ordering
# To make the viewing experience more coherent, we can:
# - use layout of a single row with multiple columns
# - order the plots in decreasing order of initial gender gap
# or
# order them increasing ending gender gap

stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

plt.legend(loc='upper right')
plt.show()

# 6. Replacing the Legend with annotations
# legends can often take up valuable space and can be represented more simply
# with annotations. We need to consider the position of the annotation so that
# it also helpls convey a message.

#7. Annotating in Matplotlib
# We can use the Axes.text() method for annotations
# the parameters are x, y, and s
# The values in the coordinate grid match exactly with the data ranges for the
# x-axis and the y-axis. If we want to add text at the intersection of 1970
# from the x-axis and 0 from the y-axis, we would pass in those values:
# ax.text(1970, 0, "starting point")

fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    if sp == 0:
        ax.text(2005,87,"Men")
        ax.text(2002,8,"Women")
    elif sp == 5:
        ax.text(2005,62,"Men")
        ax.text(2001,35,"Women")

plt.show()

# We learned to improve the viewing experience by making plots using more
# color-blind friendly and thickening the line widths.
# we then explored how to use the layout and ordering of the plots as well as
# annotations directly onto the plots to enhance the story being told.
#
