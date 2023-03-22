num=int(input("Enter a number:"))
x=1
y=1
fib_list=[0,1,1]

while x<=1000:
    x=x+y
    y=x+y
    fib_list.append(x)
    fib_list.append(y)

while True:
    if num in fib_list:
        print("This is a Fibonacci number!")
    else:
        print("This is not a Fibonacci number :/")
    again=input("Do you want to try again?")
    if again == "yes":
        num=int(input("Enter a number:"))
    else:
        break

print(fib_list)
