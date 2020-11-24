import random
import requests 

class Game:
	def __init__(self):
		self.random_grid() 

	def random_grid(self):
		lst=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Z","Y"]
		self.grid = random.sample(lst,9)
		print(self.grid)

	def is_valid(self, word):
		if not word:
			return False
		else:
			lst=self.grid.copy()
			for w in word:
				if(w in lst):
					lst.remove(w)
					print(w)
					print(lst)
				else:
					return False
			return self.__check_dictionary(word)

	@staticmethod
	def __check_dictionary(word):
		response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
		json_response = response.json()
		return json_response['found']
	
