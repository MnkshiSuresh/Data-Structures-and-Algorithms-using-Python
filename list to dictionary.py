'''convert 2 lists into dictionary'''

s1=input("enter the first list with a space gap: ")
s2=input("enter the second list with a space gap")

list1=s1.split()
list2=s2.split()

if len(list1) != len(list2):
    print("Error: Lists must be of equal length.")
else:
    dictn = dict(zip(list1, list2))
    print(dictn)
        
