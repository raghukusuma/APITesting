import json
import jsonpath
import requests

#pick response data from one request and using it as input in another request is called request chaining

#always method name shd start with test if not it wont run
def test_add_new_student_():
    global id
    API_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\addstudent.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(API_url, request_json)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

# id[0] should not be used here because that id is local to that method here am using it in anthr method so in abve function declare that as global
# as am using id it is a numberic now am concatinating with url so change it to string format

def test_get_details():
    API_url = "https://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_url)
    print(response.text)



