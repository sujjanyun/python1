day = int(input("Day (0-6)? "))

if day == 0 or day == 6:
    print("SLEEP SLEEP")
elif 0 < day < 6:
    print("GO GET DAT BREAD")
else:
    print("THAT AIN'T WHAT I SAID")


day = int(input("Day (0-6)? "))

sleep = False

if day == 0 or day == 6:
    sleep = True

if sleep:
    print("OKIE DOKE YO")
else:
    print("GO GET DAT BREAD")