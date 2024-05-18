'''count the frequency of numbers inn the string'''

def count_nos(s1):
    s1=str(s1)
    
    numbers=[]
    for char in s1:
        if char.isdigit():
            numbers.append(char)
    
    a=set(numbers)
    print("unique nos present are: ",a)
    for n in a:
        cnt=numbers.count(n)
        print(f"frequency of {n} is {cnt}")
        
s1=12341235662
count_nos(s1)
