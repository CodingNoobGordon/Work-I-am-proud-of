'''
This program allows the user to enter any integer, before calculating the sum of the first n and first n odd integers, and finally printing the result.
The program additionally forces the user to enter a positive integer, and also allows a replay option.
'''

#Initiliaze variables.
end = False

#Function receives n integer.
def intput():
    while True:
        try:
            integer = int(input("Enter a positive integer: "))
            #If the integer is below zero, the loop resets.
            if integer < 0:
                print("That's not a positive integer!")
            else:
                return integer
        except:
            print("That's not a positive integer!")

#Function calculates the sum of the first n integers.
def firstInt(n):
    sum = 0
    for integer in range(n+1):
        sum += integer
    return sum

#Function calculates the sum of the first n odd integers.
def firstOddInt(n):
    sum = 0
    sum = n**2
    return sum


'''MAIN PROGRAM'''
#Output - Outputs the function's calculations
while end == False:
    #Resets the replay loop to false after each time.
    replayEnd = False
    #Utilizes functions and ouputs their results.
    n = intput()
    b = firstInt(n)
    c = firstOddInt(n)
    print("The sum of the first " + str(n) + " integers was " + str(b) + ", \n\
while the sum of the first " + str(n) + " odd integers was " + str(c))
    
    #Asks user if they want to replay the program, and loops until they respond.
    while replayEnd == False:
        replay = input("Would you like to run the program again?(YES/NO): ")
        #Replays if the user says yes.
        if replay == "YES":
            print("Good choice!")
            replayEnd = True
            end = False
        #Ends if the user says no.
        elif replay == "NO":
            print("Ending program...")
            replayEnd = True
            end = True
        else:
            print("Please answer with either 'YES' or 'NO'")
