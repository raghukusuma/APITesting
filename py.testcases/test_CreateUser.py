import requests
import json
import jsonpath

#write a method for pytest and code shd be inside method, also method name shd start with tes

def test_create_new_user():
    url="https://reqres.in/api/users"
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
    #now post request wr we will send this json input as a body
    #make post request with json input body
    response=requests.post(url,request_json)
    print(response.content)
    #validating response code
    assert response.status_code == 201
    #fetch header from response
    print(response.headers)
    #if we want specific headers then
    print(response.headers.get('Content-Type'))
    print(response.headers.get('Content-Length'))
    # i want id value from response content
    # parse response to json format
    response_json=json.loads(response.text)
    # pick id using json path
    #jsonpath.jsonpath(response_json,'id')
    # we knw abve gonna fetch list so we wanna have first item of list so
    id=jsonpath.jsonpath(response_json,'id')
    #wen evr we are applyng json path it always returns list , even if it finds a single value
    # so wat ever list it is fetching we are storing it in id and fetching first value
    print(id[0])


