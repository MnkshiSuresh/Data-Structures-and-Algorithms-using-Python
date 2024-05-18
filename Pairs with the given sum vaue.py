'''Pairs with given sum value'''

num = int(input("enter the no of elemets in array: "))
array = []
for i in range(num):
    array.append(int(input(f"enter the {i+1} element: ")))
    
summ = int(input("enter the required sum: "))
for i in range(num):
    for j in range(i+1,num):
        if array[i]+array[j]==summ:
            print(f"array[{i}]: {array[i]} and array[{j}]: {array[j]} makes the sum : {summ}")

        
