import requests


#API URL
url="https://reqres.in/api/users?page=2"

#send Get Requests

response = requests.get(url)
print(response)

# Display Response content
print(response.content)

# display header
print(response.headers)

