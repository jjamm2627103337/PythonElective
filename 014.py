largest = None
smallest = None

while(True):
    try:
        num = input("Enter number: ")

        if(num=="done"):
            break
        n = int(num)
        if(largest==None or n > largest):
            largest=n

        if(smallest==None or n<smallest):
            smallest=n
    except ValueError:
        print("Invalid input")

print("largest: ", largest)
print("smallest: ", smallest)

    