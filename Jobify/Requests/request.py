import requests

def profile_list():
    response = requests.get('http://127.0.0.1:8000/account/api-v1/profile-list/')
    return response

print(profile_list())