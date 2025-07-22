# Ex-1
arr=eval(input())
result={}
for i in range(len(arr)):
    result[arr[i]]=i
print(result)

# Ex-2
result=[]
arr2D =eval(input())
col_index = int(input())
if col_index < 0 or col_index >= len(arr2D[0]):
    result = 'Out of range'
else:
    for row in arr2D:
        result.append(row)
        row[col_index] = '*'
print( result)

# Ex-3
arr=eval(input())
array=[]
for num in arr:
    for i in range(len(num)):
        if num[i]==6:
            num[i]= 10
    array.append(num)
print(array)

# Ex-4
arr=eval(input())
array=[]
for num in arr:
    if num <= 10:
        num = 10
    array.append(num)
print(array)


# Ex-5
arr=eval(input())
new_arr=[]
array=len(arr[0])
for i in range (array):
    sum=0
    for num in arr:
        sum+=num[i]
    new_arr.append(sum//len(arr))
print(new_arr)

# Ex-6
arr=eval(input())
array=[]
for num in arr:
    countOdd=0
    for i in range(len(num)):
        if num[i] %2==1:
            countOdd+=1
    array.append(countOdd)
print(array)

# Ex-7
arr=eval(input())
array=[]
for num in arr:
    max=0
    for i in range(len(num)):
        if num[i] > max:
            max = num[i]
    array.append(max)
print(array)

# Ex-8
arr=eval(input())
num= len(arr[0])
array=[]
for col in range(num):
    values = []  
    for number in arr:
        values.append(number[col])
    min_value = min(values)
    array.append(min_value)
print(array)

# Ex-9
arr=eval(input())
array=[]
for num in arr:
    sum=0
    for i in range(len(num)):
        sum+=num[i]
    array.append(sum)
print(array)


# Ex-10
arr=eval(input())
new_arr=[]
for i in range(len(arr[0])):
    sum=0
    for number in arr:
        sum+=number[i]
    new_arr.append(sum)
print(new_arr)