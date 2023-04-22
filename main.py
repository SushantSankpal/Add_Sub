# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("********** Select the Operation from below ***********")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice= input("Please Select the Choice(1/2/3/4):")

num_1 = int(input("Please enter the first number:"))
num_2 = int(input("Please enter the second number:"))

if choice =='1':
    print(num_1,"+",num_2,"=",add(num_1, num_2))
elif choice=='2':
    print(num_1 + "-" + num_2 + "=" + sub(num_1, num_2))
elif choice=='3':
    print(num_1+"*"+num_2+"="+mul(num_1, num_2))
elif choice=='4':
    print(num_1 + "/" + num_2 + "=" + div(num_1, num_2))
else:
    print(choice+": This Option is invalid")
