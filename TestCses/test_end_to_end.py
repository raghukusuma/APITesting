import requests
import json
import jsonpath

# execution 4 methods shown in udemy

# adding a student with basic details - POST

def test_Add_new_data():

    App_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\addstudent2.json','r')
    request_json = json.loads(file.read())
    response = requests.post(App_url,request_json)
    print(response.text)

def test_get_student_data():
    App_url = "https://thetestingworldapi.com/api/studentsDetails/4229818"
    response=requests.get(App_url)
    #print(response.text)
    json_response = json.loads(response.text)
    # or json_response = response.json() - this also we can use instead of json loads, it wl auto mtcly transltes our response to json formt
    id=jsonpath.jsonpath(json_response,'data.id')
    print(id)
    #as assert it passes if we change comparsn value then it fails
    assert id[0]==4229788


#my experimnts i can do like collectn variable instead of direct id like what gets created i shd collect and pass it here


def test_update_new_data():

    App_url = "https://thetestingworldapi.com/api/studentsDetails/4229818"
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\addstudent3.json','r')
    request_json = json.loads(file.read())
    response = requests.put(App_url,request_json)
    print(response.text)


# fetching data for validating whethr updated properly or not

def test_get_student_data():
    App_url = "https://thetestingworldapi.com/api/studentsDetails/4229788"
    response=requests.get(App_url)
    #print(response.text)
    json_response = json.loads(response.text)
    # or json_response = response.json() - this also we can use instead of json loads, it wl auto mtcly transltes our response to json formt

    #print json response to see updated value
    print(json_response)


def test_delete_studen():
    App_url = "https://thetestingworldapi.com/api/studentsDetails/4229818"
    response=requests.delete(App_url)
    print(response.text)

#fetching data again for validating deleted or not - assert should fail as once deltd it shd not fetch data

def test_get_student_data():
    App_url = "https://thetestingworldapi.com/api/studentsDetails/4229818"
    response=requests.get(App_url)
    #print(response.text)
    json_response = json.loads(response.text)
    # or json_response = response.json() - this also we can use instead of json loads, it wl auto mtcly transltes our response to json formt

    #print json response to see updated value
    print(json_response)
    # or json_response = response.json() - this also we can use instead of json loads, it wl auto mtcly transltes our response to json formt
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    # as assert it passes if we change comparsn value then it fails
    assert id[0] == 4229818


