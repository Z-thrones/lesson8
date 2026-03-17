mark1 = int(input("Enter a mark "))
mark2 = int(input("Enter another mark "))
mark3 = int(input("Enter another mark "))
mark4 = int(input("Enter another mark "))
mark5 = int(input("Enter the final mark "))
tot = mark1 + mark2 + mark3 + mark4 + mark5
ave = tot/5
if ave >= 91 and ave <= 100:
    print("Grade A1")
elif ave >= 81 and ave < 91:
    print("Grade A2")
elif ave >= 71 and ave < 81:
    print("Grade B1")
elif ave >= 61 and ave < 71:
    print("Grade B2")
elif ave >= 51 and ave < 61:
    print("Grade C1")
elif ave >= 41 and ave < 51:
    print("Grade C2")
elif ave >= 33 and ave < 41:
    print("Grade D")
elif ave >= 21 and ave < 33:
    print("Grade E1")
elif ave >= 0 and ave < 21:
    print("Grade E2")
else:
    print("INVALID INPUT!")