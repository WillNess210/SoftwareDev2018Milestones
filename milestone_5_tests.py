import requests
import unittest

#These Test API calls, see if they return correct values
class TestAPICalls(unittest.TestCase):
	#first call tests a recipe get call, checks if recipe with id 410 call gives back expected result
	def test_recipe(self):
		resp = requests.get('https://djibouti-recipe.herokuapp.com/api/recipes/790')
		for res in resp.json():
			print(res['name'])
			self.assertEqual(res['name'], "asdf");
	#second tests checks one of the ingredients (id = 20)
	def test_ingredient(self):
		resp = requests.get('https://djibouti-recipe.herokuapp.com/api/ingredients/870')
		for res in resp.json():
			print(res['name'])
			self.assertEqual(res['name'], "asdf");
	#third test checks on of the users (id = 17)
	def test_user(self):
		resp = requests.get('https://djibouti-recipe.herokuapp.com/api/users/17')
		for res in resp.json():
			print(res['username'])
			self.assertEqual(res['username'], "admin");

if __name__ == '__main__':
    unittest.main()
