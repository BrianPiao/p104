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
new_data.sort()

# floor division is shown by //
if n % 2 == 0:
     m1 = float (new_data[n // 2])
     m2  = float (new_data [n // 2 - 1])
     median = (m1+m2)/2
else :
    median = new_data [n // 2]
print (median)