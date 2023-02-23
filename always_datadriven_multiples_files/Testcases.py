import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_multiple_students():

    # API
    Api_url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\rkusuma\\Desktop\\API\\addstudent2.json', 'r')
    json_request = json.loads(file.read())

    obj = Library.common("C:\\Users\\rkusuma\\Desktop\\API\\Test_data_exl.xlsx","Sheet1")
    col = obj.fetch_column_count()
    row= obj.fetch_row_count()
    keyList=obj.fetch_key_names()

    for i in range(2,row+1):
        updated_json_request = obj.update+request_with_data(i,json_request,keyList)
        response = requests.post(api_url,updated_json_request)
        print(response)






