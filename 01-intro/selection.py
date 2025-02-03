
a = 0
a = int(input("Type your age: "))

if a >= 18:
    print("Go on")
else:
    print("Stop")


print("MENU")
print("1. Open File")
print("2. Save File")
print("3. Delete File")

sel = int(input("Select 1-3: "))

if sel == 1:
    print("File openned")
elif sel == 2:
    print("File saved")
elif sel == 3:
    print("File deleted")
else:
    print("Wrong choice")

match sel:
    case 1:
        print("File openned")
    case 2:
        print("File saved")
    case 3:
        print("File deleted")
    case _:
        print("Wrong choice")