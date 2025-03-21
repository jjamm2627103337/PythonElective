age = int(input("Enter age: "))

try:
    if(age<18):
        raise ValueError
    else:
        print("Hello")
except ValueError:
    print("Age is less than 18")