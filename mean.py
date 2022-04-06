import csv

with open("height-weight.csv" , newline = "") as f:
     r = csv.reader( f )
     file_data = list( r )

file_data.pop(0)

new_data = [] 
for i in range( len(file_data)):
     num = file_data[i][2]
     new_data.append( float(num) )

n = len(new_data) 
sum = 0
for x in new_data:
    sum += x
    # sum = sum + x


mean = sum / n
print (mean)