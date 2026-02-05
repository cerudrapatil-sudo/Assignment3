def factorial(n):
    if n<0:
        print("Negative Numbers factorial not Countable")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
    
num=int(input("Enter a Number: "))
fact=factorial(num)
print(f"\nFactorial of {num} is: {fact}")