

print("=======================================")

_ =input("Lotfan yek adad beyn 1 ta 100 entekhab konid ...")

guess = 50
payin = 1
bala = 100
win = False 

while win == False:

    t = input("Aya adade shoma " + str(guess) + " ast? ")

    # B agar bishtar bsahe 
    if t == 'B':
        payin = guess
        guess = (guess+bala)//2
        
    # K agar kamtar bashe 
    elif t == "K":
        bala = guess
        guess = (guess+payin)//2
        
    # A agar hads dorost bashe
    elif t == "A":
        win = True
    else: 
        print("motavajeh nashodam!") 

print("=======================================")





print("=======================================")

_ =input("Lotfan yek adad beyn 1 ta 100 entekhab konid ...")

guess = 50
payin = 1
bala = 100


while True:

    t = input("Aya adade shoma " + str(guess) + " ast? ")

    # B agar bishtar bsahe 
    if t == 'B':
        payin = guess
        guess = (guess+bala)//2
        
    # K agar kamtar bashe 
    elif t == "K":
        bala = guess
        guess = (guess+payin)//2
        
    # A agar hads dorost bashe
    elif t == "A":
        break

    else: 
        print("motavajeh nashodam!") 

print("=======================================")