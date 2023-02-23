import requests
import json
import jsonpath



#dng similar to postman api exmple, with username and pwd logged in and collectd token which it generated in functn1 and in functn 2 i wll make use of that token to perfrm post activity

#i can do 2 functions or i can declare global variable in function 1 and take it to functn2

def test_with_authentication2():

    auth_endpoint ='https://restful-booker.herokuapp.com/auth'

    auth_credentials= {
        'username' : 'admin',
        'password' : 'password123'
                    }
    auth_response = requests.post(auth_endpoint, json=auth_credentials)

    print(auth_response)
    assert auth_response.status_code == 200

    auth_data = auth_response.json()
    print(auth_data)

    auth_token = auth_data['token']
    print(auth_token)

#follow this sample api and create things which i created in postman using chat gpt code - https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBookings

#get bookings on uri
def test_get_bookings ():

    global json_response
    resource_endpoint='https://restful-booker.herokuapp.com/booking'
    response = requests.get(resource_endpoint)
    print(response)

    # convertg response into json
    #json_response = json.loads(response.text)
    json_response = response.json()
    print(json_response)

    # as json response stores in list, i can ask for any list index value to print
    #rembr as i had only i booking value in response it worked if have more values in response and i want only booking value then follow code like request chain

    print(json_response[1])


#get bookings on uri based on booking id

def test_get_bookings_on_id ():
    resource_endpoint = 'https://restful-booker.herokuapp.com/booking/1' +str(json_response[1])
    response = requests.get(resource_endpoint)
    print(response.text)


#create new booking and in that response whatever booking id am getting am gonna use that in next function to update it
# also here response contains more than just booking id so unlike above here we are particularly taking booking id from response

# method 1, here data is sent as file
def test_create_new_booking_meth1 ():

    global booking_id
    resource_endpoint = 'https://restful-booker.herokuapp.com/booking'

   #add headers just like postman, add headers given in api link if we dont add header content type = json/test it will take like plain text and it fails
    headers = {'Content-Type': 'application/json', 'Accept' :'application/json' }
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\create_booking.json', 'r')
    request_json = json.loads(file.read())
    print(request_json)

    response = requests.post(resource_endpoint,request_json)
    print(response)
    print(response.headers)

    # it is throwing 500 as content type in headers is text/plain i nned to update content type of headers to 'text/json'
    # now as gpt code define headers that are present as per our api link https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBooking

    #booking_id = jsonpath.jsonpath(response.json(), 'bookingid')
    #print(booking_id[0])

# method 2, here data is sent as json data directly

def test_create_new_booking_meth2 ():

    global booking_id
    resource_endpoint = 'https://restful-booker.herokuapp.com/booking'

   #add headers just like postman, add headers given in api link if we dont add header content type = json/test it will take like plain text and it fails
    headers = {
        'Content-Type': 'application/json',
        'Accept' :'application/json'
                }
    #add data body as per api like in postman https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-CreateBooking
    data ={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : true,
    "bookingdates" : {
                 "checkin" : "2018-01-01",
                 "checkout" : "2019-01-01"
                    },
    "additionalneeds" : "Breakfast"
    }

    response = requests.post(resource_endpoint, headers=headers, json=data)
    print(response)
    print(response.text)
