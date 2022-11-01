def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1) 

def fibonacci_series(n):
    #0 1 2 3 4 5 6 7  8
    #0 1 1 2 3 5 8 13 21
    if n == 0 or n == 1:
        return n
    return fibonacci_series(n-1)+fibonacci_series(n-2)

def find_list_sum(inp_list):#[1, 2, [3,4], [5,6]]
    total = 0
    for element in inp_list:
        if isinstance(element,int):
            total += element
        else:
            total += find_list_sum(element)
    return total

def find_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * find_factorial(n-1)

def sumDigits(n):
    #First step is to separate the values so that I can loop through and add
    #Even if I go for recursion I have to go one by one digit
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(n//10)
    '''
    for i in str(n):
        tot += int(i)
    return tot'''

def sum_series(n):
    if n <= 0:
        return 0
    return n + sum_series(n-2) 

def harmonic_sum(n):
    y = n
    tot = float(0)
    if y <= n-1:
        return 0
    tot += harmonic_sum(y/(n+1))  #1/2,1/3....1/12
    return tot+n

def power(a,b):
    result = 1
    if b== 0:
        return 1
    else:
        #result = result*a 
        result = a * power(a,b-1)
    return result

def find_gcd(num1,num2):
    pass
    '''
    result = 1
    for i in range(b):
        result = result*a
    return result'''

if __name__ == "__main__":
    '''
    val = find_sum(5) #1+2+3+4+5 1+3+6+10+15 == 
    print(val)

    val2 = fibonacci_series(6)
    print(val2)

    list_ex = [1, 2, [3,4], [5,6]]
    print(find_list_sum(list_ex))

    factorial = find_factorial(5)
    print('factorial is ',factorial)

    print(sumDigits(451569))'''
    #print(sum_series(6))
    #print(harmonic_sum(1))

    #print(power(3,5))

    num1 = 54 
    num2 = 24

    if num1 < num2:
        smallest = num1
        largest = num2
    else:
        smallest = num2
        largest = num1

    for i in range(1,smallest):
        if smallest%i == 0 and largest%i == 0:
            gcd_result = i

    print('The GCD result is ',gcd_result)

    for i in range(1,smallest):
        if smallest%i == 0 and largest%i == 0:
            gcd = i
            small_rem = int(smallest/i)
            large_rem = int(largest/i)
    lcm_result = gcd*small_rem*large_rem
    print('The LCM result is ',lcm_result)

'''
1. Write a Python program to calculate the sum of a list of numbers. Go to the editor
Click me to see the sample solution

2. Write a Python program to converting an Integer to a string in any base. Go to the editor
Click me to see the sample solution

3. Write a Python program of recursion list sum. Go to the editor
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
Click me to see the sample solution

4. Write a Python program to get the factorial of a non-negative integer. Go to the editor
Click me to see the sample solution

5. Write a Python program to solve the Fibonacci sequence using recursion. Go to the editor
Click me to see the sample solution
'''