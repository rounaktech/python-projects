import random

def game():
    Highscore = 0
    print("Guess The Value | 0 or 1")
    for x in range(0,100):
        ans = int(input())
        r = random.randrange(0,2)
        if(ans == r):
            Highscore+=1
            print("Computer", r, "Your answer", ans)
        else:
            print("Gameover")
            return Highscore
        

hs = game()
f = open("highscore.txt", "r")
prev = f.read()

f.close()
if(hs>int(prev)):
    f = open("highscore.txt","w")
    f.write(str(hs))
    print("New High Score", hs)
else:
    print("Old High Score", prev)



