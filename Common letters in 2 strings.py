      '''write python program to find common letters between two strings'''

def common_letters(a,b):  
    s1=set(a)
    s2=set(b)
    print("deleting duplicates: s1= ",s1)
    print("deleting duplicates: s2= ",s2)
    lst=s1 & s2
    print(lst)
    
    
    
    
a=input("enter the string 1: ")  
b=input("enter the string 2: ")
common_letters(a,b)
