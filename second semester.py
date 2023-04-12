# welcome to my application
password = "veritas"
d = str(input("ENTER PASSWORD:"))
for x in range(0,4):
    if d != "veritas":
        print("try again")
        d = str(input("ENTER PASSWORD:"))
if d == "veritas":
    p = str(input("ENTER NAME:"))
    y = int(input("ENTER LEVEL:"))
    c = str(input("ENTER YOUR GOAL THIS SEMESTER:"))
    print("congratulations", p, "you're in", y, "level")
    print("THIS IS YOUR GOAL:", c)
else:
    print("ERROR!")











