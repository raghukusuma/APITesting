import requests
import json
import jsonpath


# adding a student with basic details

# execution of end to shown in youtube last video

def test_Add_new_data():

    App_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\addstudent2.json','r')
    request_json = json.loads(file.read())
    response = requests.post(App_url,request_json)
    print(response.text)





