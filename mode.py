import csv

with open("height-weight.csv" , newline = "") as f:
     r = csv.reader( f )
     file_data = list( r )

file_data.pop(0)

new_data = [] 
for i in range( len(file_data)):
     num = file_data[i][2]
     new_data.append( float(num) )

import statistics

mode = statistics.mode (new_data)
print ("Mode of data is : " , mode)

mean = statistics.mean (new_data)
print ("Mean of data is : " , mean)

median = statistics.median (new_data)
print ("Median of data is : " , median)

