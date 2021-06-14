# conditional_plots.py
# Notes on DataQuest module for conditional plots
# 1. Introduction to Seaborn
# So far we learned how to use basic plots and how to visual represent data in
# palatable way. Now we're going explore how to quickly create multiple plots
# that are subsetted using on or more conditions.
# We'll use the seaborn visualizaiton library, which is built on top of matplotlib

# 2. Introduction to the Data set
# We'll be working with a data set of the passengers of the Titanic.
# Titanic shipwreck was famous and led to creation of better safety regulations.

# The data is contained in 2 files train.csv and test.csv
# Each row in both data sets represents a passenger on the Titanic, and
# some information about them. We'll be working with the train.csv file,
# because the Survived column, which describes if a given passenger survived
# the crash, is preserved in the file. The column was removed in test.csv,
# to encourage competitors to practice making predictions using the data.
# Here are descriptions for each of the columns in train.csv:
#
# PassengerId -- A numerical id assigned to each passenger.
# Survived -- Whether the passenger survived (1), or didn't (0).
# Pclass -- The class the passenger was in.
# Name -- the name of the passenger.
# Sex -- The gender of the passenger -- male or female.
# Age -- The age of the passenger. Fractional.
# SibSp -- The number of siblings and spouses the passenger had on board.
# Parch -- The number of parents and children the passenger had on board.
# Ticket -- The ticket number of the passenger.
# Fare -- How much the passenger paid for the ticket.
# Cabin -- Which cabin the passenger was in.
# Embarked -- Where the passenger boarded the Titanic.

# We want to remove columns like Name and Ticket which we won't be able to visualize
# We also want to remove any rows containing missing values because seaborn will
# throw erres when we try to plot missing values.

import pandas as pd

titanic = pd.read_csv('train.csv')
new_cols =['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
titanic= titanic[new_cols]

titanic = titanic.dropna()

# 3. Creating Histograms In Seaborn
import seaborn as sns    # seaborn is commonly imported as `sns`
import matplotlib.pyplot as plt
sns.distplot(titanic["Fare"])
plt.show()

#seaborn creates a smotther version of the histogram from pyplot called a kernel
# density plot.

# now we want to visualize the distribution of the 'Age' column
sns.distplot(titanic['Age'])
plt.show()

# 4. Generating a kernel Density plot
# We don't want the visual to be overwhelming so instead we'll use
sns.kdeplot(titanic['Age'])

# although the visual may be displayed more smoothly it but more difficult to
# estimate values visually
# we'll sahde the area under the plot to make it easier to do so
sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel('Age')

# we can adjust some of the visual feature of seaborn plots by using
# seaborn.set_style()
# we can also remove the spines by using sns.despine()

# we will change the backgroun color to white
sns.set_style('white')
sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel('Age')
sns.despine(left=True, bottom=True)

# 6. Conditional distributions using a single condition
# seaborn can help us create a small multiple by specifyingthe conditioning
# criteria  and the type of data visualization we want.
# One kernel density plot would visualize the distribution of values in the 'Age'
# column where Survived=0 and the other would be Survived=1

# Condition on unique values of the 'Survived' column.
g = sns.FacetGrid(titanic, col='Survived', size=6)
# For each subset of value, generate a kernel density plot of the 'Age' columns.
g.map(sns.kdeplot, 'Age', shade=True)

# We are now going to create a grid of plots that displays the age distributions
# for each class.
h = sns.FacetGrid(titanic, col='Pclass', size=6)
h.map(sns.kdeplot, 'Age', shade=True)
h.despine(left=True, bottom=True)
plt.show()

# 7. Creating Conditional Plots Using Two Conditions
# When using sns.FacetGrid() we can use the row parameter to
# specify the column in the dataframe we want used to subset acrros the rows in
# the grid.

# we going set the parameters to Pclass and Survived
g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

# 8. Creating Conditional Plots using 3 Conditions
# we set a third parameter for a our plots which would be the hue
# this would change the color of each plot
# we would simply set hue='col_name'
g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue='Sex', size=3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
plt.show()
g.add_legend()
