############################
import random;

############################
#   Variables declaration  #  
############################
error = 0;
word0 = 'Binary';
word1 = 'Fire';
word2 = 'Air';
word3 = 'Computer';
guess = '';
rightWord = [];


###################################
#  Random number to chose a word  #
###################################
a = random.randint(0, 3)

if(a == 0) :
    chosenWord = word0;
elif(a == 1) :
    chosenWord = word1;
elif(a == 2) :
    chosenWord = word2;
elif(a == 3) :
    chosenWord = word3;
    
###################################
#        Doll construction        #
###################################
def hanged(error) :
    if error == 1 :        
        print 'Wrong guess';
        print '________      ';
        print '|      |      ';
        print '|      @      ';
        print '|             ';
        print '|             ';
        print '|             ';

    elif error == 2 :        
        print 'Wrong guess';
        print '________      ';
        print '|      |      ';
        print '|      @      ';
        print '|      |      ';
        print '|             ';
        print '|             ';   

    elif error == 3 :        
        print 'Wrong guess';
        print '________      ';
        print '|      |      ';
        print '|      @      ';
        print '|     /|      ';
        print '|             ';
        print '|             ';

    elif error == 4 :        
        print 'Wrong guess';
        print '________      ';
        print '|      |      ';
        print '|      @      ';
        print '|     /|\     ';
        print '|             ';
        print '|             ';

    elif error == 5 :        
        print 'Wrong guess';
        print '________      ';
        print '|      |      ';
        print '|      @      ';
        print '|     /|\     ';
        print '|     /       ';
        print '|             ';


    elif error == 6 :        
        print 'Wrong guess';
        print '________      ';
        print '|      |      ';
        print '|      @      ';
        print '|     /|\     ';
        print '|     / \     ';
        print '|             ';
        print 'Game Over.';
        
###############################################################################
#                   User input and character ArithmeticError                  #
###############################################################################
leng = len(chosenWord);
for i in range(0, leng) :
    rightWord.append(i);
    rightWord[i] = 'x';
print 'Welcome to the Python Hangman Game. Your word has ', leng, ' letters.';    
print 'You have 6 guesses, good luck';
while error < 6:
    guess = raw_input('Enter a word: ');
    if guess in chosenWord :
        print 'Correct';        
        tst = [pos for pos, char in enumerate(chosenWord) if char == guess];        
        for i in range(0, leng) :            
            if i in tst :
                rightWord[i] = guess;
            elif not rightWord[i] in chosenWord :
                rightWord[i] = 'x';            
            print (rightWord[i]);
    else :
        error += 1;
        hanged(error);
###############################################################################

