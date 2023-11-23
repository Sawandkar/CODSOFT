print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
operation = input()
if operation == "1":
    num1 = input("Enter First Number:")
    num2 = input("Enter Second Number:")
    print("The Sum of Two number is:"+ str(int(num1)+int(num2)))
elif operation == "2":
    num1 = input("Enter First Number:")
    num2 = input("Enter Second Number:")
    print("The Subtraction of Two number is:"+str(int(num1)-int(num2)))
elif operation == "3":
    num1 = input("Enter First number:")
    num2 = input("Enter Second number:")
    print("The Multiplication of Two number:"+str(int(num1)*int(num2)))
elif operation == "4":
    num1 = input("Enter FIrst Number:")
    num2 = input("Enter Second Number:")
    print("The Division of Two number:"+ str(int(num1)/int(num2)))
else:
    print("Invalid Entry")
