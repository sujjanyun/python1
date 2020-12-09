count = 0
user_input = input("How high should we count? ")

try: 
    MAX = int(user_input)
    while(count < MAX):
        print(count)
        # the following line means, "add 1 to the value of count"
        count += 1
except ValueError:
    # the following line is the exception message
    print("Please run the program again, this time with a number")

