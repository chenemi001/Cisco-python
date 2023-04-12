# guessing game
score = 0
print("HELLO!", "WELCOME TO MY GUESSING GAME", ",", "HAVE FUN!")
a = str(input("ENTER NAME:"))
print("WELCOME!", a)
a1 = "break"
print("THIS IS LEVEL 1")
p = str(input("ALL RELATIONSHIPS?:"))
for x in range(2):
    if p != a1:
        print("*TRY AGAIN*")
        p = str(input("ALL RELATIONSHIPS?  :"))
if p != a1:
    print("OOPS!", "GAME OVER!", a)
if p == a1:
    score += 5
    print("CONGRATULATIONS!\n", "YOU'VE EARNED:", score, "points")
    print("WELCOME TO LEVEL 2")
    a2 = "father"
    c = str(input('THE HEAD OF THE HOUSE IS CALLED?:'))
    for x in range(2):
        if c != a2:
            print("*TRY AGAIN*")
            c = str(input('THE HEAD OF THE HOUSE IS CALLED?:'))
    if c != a2:
        print("OOPS!", "GAME OVER!", a)
    if c == a2:
        score += 5
        print("CONGRATULATIONS!\n", "YOU'VE EARNED:", score, "points")
        print("WELCOME TO LEVEL 3 EXPERT", a)
        a3 = "peter obi"
        g = str(input("WHO IS THE BEST PRESIDENT OF NIGERIA?:"))
        for x in range(2):
            if g != a3:
                print("*TRY AGAIN*")
                g = str(input("WHO IS THE BEST PRESIDENT OF NIGERIA?:"))
        if g != a3:
                print("OOPS!", "GAME OVER!", a)
        if g == a3:
            score += 5
            print("CONGRATULATIONS!\n", "YOU'VE EARNED:", score, "points")
            print("GOOD JOB!!!!")
z = score + score + score
print('TOTAL SCORE:', z, "points")

