'''Tests for all the mcoc methods'''
import unittest
import json
import requests


class MCOCTest(unittest.TestCase):
    def setUp(self):
        pass

class TestAddChampion(MCOCTest):
    def test_add_champion1(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/add_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Captain America WII",
		                "class" : "Science",
		                "rank" : "Average",
		                "2_Star" : true,
		                "3_Star" : true,
		                "4_Star" : true,
		                "5_Star" : false
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        champion = json.loads(req.text)

        #Test Response
        self.assertEqual(champion['name'], "Captain America WII")
        self.assertEqual(champion['class'], "Science")
        self.assertEqual(champion['rank'], "Average")
        self.assertEqual(champion['2_Star'], True)
        self.assertEqual(champion['3_Star'], True)
        self.assertEqual(champion['4_Star'], True)
        self.assertEqual(champion['5_Star'], False)
        #Test Database content
        

    def test_add_champion2(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/add_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Captain America WII",
		                "class" : "Science",
		                "rank" : "Average",
		                "2_Star" : true,
		                "3_Star" : true,
		                "4_Star" : true,
		                "5_Star" : false
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        self.assertEqual(req.text, '{}')
        self.assertTrue(req.status_code == 200)

class TestGetChampion(MCOCTest):

    def test_get_champion1(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/get_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Captain America WII"
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        
        champion = json.loads(req.text)
        #Test Connection
        self.assertTrue(req.status_code == 200)
        #Test Response
        self.assertEqual(champion['name'], "Captain America WII")
        self.assertEqual(champion['class'], "Science")
        self.assertEqual(champion['rank'], "Average")
        self.assertEqual(champion['2_Star'], True)
        self.assertEqual(champion['3_Star'], True)
        self.assertEqual(champion['4_Star'], True)
        self.assertEqual(champion['5_Star'], False)
        #Test Database content

    def test_get_champion2(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/get_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Batman"
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        self.assertEqual(req.text, '{}')
        self.assertTrue(req.status_code == 200)

class TestUpdateChampion(MCOCTest):

    def test_update_champion1(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/update_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Wolverine",
		                "class" : "Mutant",
		                "rank" : "God",
		                "2_Star" : true,
		                "3_Star" : true,
		                "4_Star" : true,
		                "5_Star" : false
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        
        champion = json.loads(req.text)
        #Test Connection
        self.assertTrue(req.status_code == 200)
        #Test Response
        self.assertEqual(champion['name'], "Wolverine")
        self.assertEqual(champion['class'], "Mutant")
        self.assertEqual(champion['rank'], "God")
        self.assertEqual(champion['2_Star'], True)
        self.assertEqual(champion['3_Star'], True)
        self.assertEqual(champion['4_Star'], True)
        self.assertEqual(champion['5_Star'], False)
        #Test Database content

    def test_update_champion2(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/update_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Wolverine",
		                "class" : "Mutant",
		                "rank" : "Demi-God",
		                "2_Star" : true,
		                "3_Star" : true,
		                "4_Star" : true,
		                "5_Star" : false
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        
        champion = json.loads(req.text)
        #Test Connection
        self.assertTrue(req.status_code == 200)
        #Test Response
        self.assertEqual(champion['name'], "Wolverine")
        self.assertEqual(champion['class'], "Mutant")
        self.assertEqual(champion['rank'], "Demi-God")
        self.assertEqual(champion['2_Star'], True)
        self.assertEqual(champion['3_Star'], True)
        self.assertEqual(champion['4_Star'], True)
        self.assertEqual(champion['5_Star'], False)

    def test_update_champion3(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/update_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Batman",
		                "class" : "Science",
		                "rank" : "Average",
		                "2_Star" : true,
		                "3_Star" : true,
		                "4_Star" : true,
		                "5_Star" : false
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        self.assertEqual(req.text, '{}')
        self.assertTrue(req.status_code == 200)

class TestRemoveChampion(MCOCTest):

    def test_remove_champion1(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/remove_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Captain America WII"
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        
        champion = json.loads(req.text)
        #Test Connection
        self.assertTrue(req.status_code == 200)
        #Test Response
        self.assertEqual(champion['name'], "Captain America WII")
        self.assertEqual(champion['class'], "Science")
        self.assertEqual(champion['rank'], "Average")
        self.assertEqual(champion['2_Star'], True)
        self.assertEqual(champion['3_Star'], True)
        self.assertEqual(champion['4_Star'], True)
        self.assertEqual(champion['5_Star'], False)
        #Test Database content
        
    def test_remove_champion2(self):
        url = 'http://0.0.0.0:10000/api/v1/namespaces/snafu/actions/remove_champion.lambda_handler'
        data = '''{"event" : 
	                {
		                "name" : "Batman"
	                }
                }'''
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url, data, headers)
        self.assertEqual(req.text, '{}')
        self.assertTrue(req.status_code == 200)


    
if __name__ == '__main__':
    unittest.main()