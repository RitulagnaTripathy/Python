#Implementation of Hangman game
import random

score=10
ans=[]
guess=''
c=0

name=input("What's ur name?")
print("Hey"+name,",Let's play Hangman!!")
#List of movies 
movie_list=['LAGAAN','HIGHWAY','THOR','DANGAL','NEWTON']
movie=random.choice(movie_list)
a=len(movie) #no of letters in movie
ans.extend(movie)
for i in range(a):
    ans[i]= '*'
print(ans)
#initial score=10
print("score=10")
while (score>0):
    #to input the guessed letter
    print("Guess a Letter")
    guess=input()
    if guess in movie: #to check whether the guessed letter is correct or not
       for i in range(a):
            if guess in ans[i]:
                print("U have already guessed it!")
                break
            if movie[i]==guess:
                ans[i]=guess
                c+=1
                print(ans)
                print("Correct Guess!")
                #3 points will be awarded for correct guess
                score+=3
                print(score) #to print score
                
    if guess not in movie:
        print("Ooops! Wrong Guess")
        #2 points will be deducted for wrong guess
        score-=2
        print(score)#to print score
    if c==a:
        break

for i in range(a): #declaration of final result
    if ans[i]==movie[i]:
        print("Congrats..You Won!!")
        break
    else:
        print("You Lose!")
        print("Better luck next time")
        break
        
    


    
        
        
            
            


