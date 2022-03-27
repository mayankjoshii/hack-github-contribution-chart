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


#Execution Starts here

if __name__ == "__main__":

	helpString = "\nEnter number of days for which you want to make commit in past\n"\
	"Format: Number of Days in integer format\n"\
	"Example: 107 (if you wnat to make commit for last 107 days\n"\
	"\nYour Input:"

	numberOfDays = int(input(helpString))

	HackForDays(numberOfDays)
				