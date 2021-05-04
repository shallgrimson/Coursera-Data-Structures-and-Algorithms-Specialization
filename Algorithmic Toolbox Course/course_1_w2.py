'''
I think these need to be adjusted to take console input
'''

'''
Problem 1 - Fibonacci sequence
'''
#can just store n1 and n2 in variables rather than using an array
def fibonacci_sequence(num):
    seq = []
    seq.append(0)
    seq.append(1)
    for i in range(2, num+1):
        seq.append(seq[i-1] + seq[i-2])

    return seq[num]

'''
Problem 2 - Return last digit of Fibonacci number
'''
#Here just the lastest digit of the Fibonacci number is retured, a array is not used to hold the number
def fib_sequence_get_final_digit(num):
    n1 = 0
    n2 = 1

    if num == 0:
        return n1

    for i in range(2, num+1):
        nbuff = n2
        n2 = (n1 + n2)%10
        n1 = nbuff

    return n2

'''
Problem 3 - Euclidean algorithm to find GCD of two numbers
'''
#n1 is the greater digit
def GCD_Euclidean(n1, n2):
    if n2 > n1:
        n1, n2 = n2, n1 

    if n2 == 0:
        return n1
    
    while n2 > 0:
        #div = int(n1/n2)
        rem = n1%n2
        n1 = n2
        n2 = rem 

    return n1
    
'''
Problem 4 - Least Common Multiple
'''
def LCM(n1, n2):
    gcf = GCD_Euclidean(n1,n2) #find greatest common factor
    return n1/gcf*n2

'''
Problem 5 - Fibonacci Numbers but find mod of each number - Pisano period
THIS CAN BE CHANGED TO MAKE USE OF THE Pisano period TO SPEED IT UP - REFER TO PROBLEM 5
'''
#grab Pisano period for a certain mod and then relate it to the number
def find_pisano_period(mod):
    n1, n2 = 0, 1
    mod_n1, mod_n2 = 0, 1
    mod_seq = []

    for i in range(0, mod*mod):
        mod_seq.append(mod_n1)

        nbuff = n2
        n2 = (n1 + n2)
        n1 = nbuff

        mod_n1 = n1%mod
        mod_n2 = n2%mod

        if mod_n1 == 0 and mod_n2 == 1:
            return mod_seq

'''
Find the mod value for a specific num - space could be reduced by not passing mod_seq
'''
def fib_mod(num, mod):
    mod_seq = find_pisano_period(mod)
    # print(num%len(mod_seq)-1)
    # print(mod_seq[num%len(mod_seq)])

    return mod_seq[num%len(mod_seq)]


'''
Problem 7 - Find last digit of the sum of fib numebrs
THIS CAN BE CAHNGED TO MAKE USE OF THE Pisano period TO SPEED IT UP - REFER TO PROBLEM 5
'''
def fib_sequence_get_final_digit(low, high):
    n1, n2 = 0, 1 
    sum = 0
    
    if high < low: #swap fib numbers so fnb is always bigger
        high, low = low, high 

    if low < 2: #this is to account for if low is less than 2, n1 is never added to sum and n2 is never the fib nums of 1 and 0
        sum = sum + 1

    for i in range(2, high+1):
        nbuff = n2
        n2 = n1 + n2
        n1 = nbuff

        if i >= low:
            sum = sum + n2

    return sum%10

'''
Problem 8  - Last Digit of the Sum of Squares of Fibonacci Numbers
'''
def fib_sum_of_squares(num):
    #make use of the tiles property: Length = Fn, and width = Fn + (Fn-1)
    #and the Pisano period to do this, only need last digits to find last digit of area
    mod_seq = find_pisano_period(10)
    f1 = mod_seq[num%len(mod_seq)]
    f0 = mod_seq[(num-1)%len(mod_seq)]

    return (f1*(f1+f0))%10


if __name__ == "__main__":
    print(fib_sum_of_squares(12345789))
