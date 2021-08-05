#!/usr/bin/env python
# coding: utf-8

# # Project Description

# Write a brief description of your project here. 
# 
# Note that projects should be self-sufficient, so make sure to provide enough information and context here for someone to understand what you are doing in your project, and why. 

# This project will be a data analysis project focusing on two datasets:
# 1. A dataset that shows the amount of cars per 1000 people in each country
# 2. A dataset that shows the CO2 emissions in metric tons per capita in each country
# 
# The analysis will test the relationship between the amount of cars per 1000 people a country has, and the amount of CO2 emissions per capita the country has. The null hypothesis is: The amount of cars per 1000 people a country has no impact on its CO2 emissions. The alternative hypothesis is: the more cars per 1000 people a country has, the higher its CO2 emissions per capita will be.
# 
# In order to complete this project, I will have to clean the datasets to only incorporate countries with data in both datasets in the year 2014.
# 
# After cleaning the data, I will aggregate the datasets into one, and plot the data to reveal the relationship between the two variables. 
# 
# The data I used for cars is from: https://www.nationmaster.com/country-info/stats/Transport/Road/Motor-vehicles-per-1000-people#
# 
# The data I used for CO2 emissions is from: https://data.worldbank.org/indicator/EN.ATM.CO2E.PC
# 
# 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


from my_module.functions import remove_nans
from my_module.functions import choose_columns
from my_module.functions import summary_stats

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import nan


# In[2]:


#here you can see the raw dataframes

df_co2 = pd.read_csv('data/co2.csv')
df_cars = pd.read_csv('data/vehicles_per_1000.csv')

display(df_cars)
display(df_co2)


# In[3]:


# this will clean the df_co2 dataframe by removing nans and selecting only the relevant columns
df_co2 = remove_nans(df_co2, '2014')
df_co2 = choose_columns(df_co2, 'Country Name', '2014')


# this will clean the df_cars dataframe by removing nans
# additionally, the csv file originally stored all the amounts of cars as strings, so we must
# strip the strings of the commas and turn them into integers
df_cars = remove_nans(df_cars, 'Amount')
df_cars['Amount'] = df_cars['Amount'].str.replace(",", "")
df_cars['Amount'] = pd.to_numeric(df_cars['Amount'])


# this will rename the columns so that they make more sense to read, and will also make it easier for us
# to merge the two dataframes later
df_co2 = df_co2.rename(columns =  {'Country Name' : 'Country', '2014': "CO2 Emissions"})
df_cars = df_cars.rename(columns = {'Amount': 'Cars'})

# now we can look at pandas dataframes that show the summary statistics of each dataframe we cleaned
display(summary_stats(df_co2, 'CO2 Emissions'))
display(summary_stats(df_cars, 'Cars'))


# In[4]:


# here we have the merged dataframes, where we concatuate the two dataframes on the "country" column
# this only keeps the data for which there is information on both CO2 emissions and Cars for that country

df_merged = pd.merge(df_co2, df_cars, on = "Country")
df_merged = choose_columns(df_merged, 'Country', "CO2 Emissions", "Cars")

display(df_merged)


# In[5]:



get_ipython().system('pytest tests.py')


# In[6]:


# set x variable to the independent variable, cars per capita
x  = np.array(df_merged["Cars"])
# set y variable to dependent variable, CO2 emissions per capita
y = np.array(df_merged["CO2 Emissions"])

# find the slope and y intercept of the line of best fit
m, b = np.polyfit(x, y, 1)

# establish the size of the plot
plt.figure(figsize = (20, 10))
# create the scatter plot, line of best fit, and labels
plt.scatter(x, y, alpha = .3)
plt.plot(x, m * x + b, color = "k")
plt.xlabel("Number of Cars per 1000 people")
plt.ylabel("CO2 Emissions per Capita (in metric tons)")
plt.title("Relationship between Amount of Cars and CO2 Emissions")


# In[7]:


# find R-squared value of the regression 
correlation = np.corrcoef(x, y)
r_squared = correlation[0, 1] ** 2

print("Slope: \t", m)
print("R-Squared: \t", r_squared)


# The graph above shows the raw analysis of cars per 1000 people and CO2 emissions per capita. There is a dense concentration of points in the bottom left, mostly because there is are a few countries with a disproportionate amount of CO2 emissions per capita and cars per 1000 people. The R-squared calculated for this relationship shows a solid but not great line of best fit. 

# In[8]:


# this plot will take all the same data, but we will take the log of cars and co2 emissions since in the first
# plot, a lot of the data points were concentrated into one area, obscuring the real impact of number of 
# cars per capita on co2 emissions per capita

# set x variable to the independent variable, cars per capita
log_x = np.log(x)
# set y variable to dependent variable, CO2 emissions per capita
log_y = np.log(y)

# find the slope and y intercept of the line of best fit
log_m, log_b = np.polyfit(log_x, log_y, 1)


# establish the size of the plot
plt.figure(figsize = (20, 10))
# create the scatter plot, line of best fit, and labels
plt.scatter(log_x, log_y, alpha = .5, color = "b")
plt.plot(log_x, log_m * log_x + log_b, color = "r")
plt.xlabel("Log of Number of Cars per 1000 people")
plt.ylabel("Log of CO2 Emissions per Capita (in metric tons)")
plt.title("Relationship between Amount of Cars and CO2 Emissions")


# In[9]:


# find R-squared of the regression
correlation = np.corrcoef(log_x, log_y)
r_squared = correlation[0, 1] ** 2

print("Slope: \t", log_m)
print("R-squared: \t", r_squared)


# The graph above shows the relationship between the log of the number of cars per 1000 people and CO2 emissions per capita. In the first graph, we saw a heavy concentration of points on the lower ends of the axis, thus I took the log of each axis in order to make the spread of the variables more even. In this graph, we can more clearly see the relationship between the dependent and independent variable. The R-squared value also tells us that this line better predicts the data than the first graph. 

# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. Your Python Background
# 2. How your project went above and beyond the requirements of the project and/or how you challenged yourself to learn something new with the final project
# 
# My only python experience is taking CSS 1 last quarter which is "Introductory Programming for Computational Social Science". I think my project went above and beyond because I utilized a lot of pandas and matplotlib functionality that was not taught in class. Although my code doesn't look like that much, I tried my best to find built-in functions that kept everything concise and easy to read. 

# In[ ]:




