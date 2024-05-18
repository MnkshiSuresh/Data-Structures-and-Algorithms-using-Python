'''Problem Statement
Ravi learned about various kinds of numbers when he came across a special type called the Filo Numbers.
A Filo Number is any number that can be expressed as a sum of consecutive natural numbers.
As he studied more, he became more interested after knowing that every positive integer can be expressed as a Filo Number.
However, after thinking for a while, he thought that a positive integer could be expressed as a Filo Number in more than one way, and later,
he got confused about how he could calculate those ways.
Given a positive integer, determine the number of ways in which it can be expressed as a Filo Number.
Input Format
* Given n, a positive integer.
Output Format
Print the number of ways n can be expressed as a Filo Number.  
sample test case:-  input:9  output:3 '''
------------------------

ans 1:
def filo(n):
    count = 0
    k = 1
    
    while k * (k - 1) // 2 < n:
        if (n - k * (k - 1) // 2) % k == 0:
            count += 1
        k += 1

    print(count)

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    filo(n)

if __name__ == "__main__":
    main()


ans 2:def filo(n):
    count = 0

    # Iterate over possible starting points of the sequence
    for i in range(1, n + 1):
        summ = 0
        # Sum consecutive numbers starting from i
        for j in range(i, n + 1):
            summ += j
            # If the sum equals n, we found a valid sequence
            if summ == n:
                count += 1
                break
            # If the sum exceeds n, no need to continue further for this starting point
            elif summ > n:
                break

    print(count)

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())  # Read and convert the input to an integer
    filo(n)

if __name__ == "__main__":
    main()


'''ans1 got all testcases correct'''
