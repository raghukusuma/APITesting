import requests
import json
import jsonpath



#dng similar to postman api exmple, with username and pwd logged in and collectd token which it generated in functn1 and in functn 2 i wll make use of that token to perfrm post activity

#i can do 2 functions or i can declare global variable in function 1 and take it to functn2

def test_with_authentication2():
    global auth_token
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

    global id
    resource_endpoint='https://restful-booker.herokuapp.com/booking'
    response = requests.get(resource_endpoint)
    print(response)

    # convertg response into json
    #json_response = json.loads(response.text)
    json_response = response.json()
    print(json_response)

    # as json response stores in list, i can ask for any list index value to print
    #rembr as i had only i booking value in response it worked if have more values in response and i want only booking value then follow code like request chain

    #it displays first key value pair from dictionary which we got, but we want only value not key to parse for next
    print(json_response[0])

    #id = jsonpath.jsonpath(response.json(), 'bookingid')

    #easy method as per gpt - directly from response index am fetching field i wanted
    id= json_response[0]['bookingid']
    #now we get only value of booking id previously we got booking id key value pair
    print(id)


#get bookings on uri based on booking id

def test_get_bookings_on_id ():
    resource_endpoint = 'https://restful-booker.herokuapp.com/booking/' +str(id)
    response = requests.get(resource_endpoint)
    print(response.text)


#create new booking and in that response whatever booking id am getting am gonna use that in next function to update it
# also here response contains more than just booking id so unlike above here we are particularly taking booking id from response

def test_create_new_booking_meth2 ():

    global id2
    resource_endpoint = 'https://restful-booker.herokuapp.com/booking'

   #add headers just like postman, add headers given in api link if we dont add header content type = json/test it will take like plain text and it fails
    headers = {
        'Content-Type': 'application/json',
        'Accept' :'application/json'
                }
    #add data body as per api like in postman https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-CreateBooking
    data ={
    "firstname" : "rag_8pm",
    "lastname" : "new",
    "totalprice" : 111,
    "depositpaid" : "true",
    "bookingdates" : {
                 "checkin" : "2018-01-01",
                 "checkout" : "2019-01-01"
                    },
    "additionalneeds" : "Breakfast"
    }

    response = requests.post(resource_endpoint, headers=headers, json=data)
    print(response)
    print(response.text)

    #convert general response to json response
    json_response = response.json()

    #if i don't convert response to json like abve thn i cant take a seprte value from text response

    #from response i just wanted to collect booking id into a variable
    id2= json_response['bookingid']
    print(id2)

# method 1 to create booking - headers from code and json from file
def test_create_new_booking_meth1 ():

    global booking_id
    resource_endpoint = 'https://restful-booker.herokuapp.com/booking'

   #add headers just like postman, add headers given in api link if we dont add header content type = json/test it will take like plain text and it fails
    headers = {'Content-Type': 'application/json', 'Accept' :'application/json' }
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\create_booking.json', 'r')
    data = json.loads(file.read())
    print(data)

#sme hw gpt gave data=data and it is not wrkng thn i workd around and gave this formt it workd fr my kind of code may be gpt wrks fr that code as file as difrnt in that code
    response = requests.post(resource_endpoint,headers=headers,json=data)
    print(response)
    print(response.text)
    # it is throwing 500 as content type in headers is text/plain i nned to update content type of headers to 'text/json'
    # now as gpt code define headers that are present as per our api link https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBooking

    #booking_id = jsonpath.jsonpath(response.json(), 'bookingid')
    #print(booking_id[0])

# Updates a current booking, and booking id i wll fetch from above created id

def test_update_current_booking_widfixedid ():

   # resource_endpoint = 'https://restful-booker.herokuapp.com/booking/1'
    resource_endpoint = 'https://restful-booker.herokuapp.com/booking/' + str(id2)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': 'token=' + auth_token,
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    }

    print(auth_token)

    file = open('C:\\Users\\rkusuma\\Desktop\\API\\update_booking.json', 'r')
    data = json.loads(file.read())
    print(data)
    response = requests.put(resource_endpoint, headers=headers, json=data)
    print(response)
    print(response.text)

# get function for updated resource

def test_get_bookings_on_id2 ():
    #resource_endpoint = 'https://restful-booker.herokuapp.com/booking/' +str(json_response[1])
    resource_endpoint = 'https://restful-booker.herokuapp.com/booking/'+ str(id2)
    response = requests.get(resource_endpoint)
    print(response.text)
