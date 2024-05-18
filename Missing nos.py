''' find missing number in an array'''

num = input("enter list of numbers with a space gap: ")
n = []
for k in num :
    if k.isdigit():
        n.append(int(k))

l = len(n)

for i in range(1,l+1):
    if i not in n:
        print(f"{i} is not present in the list")
    
        
