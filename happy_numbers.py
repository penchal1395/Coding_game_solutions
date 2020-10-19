"""
Input
Line 1: An integer N for the number of numbers to test.
Following N Lines: Each line has a positive integer you should test whether it is happy or not.

Be aware that some input numbers are really BIG, much bigger than your Integer type can handle. Find a way to overcome it.
Output
Output N lines.
Following the same order as inputs, each line starts with a given number from the list, a space, and then an ascii art :) or :( to indicate this number is happy or unhappy.
Constraints
1 ≤ N ≤ 100
0 < each number ≤ 10^26
Example
Input
2
23
24
Output
23 :)
24 :(

"""
"""
Input
Line 1: An integer N for the number of numbers to test.
Following N Lines: Each line has a positive integer you should test whether it is happy or not.

Be aware that some input numbers are really BIG, much bigger than your Integer type can handle. Find a way to overcome it.
Output
Output N lines.
Following the same order as inputs, each line starts with a given number from the list, a space, and then an ascii art :) or :( to indicate this number is happy or unhappy.
Constraints
1 ≤ N ≤ 100
0 < each number ≤ 10^26
Example
Input
2
23
24
Output
23 :)
24 :(

"""
def number_square(number):
    sum = 0
    while number > 0:
        k = number%10
        sum +=k**2
        number = number//10
    return sum


number_of_inputs = int(input())
l = [int(input()) for i in range(number_of_inputs)]
for i in l:
    print(i,end=" ")
    while i>9:
        i = number_square(i)
    if i==1 or i==7:
        print(":)")
    else:
        print(":(")

    
    


    

