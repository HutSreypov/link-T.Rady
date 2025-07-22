# Ex-1
def find_first_index(arr):
    is_first = False
    for i in range(len(arr)):
        if arr[i] == 7 and not is_first:
            is_first = True
            index = i
    return index        
def has_seven(arr):
    result = False
    for num in arr:
        if num == 7 :
            result = True
    return result
number = int(input())
array = []
for i in range(number):
    array.append(int(input()))
if has_seven(array):
    print("7 index is:", find_first_index(array))
else:
    print("No 7 entered")

# Ex-2

text=input()
A=5
a=10
sum=0
for char in text:
    if char == 'A':
        sum+=A
    elif char == 'a':
        sum+=a
    else:
        sum+=1
print('The total score is:',sum)

# Ex-3


i = 0
array = {}
index = 0
while i <= 2:
    user = input()
    array[user] = len(user)
    if len(user) > index:
        index = len(user)
    i += 1
for key in array:
    if array[key] == index:
        print(key)


# Ex-4

text=input()
countA=0
countB=0
for char in text:
    if char == 'A':
        countA+=1
    if char == 'B':
        countB+=1
if countA>countB:
    print('WELL DONE')
else:
    print('LOST')


# Ex-5

text=input()
result=''
for char in text:
    if char != 'A':
        result+= char
if len(result) >0:
    print('LOST')
else:
    print('WELL DONE')


# Ex-6

text=input()
countA=0
countB=0
for char in text:
    if char == 'A':
        countA+=1
    if char == 'B':
        countB+=1
if countA==2 and countB==2:
    print('WELL DONE')
else:
    print('LOST')

# Ex-7

text = input()
i = 0
lenText = len(text) 
while i < lenText :
    if i == 0 :
        print(text)
    else:
        print(text[:-i])
    i += 1

# Ex-8

text=input()
if len(text)<=3:
    print("It's small!")
elif 4<len(text)<6 or 8<len(text)<10:
    print("It's medium!")
elif len(text)==7:
    print("It's exactly the average!")
else:
    print("It's big!")

# Ex-9
user = input()
print('Y'*len(user))

# Ex-10

number=int(input())
text=input()
for i in range(number):
    print(text)