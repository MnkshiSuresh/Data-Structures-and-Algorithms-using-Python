'''You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .

Return true if the given string 'S' is balanced, else return false.'''

def isValidParenthesis(s: str) -> bool:
    array = list(s)
    i = 0
    while i < len(array):
        if array[i] == '{':
            found = False
            for j in range(i + 1, len(array)):
                if array[j] == '}':
                    del array[j]
                    del array[i]
                    i = max(i - 1, 0)
                    found = True
                    break
            if not found:
                return False
                
        elif array[i] == '(':
            found = False
            for j in range(i + 1, len(array)):
                if array[j] == ')':
                    del array[j]
                    del array[i]
                    i = max(i - 1, 0)
                    found = True
                    break
            if not found:
                return False

        elif array[i] == '[':
            found = False
            for j in range(i + 1, len(array)):
                if array[j] == ']':
                    del array[j]
                    del array[i]
                    i = max(i - 1, 0)
                    found = True
                    break
            if not found:
                return False
                
        else:
            i += 1

    return len(array) == 0

pass
