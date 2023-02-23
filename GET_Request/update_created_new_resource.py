import requests
import json
import jsonpath

url="https://reqres.in/api/users/2"

#post creating a resource , put updating a resource, when a resource is created 201 we get

#post lo we shd send a request body i.e a body to create our post

#read input json file

#opening file in read only mode

file = open('C:\\Users\\rkusuma\\Desktop\\API\\Createuser.json','r')

#reading content from file and storing it in variable
json_input=file.read()

#as above content is only string for us so we need to parse it into json format
request_json=json.loads(json_input)

#print(request_json)

#now put request wr we will send this json input as a body

#make put request with json input body

response=requests.put(url,request_json)

print(response.content)

#validating response code
assert response.status_code == 200

#parse response content
response_json=json.loads(response.text)

updated_list = jsonpath.jsonpath(response_json,'updatedAt')

print(updated_list[0])






