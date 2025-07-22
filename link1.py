# Ex-1
arr=eval(input())
result = {} 
for i in range(len(arr)):
    result[arr[i]] = i
print(result)

# Ex-3
arr=eval(input())
array=[]
for text in arr:
    sum=''
    for i in range(len(text)):
        sum +=str(text[i]).lower()
    array.append(sum)
print(array)
       

# Ex-4
arr=eval(input())
countFruit=0
countMeat=0
for key in arr:
    for num in key:
        if num == 'fruit':
            countFruit+=1
        if num == 'meat':
            countMeat+=1
print('Fruit:'+str(countFruit))
print('Meat:'+str(countMeat))

# Ex-5
result=[]
arr=eval(input())
num=int(input())
if num < 0 or num >= len(arr[0]):
    result= 'Out of range'
else:
    for array in arr:
        result.append(array)
        array[num]='*'
print(result)


# Ex-6
def deleteSix (arr):
    for i in range(len(arr)):
        for x in range(len(arr[i])):
            if arr[i][x]==6:
                arr[i][x]=10
    return arr
arrays=eval(input())
print(deleteSix(arrays))

# Ex-7
arr=eval(input())
new_arr=[]
array=len(arr[0])
for i in range (array):
    sum=0
    for num in arr:
        sum+=num[i]
    new_arr.append(sum//len(arr))
print(new_arr)

# Ex-8
arr = eval(input())
array=[]
for i in range(len(arr)):
    count=0
    for num in arr[i]:
        if num %2==1:
            count+=1
    array.append(count)
print(array)

# Ex-9
arr=eval(input())
array=[]
for i in range(len(arr)):
    max=0
    for num in arr[i]:
        if num > max:
            max = num
    array.append(max)
print(array)

# Ex-10
arr=eval(input())
array=[]
for col in range(len(arr[0])):
    values = []  
    for number in arr:
        values.append(number[col])
    min_value = min(values)
    array.append(min_value)
print(array)

# Ex-11
arr=eval(input())
array=[]
for i in range(len(arr)):
    sum=0
    for num in arr[i]:
        sum+=num
    array.append(sum)
print(array)

# Ex-12
arr=eval(input())
sum=0
total=0
for i in range(len(arr)):
    if arr[i]%2==1:
        total+=arr[i]
        sum+=1
print(total//sum)


# Ex-13
text=input()
result=''
for i in range(len(text)):
    result += text[-i-1]
print(result)


# Ex-14
name = input()
name=name.lower()
if 'rady' in name:
    print('Yes')
else:
    print('No')

# Ex-15
arr=eval(input())
array=[]
for num in arr:
    if num not in array:
        array.append(num)
result = ""
for number in array:
    result += str(number)
    result+=' '
print(result)


