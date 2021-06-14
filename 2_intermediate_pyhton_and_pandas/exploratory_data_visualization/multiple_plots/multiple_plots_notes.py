import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

# for each subplot, matplotlib generated a coordinate grid that was similar to
# the one we generated using plot() function:

# The main difference is that this plot franged from 0 to 1.0 instead of from
# -.06 to 0.06

# we can now create multiple plots to compare monthly unemployment trends.
# This means we need to specify the position of each subplot on the grid.

# fig2 = plt.figure()
# ax21 = fig2.add_subplot(2,2,1)
# ax22 = fig2.add_subplot(2,2,2)
# ax23 = fig2.add_subplot(2,2,3)
# ax24 = fig2.add_subplot(2,2,4)

# y_values = [10, 20, 40]
# x_values = [0.0, 0.5, 1.0]
# ax1.plot(x_values, y_values)

first_twelve = unrate[0:12]
second_twelve = unrate[0:12]
ax1.plot(first_twelve['DATE'],first_twelve['VALUE'])
ax2.plot(second_twelve['DATE'],second_twelve['VALUE'])
plt.show()

#Now we need to resize the plots so that their bigger
# we will use the figsize parameter when calling plt.figure()
#fig = plt.figure(figsize=(width, height))
# we must keep in mind that the units for both lengths is inches

# We going to rewrite the code to make it a little more clear
# and add some titles and include the resizing
fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

#We want to now visualize dat a from a few more years to see if we find any
# evidence for seasonality between those years.
# This means we can use a loop to minimize repeatitive code.
# we are going to use python's range() function
# Ex:
# for i in range(5):
#     print(i)

# A way that we can use this to produce plots similar to the ones above
fig = plt.figure(figsize=(12,5))

for i in range(2):
    ax = fig.add_subplot(2,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])

plt.show()


# So now we'll rewrite the code to include
fig = plt.figure(figsize=(12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])
    ax.set_title('Monthly Unemployment Rate, {year}'.format(year = 1948+i))

plt.show()

# Unfortunately what we notice as we look across more years for seasonal trends
# we need have to scan over more space which is the same limitation we experienced
# when scanning the table representations of the same data
# We handle this by overlaying the line charts in a single subplot.

# Let's start by extrating the month values from the DATE column and assign
# them to a new column. So let's use the pandas.Series.dt accessor:
unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c ='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c = 'blue')
plt.show()


# Now we'll apply the same changes to all 5 plots
fig = plt.figure(figsize=(10,6))
colors = ["red", "blue", "green", "orange", "black"]
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset["MONTH"], subset["VALUE"], c = colors[i])

plt.show()

# Now we want to add a legend to clear up our plots as well as a title

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label = '{y}'.format(y=1948+i))
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()

# Some notes and thoughts. I think that choosing the right size of the figure
# is important in making sure that all the information fits well.
# Deciding on wether we want plots to overlay or be aside each other is an
# important choice to make in terms analyzing the data more easily.
# Making sure that not too many plots overlay each other is an important
# thing to consider.
