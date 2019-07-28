import json

#File Object Handler Init
resultsJSON = {}
resultsJSON['run'] = []

class File:
	#Buidling JSON object to dump into the text file
	def buildJSON(self, tryNumber, diceRoll, coinFlip, cardPick, outcome):
		outcomeDict = {
			'try': tryNumber,
			'dice': diceRoll,
			'coin': coinFlip,
			'card': cardPick,
			'result': outcome
		}

		resultsJSON['run'].append(outcomeDict) 

	def keyboardInterrupt(self,tryNumber):

		interruptMsg = {
			'try': tryNumber,
			'message': "Keyboard Interrupt on Try: " + str(tryNumber)
		}

		resultsJSON['run'].append(interruptMsg)

	#Writing the full JSON Object to results.txt
	def write(self):
		with open('results.txt',"w+") as result_file:
			json.dump(resultsJSON, result_file)