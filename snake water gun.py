import random
lst=['s','w','g']
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you=='s':
            return True
        
    elif comp == 'g':
        if you == 's':
            return False
        elif you=='w':
            return True

print("com turn :snake(s) wate(w) gun(g) ? ")
comp= random.choice(lst)



you=input(" your turn :snake(s) wate(w) gun(g) ? ")   
a= gamewin (comp,you)  


print(f' computer chose {comp}')
print(f' you chose {you}')

if a==None:
    print( " the game is tie !")
elif a:
    print(" you win")
else :
    print( "you lose" )




            
