import pandas as pd



#remove rows with nans in the year we are looking at
def remove_nans(dataframe, column):
    """removes all nans from the column in the dataframe
    
    parameters:
        dataframe: takes a pandas dataframe
        column: takes the name of a column in the specified dataframe
        
    returns:
        dataframe: the modified dataframe with all nans removed
    """
    
    dataframe = dataframe[dataframe[column].notna()]
    dataframe = dataframe.reset_index(drop = True)
    return dataframe


#function will create dataframe with only desired columns 
def choose_columns(dataframe, *columns):
    """selects a subset of columns from the given dataframe
    
    parameters:
        dataframe: takes a pandas dataframe
        *columns: takes in a variable amount of column names in the specified dataframe
        
    returns: 
        dataframe: returns the modified dataframe with only the selected columns
    """
    
    columns_list = [column for column in columns]
    dataframe = dataframe[columns_list]
    return dataframe


#will take in a dataframe and column and provide the summary statistics (max, min, standard deviation, median, mean)
def summary_stats(dataframe, column):
    """finds the summary statistics of a dataframes' specified column
    
    parameters: 
        dataframe: a pandas dataframe
        column: a column in the dataframe
        
    returns:
        output: a pandas dataframe containing the summary statistics
        
    """
    
    #initialize lists to later make dataframe
    stats_list = []
    country_list = []
    stats_names = ['Max', "Min", 'Standard Deviation', 'Mean', "Median"]
    
    #calculate max
    row_num = dataframe[column].idxmax()
    country = dataframe.iloc[row_num]["Country"]
    measure = dataframe.iloc[row_num][column]
    stats_list.append(measure)
    country_list.append(country)
    
    #calculate min
    row_num = dataframe[column].idxmin()
    country = dataframe.iloc[row_num]["Country"]
    measure = dataframe.iloc[row_num][column]
    stats_list.append(measure)
    country_list.append(country)

    #calculate standard variation
    measure = dataframe[column].std()
    stats_list.append(measure)
    country_list.append('n/a')
    
    #calculate mean
    measure = dataframe[column].mean()
    stats_list.append(measure)
    country_list.append('n/a')
    
    #calculate median
    measure = dataframe[column].median()
    stats_list.append(measure)
    country_list.append('n/a')
   
    #create dataframe
    d = {'Measure': stats_names, "Statistics": stats_list, 'Country' : country_list}
    output =  pd.DataFrame(data = d)
    return output