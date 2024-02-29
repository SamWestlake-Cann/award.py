"""
Start
ask user for swim time
confirm time completed in mins
ask user for cycle time 
confirm time completed in mins
ask user for run time
confirm time completed in mins
add swim, cycle + run together
confirm total time in mins
return their reward
End
"""

swim = int(input("In minutes how fast did you complete the swim? ")) #store as integer time for swim
print("You completed the swim in " + str(swim) + " minutes\n") #print response followed by minutes

cycle = int(input("In minutes how fast did you complete the cycle? ")) #store as integer time for cycle
print("You completed the cycle in " + str(cycle) + " minutes\n") #print response followed by minutes

run = int(input("In miutes how fast did you complete the run? ")) #store as integer time for run
print("You completed the run in " + str(run) + " minutes\n") #print response followed by minutes

total_time = swim + cycle + run #store time of all added together as total_time

print("The total time for your triathlon is " + str(total_time) + " minutes\n") #print respose as total_time in minutes


if total_time <= 100: #if total_time <= 100 print below
    print("Congratulations, you have been awarded your Provincial Colours\n")

elif total_time <= 105: #if total_time <= 105 print below
    print("Well done Provincial Half Colours\n")

elif total_time <= 110: #if total_time <= 110 print below
    print("Keep it up Provicial Scroll for you\n")

else: #if anything else print below
    print("Sorry you didn't gain an award this time, keep up the hard work you will get it next time\n")

"""
0 - 100 Provincial colours
101 - 105 Provincial Half colours
106 - 110 Provicial Scrol
111 + No award
"""