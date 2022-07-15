#Edit data.json with the appropriate names and run this file to generate random partners.
#Input: data.json file
#Output: a list of random names in pairs
#Note: The last pairing will consist of 3 names if there's
#an odd number of total students.

import json
import random

#initialize your variables
data = []
current_list = []
new_list = []

#load students from data.json 
with open('./data.json') as f:
    data = json.load(f)
    
#Store each students name in CURRENT_LIST
for student in data:
    current_list.append(student['name'])

#Get a random student's name from CURRENT_LIST and add it to a random index in NEW_LIST
class_size= len(current_list)
for i in range(class_size):
    new_list.insert(
        random.randint(0, len(new_list)),
        current_list.pop(random.randint(0, len(current_list)-1))
        )
#Print PairProgramming Partners for even number of students
if class_size % 2 == 0:
    for i in range(0, class_size, 2):
        print(f"{new_list[i]} => {new_list[i+1]}")
#Print PairProgramming Partners for odd number of students
else:
    for i in range(0, class_size-3, 2):
        print(f"{new_list[i]} => {new_list[i+1]}")
    print(f"{new_list[-3]} => {new_list[-2]} => {new_list[-1]}")
