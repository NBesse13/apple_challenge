import json
#File Handler to avoid the play program becoming too beefy
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

	def write(self):
		with open('results.txt',"w+") as result_file:
			json.dump(resultsJSON, result_file)