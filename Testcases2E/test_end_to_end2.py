import requests
import json
import jsonpath


# adding a student with basic details

# execution of end to shown in youtube last video

def test_Add_new_data():

    App_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\addstudent2.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(App_url, request_json)
    print(response.text)

    # from json response fetch id value and store in id is what we are doing now

    id = jsonpath.jsonpath(response.json(), 'id')
    # as it stores in form of list we are giving 0 index
    print(id[0])

    # adding techincal details

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\addtechncl.json', 'r')
    request_json = json.loads(file.read())

    #for variable id storing
    request_json['id']=int(id[0])
    request_json['st_id'] = id[0]

    response = requests.post(tech_api_url, request_json)
    print(response.text)

    # adding adress

    add_api_url = "https://thetestingworldapi.com/api/addresses"
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\addadress.json', 'r')
    request_json = json.loads(file.read())

    # for variable id storing
    request_json['stId'] = id[0]

    response = requests.post(add_api_url, request_json)
    #print(response.text)

    # fetch complete details of student

    #final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/4229825"
    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)
