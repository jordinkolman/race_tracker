#Purpose: Track dummy race times and determine winner
#Author: Jordin Kolman
#Date: 08/07/2022

#set up lists and variables
chevyTimes = [0.0] * 8
fordTimes = [0.0] * 8
chevyWins = 0
fordWins = 0

#get Chevy Times
counter = 1
print("---Input Chevy Times---")
for i in range(8):
    chevyTimes[i] = float(input("Enter time for Chevy Car " + str(counter) + ": "))
    counter = counter + 1

#get Ford Times
counter = 1
print("---Input Ford Times---")
for i in range(8):
    fordTimes[i] = float(input("Enter time for Ford Car " + str(counter) + ": "))
    counter = counter + 1

#determine and display winners for each pair
print ("And the winners are: ")
for i in range(8):
    if chevyTimes[i] < fordTimes[i]:
        print ("Chevy by", round(fordTimes[i] - chevyTimes[i],2), "sec")
        chevyWins = chevyWins + 1
    elif fordTimes[i] < chevyTimes[i]:
        print("Ford by", round(chevyTimes[i] - fordTimes[i], 2), "sec")
        fordWins = fordWins + 1
    else:
        print("Tie!")

#determine and display overall winner
if chevyWins > fordWins:
    print("And the winning team is: C H E V Y !")
elif chevyWins < fordWins:
    print("And the winner is: F O R D !")
else:
    print("It's a T I E !")

    