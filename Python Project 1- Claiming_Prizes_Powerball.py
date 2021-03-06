/*/In this project, the grand prize (in dollars) and the winning numbers are given. The program reads multiple tickets 
   (6 selected numbers in each ticket) from the user.  For each ticket, the program calculates its prize won, and outputs 
   the prize (in dollars) to the user.
   Game rules:
   In each game, players select 5 numbers from a set of 69 white balls (numbered 1 to 69) and one number from 26 red balls 
   (numbered 1 to 26).  The red ball number can be the same as one of the white balls, but a white ball can only be selected once.  
   The order of selection does not matter.  The numbers in each ticket is not guaranteed to be sorted in any way.

----------------------------------------------------------------------------------------------------------------------------------------
# 2 12 16 29 54 6
GRAND_PRIZE = "$242,000,000"
WHITE = [2, 12, 16, 29, 54]
RED = 6

z = []
while True:
    totalBalls = input("Enter 6 ball numbers:").split()
    for i in totalBalls:
        z.append(int(i))
    w = z[:-1]
    r = z[5]
    dupeCheck = len(w) == len(set(w))
    c = 0
    for x in w:
        if int(x) >= 1 and int(x) <= 69:
            c+= 1
    p = len(w) == c
    s = r >= 1 and r <= 26
    a_set = set(w)
    b_set = set(WHITE)

    q = len(a_set.intersection(b_set))
    matchRed = int(RED == r)
    if (len(totalBalls) == 6 and dupeCheck and p and s):
        if(matchRed == 1 and q == 0): print("$4")
        elif (matchRed == 1 and q == 1): print("$4")
        elif (matchRed == 1 and q == 2): print("$7")
        elif (matchRed == 0 and q == 3): print("$7")
        elif (matchRed == 1 and q == 3): print("$100")
        elif (matchRed == 0 and q == 4): print("$100")
        elif (matchRed == 1 and q == 4): print("$50,000")
        elif (matchRed == 0 and q == 5): print("$1,000,000")
        elif (matchRed == 1 and q == 5): print(GRAND_PRIZE)
        else: print("$0")        
        k = input("Do you want to play the game again? y/n ") 
        if k == "y":
            z.clear()
            continue
        else:
            print("Thanks for playing the game")
            break
    else:
        print("Sorry, your response was not loud enough.")
        continue          
     




        
    
    
