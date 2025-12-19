print("Sinh vien : Ho Sy Nghia")
print("Ma so sv  :040206022078")
print("##############################")

# This function adds two numbers
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtracts(x, y):
    return x - y
# This function multiplies two numbers
def multiplies(x, y):
    return x * y
# This function divides two numbers
def divides(x, y):
    return x / y
print("Select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",Divide(num1,num2))
else:
    print("Invalid input")
