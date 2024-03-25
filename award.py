"""
Start
ask user for swim_time
confirm time completed in mins
ask user for cycle_time 
confirm time completed in mins
ask user for run_time
confirm time completed in mins
add swim_time, cycle_time + run_time together
confirm total time in mins
return their reward
End
"""

# Changes to titles
swim_time = int(input("In minutes how fast did you complete the swim? ")) #store as integer time for swim
print("You completed the swim in " + str(swim_time) + " minutes\n") #print response followed by minutes

cycle_time = int(input("In minutes how fast did you complete the cycle? ")) #store as integer time for cycle
print("You completed the cycle in " + str(cycle_time) + " minutes\n") #print response followed by minutes

run_time = int(input("In minutes how fast did you complete the run? ")) #store as integer time for run
print("You completed the run in " + str(run_time) + " minutes\n") #print response followed by minutes

total_time = swim_time + cycle_time + run_time #store time of all added together as total_time

print("The total time for your triathlon is " + str(total_time) + " minutes\n") #print response as total_time in minutes

#  Print out made more appealing 
if total_time <= 100: #if total_time <= 100 print below
    print("***************Congratulations***************")
    print()
    print("You have been awarded your Provincial Colours\n")

elif total_time <= 105: #if total_time <= 105 print below
    print("+++++++Well done+++++++")
    print()
    print("Provincial Half Colours\n")

elif total_time <= 110: #if total_time <= 110 print below
    print("==Keep up the good work==")
    print()
    print("Provincial Scroll for you\n")

else: #if anything else print below
    print("Sorry you didn't gain an award this time, keep up the hard work you will get it next time\n")

"""
0 - 100 Provincial colours
101 - 105 Provincial Half colours
106 - 110 Provincial Scroll
111 + No award
"""