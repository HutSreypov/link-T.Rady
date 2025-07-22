# Ex=1
# numbers=[1,3,4,5,6,9,2,]
# arr=[]
# for i in range(len(numbers)):
#     if numbers[i]==5:
#         numbers[i]=10
#     arr.append(numbers[i])
# print(arr)

# numbers=[1,3,4,5,6,9,2,]
# arr=[]
# for num in numbers:
#     if num %2==0:
#         num=100
#     arr.append(num)
# print(arr)


# numbers=[1,3,4,5,6,9,2]
# index=0
# for i in range(len(numbers)):
#     if numbers[i]==9:
#         index=i
# numbers.pop(index)
# print(numbers)
        
# numbers=[1,3,4,5,6,9,2,]
# numbers.append(404)
# print(numbers)


# Ex-2
# numbers=[1,3,4,5,6,9,2]
# for num in numbers:
#     print(num)

# numbers=[1,3,4,5,6,9,2]
# for i in range(len(numbers)):
#     if numbers[i]==5:
#         print(i)

# numbers=[1,3,4,5,6,9,2]
# for i in range(len(numbers)):
#     if numbers[i]==9:
#         print(i)

# numbers=[1,3,4,5,6,9,2]
# countOdd=0
# for num in numbers:
#     if num %2==1:
#         countOdd+=1
# print(countOdd)

# numbers=[1,3,4,5,6,9,2]
# sum=0
# for num in numbers:
#     sum+=num
# print(sum)


# numbers=[1,3,4,5,6,9,2]
# sum=0
# for num in numbers:
#     if num %2==0:
#         sum+=num
# print(sum)

# numbers=[1,3,4,5,6,9,2]
# max =numbers[0]
# for i in range(len(numbers)):
#     if numbers[i] > max:
#         max=numbers[i]
# print(max)


# numbers=[3,1,4,5,6,9,2]
# min =numbers[0]
# for num in numbers:
#     if num < min:
#          min=num
# print(min)


# Ex-3
# fruits=['banana','coconut']
# print(len(fruits))

# fruits=['banana','coconut']
# for char in fruits:
#     print(char)

# fruits=['banana','coconut']
# fruits.append('mango')
# print(fruits)

# fruits=['banana','coconut']
# arr=[]
# for char in fruits:
#     if char=='banana':
#         char='apple'
#     arr.append(char)
# print(arr)

# fruits=['banana','coconut']
# fruits.remove('coconut')
# print(fruits)


# fruits=['banana','coconut']
# count=0
# for i in range(len(fruits)):
#     for x in range(len(fruits[i])):
#         if fruits[i][x]=='n':
#             count+=1
# print(count)
        
# fruits=['banana','coconut']
# count=0
# for i in range(len(fruits)):
#     if fruits[i]=='banana':
#         for x in range(len(fruits[i])):
#             count+=1
# print(count)

# Ex-4
# students=['bopha','dara','kanha','theara']
# print(len(students))

# students=['bopha','dara','kanha','theara']
# for char in students:
#     print(char)

# students=['bopha','dara','kanha','theara']
# students.append('viza')
# print(students)

# students=['bopha','dara','kanha','theara']
# count=0
# for i in range(len(students)):
#     for x in range(len(students[i])):
#         if students[i][x].lower()=='a':
#             count+=1
# print(count)


# students=['bopha','dara','kanha','theara']
# for i in range(len(students)):
#     print(students[-i-1])

# students=['bopha','dara','kanha','theara']
# text=[]
# for char in students:
#     if char=='bopha' or char=='theara':
#         text.append(char)
# print(text)

# students=['bopha','dara','kanha','theara']
# arr=[]
# for char in students:
#     if char=='dara':
#         char='villa'
#     arr.append(char)
# print(arr)


# students=['bopha','dara','kanha','theara']
# arr=[]
# for num in students:
#     result=''
#     for i in range(len(num)):
#         result+=str(num[-i-1])
#     arr.append(result)
# for x in range(len(arr)):
#     print(arr[-x-1])


# students=['bopha','dara','kanha','theara']
# arr=[]
# for num in students:
#     result=''
#     for i in range(len(num)):
#         result+=str(num[-i-1])
#     arr.append(result)
# for x in range(len(arr)):
#     print(arr[-x-1])


# text=input()
# if 6 > len(text)>4 or 8 >len(text)>10 :
#     print("It's medium!")
# elif len(text)<=3:
#     print("It's small!")
# elif len(text)==7:
#     print("It's exactiy the average!")
# else:
#     print("It's big!")


    

    
               