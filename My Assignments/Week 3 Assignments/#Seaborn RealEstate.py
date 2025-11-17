#Seaborn RealEstate 
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('Week3/RealEstate-USA.csv',delimiter="," )

print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

#kind='hist'  
g=sns.displot(data=dffilter, x="brokered_by" , y="price" , hue="acre_lot",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=brokereby , y=price , hue=acre_lot,  kind='hist'  )"  )

#g.figure.show()
read = input("Wait for me....")

"""Plot univariate or bivariate histograms to show distributions of datasets.
A histogram is a classic visualization tool that represents the distribution of one or more variables by counting the number of observations that fall within discrete bins."""
#g = sns.histplot(data=dffilter, x='brokered_by', y='price', hue='acre_lot', multiple="stack")
#g.figure.suptitle("sns.histplot(data=dffilter, x='brokered_by', y='price', hue='acre_lot', multiple=stack)"  )
# Display the plot
#g.figure.show()
#read = input("Wait for me....")

"""Draw a scatter plot with possibility of several semantic groupings.
The relationship between x and y can be shown for different subsets of the data using the hue, size, and style parameters. These parameters control what visual semantics are used to identify the different subsets. It is possible to show up to three dimensions independently by using all three semantic types, but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e. both hue and style for the same variable) can be helpful for making graphics more accessible."""
# Use Seaborn to create a plot
g = sns.scatterplot(x='brokered_by', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='brokered_by', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


#https://seaborn.pydata.org/generated/seaborn.lineplot.html
"""Draw a line plot with possibility of several semantic groupings.

The relationship between x and y can be shown for different subsets of the data using the hue, size, and style parameters. These parameters control what visual semantics are used to identify the different subsets. It is possible to show up to three dimensions independently by using all three semantic types, but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e. both hue and style for the same variable) can be helpful for making graphics more accessible."""
g=sns.lineplot(data=dffilter, x="house_size" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=house_size , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()