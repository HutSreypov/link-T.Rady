studentsList = [
    {"id": 1, "name": "John", "age": 20, "gender": "male", "class": "A"},
    {"id": 2, "name": "Jane", "age": 21, "gender": "female", "class": "B"},
    {"id": 3, "name": "Bob", "age": 22, "gender": "male", "class": "C"},
    {"id": 4, "name": "Alice", "age": 23, "gender": "female", "class": "A"},
    {"id": 5, "name": "Tom", "age": 24, "gender": "male", "class": "B"},
    {"id": 6, "name": "Lucy", "age": 25, "gender": "female", "class": "B"},
    {"id": 7, "name": "Jack", "age": 26, "gender": "male", "class": "A"},
]
# 1 - How many students are there in the list?
# print(len(studentsList))   
#2 - How many students are there in each class?

# count={}
# for key in studentsList:
#     if key['class'] in count:
#         count[key['class']]+=1
#     else:
#         count[key['class']]=1
# print(count)

#3 - How many students are there in each gender?

# count={}
# for key in studentsList:
#     if key['gender'] in count:
#         count[key['gender']]+=1
#     else:
#         count[key['gender']]=1
# print(count)

#4 - How many students are there in each class and gender?

result = {}
for student in studentsList:
    cls = student["class"]
    gender = student["gender"]
    if cls not in result:
        result[cls] = {"male": 0, "female": 0}
    result[cls][gender] += 1
print(result)

#5 - Which class has the most students?
#6 - Which class has oldest students?
#7 - Which class has youngest student?


    
               