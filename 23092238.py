"""
Created on 1/04/2021

@author: Juraj Janekovic
"""


def input_format(country):
    """
    Function which capitalizes the country input
    """
    country = [country.capitalize() for country in country]
    
    return country
        
def read_file(csvfile):
    """
    Function reads and finds the amount of lines in the csv file inputted.
    If the amount of lines is 0 then outputs an error message
    """
    with open(csvfile) as myfile:
        my_lines = myfile.readlines()
    
    return my_lines


def get_country_list(my_lines, country):
    """
    Function which creates a list of the countries data matching the search criteria
    Loop checks for matches in the country column and if match is found adds the row to a new list
    Returns the filtered out new list
    """
    country_list = []    
    for i in range(len(my_lines)): 
        split_lines = my_lines[i].strip('\n').split(',')      #removes the new row at the end and splits the data by the ","

        if split_lines[2] == country:
            country_list.append(split_lines[2:])     #adds all the data after the 2nd index to the country_list
    
    return country_list


def data_sorting(my_list):
    """
    Creates a new list with only seperated date characters which are then sorted by month
    """
    new_list = []
    for l in my_list:
        mydate = l[1].split('/')      #splits the date index by "/"
        new_list.append([mydate[1],l[0],mydate[0],mydate[2],l[2],l[3]])    # appends the date into the new_list by month first
    new_list.sort()
      
    return new_list


def data_calculation(sorted_list):
    """
    Function which performs calculations and returns minimum, maximum values, average and standard deviation
    """
    min_table = []
    max_table = []
    average_values = []
    std_dev = []
    
    for i in range (1,13):
        m = str(i).zfill(2)       #fills to 2 index spaces
        x = [int(l[4])for l in sorted_list if l[0] == m]   #
        if not x:
            x = [0]
                    
        avg_values = sum(x)/len(x)
        average_values.append(round(avg_values,4))
        
        if len(x) > 1:    # if the length of values in list x is greater than 0
            
            min_value = min(i for i in x if i > 0)
            min_table.append(min_value)
            
        else:
            min_table.append(0)
            
        #sets max value from list
        max_value = max(x)
        max_table.append(max_value)
        
        #calculates standard deviation
        std_dev1 = 0
        for z in range (len(x)):
            std_dev1 = std_dev1 + (x[z] - avg_values)**2
            std_final = (std_dev1 / len(x))**0.5
        std_dev.append(round(std_final,4))
                
    return(min_table, max_table, average_values, std_dev)    
    

def correlation(my_table1,my_table2):
    """
    Function which outputs the correlation between 2 countries inputted
    """
    
    avg1 = sum(my_table1)/len(my_table1)
    avg2 = sum(my_table2)/len(my_table2)
    
    top = 0
    bottom_left= 0
    bottom_right = 0
    for i in range (len(my_table1)):
        x_sum = my_table1[i] - avg1
        y_sum = my_table2[i] - avg2
        top += x_sum * y_sum
        bottom_left += x_sum**2
        bottom_right += y_sum**2  
    corr = top / ((bottom_left**0.5) * (bottom_right**0.5))
    return round(corr,4)
        
        

def main(csvfile,country,type):
    """
    Main function of the program which calls other functions
    """
    my_lines = read_file(csvfile)

    if type.strip() == "statistics":
        #calculates values if type is statistics
        country_list = get_country_list(my_lines, country.strip().title())
        sorted_list = data_sorting(country_list)       
        min_table, max_table, average_values, std_dev = data_calculation(sorted_list)
        return min_table, max_table, average_values, std_dev
    else:
        
        #calls function in creating lists 
        country = input_format(country)
        c1 = get_country_list(my_lines, country[0].strip().title())
        c1_sorted_list = data_sorting(c1)
        min_table1, max_table1, average_values1, std_dev1 = data_calculation(c1_sorted_list)
        
        c2 = get_country_list(my_lines, country[1].strip().title())
        c2_sorted_list = data_sorting(c2)
        min_table2, max_table2, average_values2, std_dev2= data_calculation(c2_sorted_list)
        
        #correlation calculations
        min_corr = correlation(min_table1, min_table2)
        max_corr = correlation(max_table1, max_table2)
        avg_corr = correlation(average_values1, average_values2)
        std_corr = correlation(std_dev1, std_dev2)
        
        return min_corr, max_corr, avg_corr, std_corr
        
        
        

        
       

    
    
    
    
    



