import requests

def test_with_authentication2 ():

    auth_endpoint ='https://restful-booker.herokuapp.com/auth'

    auth_credentials= {
        'username' : 'admin',
        'password' : 'password123'
                    }
    auth_response = requests.post(auth_endpoint, json=auth_credentials)

    print(auth_response)
    assert auth_response.status_code == 200

    auth_data = auth_response.json()
    auth_token = auth_data['token']

    print(auth_token)


