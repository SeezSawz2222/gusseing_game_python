import random as rd
def com_guess(low, high, randnum,count=0):

    guess = low + (high - low) // 2
    if guess == randnum:
        return count
        
    elif guess>randnum:
        count = count + 1
        return com_guess(low,guess-1,randnum,count)
    else:
        count = count + 1
        return com_guess(guess+1, high, randnum,count)

randnum = rd.randint(1,101)
count = 0
guess = -99
while(guess != randnum):

    guess = (int)(input("Enter your guess between 1 to 100: "))
    if guess < randnum:
        print("HIGHER!!")
    elif guess > randnum:
        print("LOWER!!")
    else:
        print("YOU GUESSED IT!!!!")
        break
    count = count + 1
print("You took " + str(count)+" steps to guess the rumber right!")
print("Computer took " + str(com_guess(0,100,randnum))+" steps to guess the rumber right!")