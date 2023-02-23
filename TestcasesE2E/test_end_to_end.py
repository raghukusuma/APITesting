import requests
import json
import jsonpath


# adding a student with basic details

def test_Add_new_data():

    App_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open('C:/Users/rkusuma/Desktop/API/addstudent2.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(App_url,request_json)
    print(response.text)
