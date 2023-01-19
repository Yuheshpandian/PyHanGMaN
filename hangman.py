'''|   |   /\    |\  |    /---      |\  /|   /\   |\  |
   |---|  /--\   | \ |   |     __   | \/ |  /--\  | \ |   
   |   | /    \  |  \|    \___|  |  |    | /    \ |  \|
   
'''


#importing libraries that are required
from hangman_pic import print_hangman as p_h
from words import word_list
import random as rd

#string for verification of input
ab="abcdefghijklmnopqrstuvwxyz"

p_h=p_h()

#returns a random eng word from words module
def get_word():
    x=rd.choice(word_list)
    return x
#necessary for ending the loop
go=False

word_said=[]    

word=get_word() 
#our word field
pattern=["_"]*len(word)
   
    
      
chances=0
#Loop begins
while True:
    print("\n HanG MaN")
    print("\n\n")
    print("tries left: "+str(7-chances)," \n")
    #prints the hangman
    if chances>0:
        print(p_h[chances-1])
    print("word: \n"+str(pattern),"\n")
    guess=input("Guess an alphabet that you think it would be in the word: ").lower()
   
    if guess in word and guess not in word_said :
         print(" \nYou Got It Correct ^_^")
         for i,e in enumerate(word):
             if guess==e:
                 pattern[i]=guess  
    elif guess in word_said:
        print("\nalready said the alphabet")   
    elif guess not in ab:
        print(" \ninvalid guess,enter a alphabet")
        continue
    else:
        print("\nNope,wrong one ('-')")
        chances+=1
    word_said.append(guess)   
    #declaration of win
    if "_" not in pattern and chances<=7:
        print("\n")
        print(pattern)
        print("\nYou Won,^__^")
        go=True
    elif chances==7:
        print("\nYOU LoST •_•")
        go=True
        print("/nthe word is: "+word)
    
    if go:
        z=input(" do you want to play again(yes/no): ").lower()
        if z=="yes":
            go=False
            word=get_word()
            chances=0
            pattern=["_"]*len(word)
            word_said=[]
            continue
        elif z=="no":
            print("\nTHANK YOU")
            break
     #Thank you   
