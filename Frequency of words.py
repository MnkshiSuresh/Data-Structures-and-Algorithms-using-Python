'''write python program to find frequency if letters apppearing in a string'''

def frequency(s1):
    
    unique = s1.split(" ")
    unique_words = set(unique)
    print("Unique words:", unique_words)
    
    
    for word in unique_words:
        count = 0
        for words in unique:
            if words == word:
                count += 1
        print(f"Letter '{word}' occurs {count} times.")

s1 = "loves many flowers but flowers are colourful"
frequency(s1)
