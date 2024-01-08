import random


class Hangman:

    def __init__(self,attempts):

        self.ListOfWords=[]
        self.wordlist=[]
        self.guesslist=[]
        self.FullGuessAttmpt=[]
        self.attempts=attempts
        self.ifWinner=0


    def getWord(self,genre):
        if genre==1:
            fileName="listOfMusicWords.txt"
        elif genre==2:
            fileName=("listOfSportTeams.txt")
        elif genre==3:
            fileName=("listOfMovieTitles.txt")
        elif genre==4:
            fileName=("Geography.txt")
        elif genre==5: 
            fileName=("words.txt")


        self.WordFile=open(fileName,"r")
        Words=self.WordFile.readlines()
        self.Words=Words
        for WordWithN in self.Words:
            self.WordWithN=str(WordWithN)
            self.WordWithoutN=self.WordWithN.rstrip("\n")
            self.WordWithoutN=self.WordWithoutN.lower()
            self.ListOfWords.append(self.WordWithoutN)
        self.Word=self.ListOfWords[random.randint(0,len(self.ListOfWords)-1)]
        self.WordFile.close()
        return self.Word
    def makeWordList(self,Word):
        self.Word=Word
        for Characers in self.Word:
            self.wordlist.append(Characers)
        return self.wordlist


    def makeGuessList(self,WordToGuess):
        self.WordToGuess=WordToGuess
        for i in range(len(self.WordToGuess)):
            if self.WordToGuess[i]==" ":
                self.guesslist.append(" ")
            elif self.WordToGuess[i]=="-":
                self.guesslist.append("-")
            elif self.WordToGuess[i]=="'":
                self.guesslist.append("_'_")
            elif (self.WordToGuess[i]).isnumeric():
                self.guesslist.append(self.WordToGuess[i])
            else:    
                self.guesslist.append("_")
        return self.guesslist
    
    def gameTracker(self,GuessList,Word,hangman):
        self.Word=Word
        self.GuessList=GuessList
        self.PreviousGuesses=[]
        DisplayWord="".join(self.GuessList)
        print("\n"+"\n"+"The goal of the game is to guess the word correctly"+"\n"+"Rules "+"\n"+"You only get 7 tries."+"\n"+"The words DO NOT USE Numbers"+"\n"+"AND! The most important rule! Have fun!")
        print("\n"+"\n"+"The word is "+ str(len(self.GuessList))+" letters long." +"\n"+str(self.GuessList))
        while self.attempts>=7 or -1:
            self.askingIfGuess=input("\n"+"Do you want to guess the word(1) or a letter(2)? Press Q to quit: ")
            self.askingIfGuess=self.askingIfGuess.lower()
            if self.askingIfGuess=="q":
                break
            elif self.askingIfGuess=="2":
                self.letterGuess=""
                while len(self.letterGuess) != 1:
                    self.letterGuess=input("\n"+"What is your guess(letter)?: ").lower()
                try:
                    self.PreviousGuesses.index(self.letterGuess)
                    self.attempts+=1
                    self.PreviousGuesses.append(self.letterGuess)
                    print("\n"+"You've already guessed the letter: "+ str(self.letterGuess))
                except ValueError:
                    self.PreviousGuesses.append(self.letterGuess)
                    self.ifWinner,self.attempts,self.GuessList=hangman.tryGuess(self.GuessList,self.letterGuess,self.WordToGuess,self.Word)
                if self.attempts !=-1:
                    print("\n"+"\n"+"The word is "+ str(len(self.GuessList))+" letters long." +"\n"+str(self.GuessList))
                    print("previous guesses "+str(self.PreviousGuesses))
                    print("you have "+ str(7-self.attempts)+ " left!"+"\n"+"\n")
            elif self.askingIfGuess=="1":
                FullGuessAttmpt=input("What is your guess(word)?").lower()
                self.PreviousGuesses.append(FullGuessAttmpt)
                self.ifWinner,self.attempts=hangman.TryFullGuessAttempt(FullGuessAttmpt,self.Word)

                if self.attempts !=-1:
                    print("\n"+"\n"+"The word is "+ str(len(self.GuessList))+" letters long." +"\n"+str(self.GuessList))
                    print("previous guesses "+str(self.PreviousGuesses))
                    print("you have "+ str(7-self.attempts)+ " left!"+"\n"+"\n")
            else:
                print("Please only type 1 or 2... ")
            if self.ifWinner==-1:
                print("\n"+"\n"+"You're right the word was "+str(self.Word))
                print("\n"+"You win!"+"\n")
                print("You had "+str(7-self.attempts)+" left!"+"\n"+"\n")
                break
            if self.attempts==7:
                print("\n"+"\n"+"You suck...The word was "+str(self.Word)+"\n"+"\n")
                break


    def tryGuess(self,GuessList,letterGuess,WordToGuess,Word):
        Temp=0
        letterCount=0
        self.WordToGuess=WordToGuess
        self.Word=Word
        self.letterGuess=letterGuess
        self.GuessList=GuessList

        for i in range(len(self.GuessList)):

            if self.letterGuess== self.WordToGuess[i]:
                self.GuessList[i]=self.letterGuess
                Temp+=1
                letterCount+=1
                if self.GuessList==self.WordToGuess:
                    return -1,self.attempts , self.WordToGuess
        if letterCount==0:
            self.attempts+=1
            print("There are zero "+str(letterGuess)+"'s")
            return 0,self.attempts , self.GuessList
        if letterCount==1:
            print("There is "+str(letterCount)+" "+ str(letterGuess))
            return 0,self.attempts,self.GuessList
        else:
            print("There are "+str(letterCount)+" "+ str(self.letterGuess)+"'s")
            return 0,self.attempts,self.GuessList

    def TryFullGuessAttempt(self,FullGuessAttmpt,Word):
        self.FullGuessAttmpt=FullGuessAttmpt
        self.Word=Word
        if self.FullGuessAttmpt==self.Word:
            # print("winner")
            return -1,self.attempts
        else:
            self.attempts+=1
            return 1,self.attempts
    
    def getGameGenre(self):
        while True:
            self.Genre = input("what genre would you like? "+"\n"+\
            "(1)Music Artists (2)Sports teams (3)Movies Titles (4)Geography (5)Random: ")
            try:
                self.Genre=int(self.Genre)
                if  5>=self.Genre>0:
                    return self.Genre
                else:
                    print("Please use only a number in range 1-5")
            except ValueError:
                print("Use only a numbers from the list")

    

def main():
    attempts=0
    hangman=Hangman(attempts)  #returns the word as a list
    genre=hangman.getGameGenre()
    Word=hangman.getWord(genre)
    WordToGuess=hangman.makeWordList(Word)
    GuessList=hangman.makeGuessList(WordToGuess)
    print(Word)
    hangman.gameTracker(GuessList,Word,hangman)
if __name__=="__main__":
    main()
