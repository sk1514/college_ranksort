import csv
from operator import itemgetter

with open('college_rank.csv', 'r') as file:

    unsorted_list=[]
    reader = csv.reader(file)
    for row in reader:
        unsorted_list.append(row)

    sorted_list=sorted(unsorted_list, key=lambda x: float(x[3]))

  

    

    with open('final_college_rank.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sorted_list)