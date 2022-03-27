import os

def HackForDays(inNumberOfDays):

	for itr in range(inNumberOfDays):
		
		dateString = str(itr) + ' days ago'
		with open('commit.log', 'a') as logFile:
			logFile.write(dateString)

		os.system('git add commit.log')
		os.system('git commit --date="' + dateString + '" -m "commit nuber=' + str(itr) + '"')


	os.system('git push origin master')


if __name__ == "__main__":
	HackForDays(20)
				