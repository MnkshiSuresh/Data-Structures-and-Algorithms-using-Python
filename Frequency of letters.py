'''write python program to find frequency if letters apppearing in a string'''

def frequency(s1):
    
    unique_letters = set(s1)
    print("Unique letters:", unique_letters)
    
    
    for letter in unique_letters:
        count = 0
        for char in s1:
            if char == letter:
                count += 1
        print(f"Letter '{letter}' occurs {count} times.")

s1 = "loves many flowers but flowers are colourful"
frequency(s1)
