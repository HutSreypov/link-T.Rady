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

# countA =0
# countB =0
# countC =0
# for key in studentsList:
#     if key['class']=='A':
#         countA+=1
#     if key["class"]=='B':
#         countB+=1
#     if key["class"] == 'C':
#         countC+=1
# print('class A has:',countA)
# print('class B has:',countB)
# print('class C has:',countC)


# count={}
# for key in studentsList:
#     if key['class'] in count:
#         count[key['class']]+=1
#     else:
#         count[key['class']]=1
# print(count)

#3 - How many students are there in each gender?

# countMale=0
# countFemale=0
# for key in studentsList:
#     if key['gender']=='male':
#         countMale+=1
#     if key["gender"]=='female':
#         countFemale+=1
# print('Female:',countFemale)
# print('Male:',countMale)

# count={}
# for key in studentsList:
#     if key['gender'] in count:
#         count[key['gender']]+=1
#     else:
#         count[key['gender']]=1
# print(count)

#4 - How many students are there in each class and gender?


countMale=0
countFemale=0
for key in studentsList:
    if key['gender']=='male':
        if key['class']=='A':
            countMale+=1 
        elif key['class']=='B':
            
    else:

    

print('Female class A:',countFemale)
print('Male class B:',countMale)




       
# result = {}
# for student in studentsList:
#     cls = student["class"]
#     gender = student["gender"]
#     if cls not in result:
#         result[cls] = {"male": 0, "female": 0}
#     result[cls][gender] += 1
# print(result)

#5 - Which class has the most students?

#6 - Which class has oldest students?
#7 - Which class has youngest student?


    
               