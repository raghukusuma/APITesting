import requests
import json
import jsonpath
#API URL
url="https://reqres.in/api/users?page=2"

#send Get Requests
response = requests.get(url)

#validate specific count of response - we can do that by jsonpath - ( fetch response content with json path )

#parse response to json format

# text am loading into json format, and storing into a variable

json_response=json.loads(response.text)

#print(json_response)

#fetch value using json path

#when evr we apply jsonpath to anyresponse it is gng to return a list and list can have any no.of items

pages= jsonpath.jsonpath(json_response,'total_pages')

#currntly am printing only first index value of list

#print(pages[0])

#validating pages count now

assert pages [0] == 2


# below code as per chat gpt

if pages [0] == 2:

    print ( "pass")

else:
    print("fail")
