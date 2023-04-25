def factorial(x):
    global i
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

odd = int(input("odd number:\n"))

sum = 0
for i in range(1, odd+1):
    if(i%2 != 0):
        division = factorial(i)/factorial(i+1)
        sum += division
        
print(sum)