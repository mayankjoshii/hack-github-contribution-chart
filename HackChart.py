import os

'''
This function makes commit for given numbe of days
@inNumberOfDays: number of days for which we want to
				 make commit in past
'''
def HackForDays(inNumberOfDays):

	#iterate the given number of days
	for itr in range(inNumberOfDays):

		'''
		update it at every iteration to
		make each commit unique
		'''
		dateString = str(itr) + ' day ago \n'
		
		'''
		Open log file and write commit date string.
		This is done because for every new commit we
		need to have some chagnes. Hence the @datString
		will always change. 
		'''
		with open('commit.log', 'w') as logFile:
			logFile.write(dateString)

		'''
		Add the changes and make a commit
		git commit --date is used to make commit in past
		'''
		os.system('git add .')
		os.system('git commit --date="' + dateString + '" -m "commit nuber=' + str(itr) + '"')


	#finally push all the commits to the github
	os.system('git push -u')

	#Print success message
	print("I have successfully hacked your github contribution chart for last " + str(inNumberOfDays) + " days 🥳")

def CheckInputType(inNumberOfDays):
	
	try:
		daysAsInt = int(inNumberOfDays)
		return daysAsInt
	except:
		print("I caught you trying to hack the program.🙂 \nI expect only integer input")
		return 0


#Execution Starts here

if __name__ == "__main__":

	helpString = "\nEnter number of days for which you want to make commit in past\n"\
	"Format: Number of Days in integer format\n"\
	"Example: 107 (if you want to make commit for last 107 days)\n"\
	"\nYour Input:"

	numberOfDays = input(helpString)
	numberOfDays = CheckInputType(numberOfDays)

	HackForDays(numberOfDays)
				