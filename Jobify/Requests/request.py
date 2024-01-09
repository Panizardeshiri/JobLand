import requests

def profile_list():
    response = requests.get('http://127.0.0.1:8000/account/api-v1/profile-list/')
    return response

print(profile_list())

def edit_profile(first_name,last_name,description,token):
    response = requests.post('http://127.0.0.1:8000/account/api-v1/edit-profile/', {'first_name':first_name,'last_name':last_name,'description':description,},headers={
        "Authorization": f"Bearer {token}"}
    )

    print(response.text)


# edit_profile('pann','hosi','nothing','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1OTM5OTcwLCJpYXQiOjE3MDQ3MzAzNzAsImp0aSI6IjU4NTA1ZGQ2OTE3MjRjOWU5OWFlNDc1ZmEwMmQ1NGNjIiwidXNlcl9pZCI6MTh9.A3tcavkbHbqakCKJmJe0ElZBozWCQwcA2qhXfnuSTSw')


def address(token):
    response = requests.get('http://127.0.0.1:8000/account/api-v1/add-address/',headers={
        "Authorization":f"Bearer {token}"
    })
    print(response.text)


address('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDE0OTA4LCJpYXQiOjE3MDQ4MDUzMDgsImp0aSI6IjJhMmYzZDJhMDE1ZjQ2MmU4MGMzMjFlMzYwY2U2NjFjIiwidXNlcl9pZCI6MTh9.mc9LwO6sL7RqrIJLngfLLke3nKSc3qQem_tIxsMrCg8')


def address(state,city,street,alley,plaque,postal_code,extra_comment,user,token):
    response = requests.post('http://127.0.0.1:8000/account/api-v1/add-address/',{'state':state,'city':city,'street':street,'alley':alley,'plaque':plaque,'postal_code':postal_code,'extra_comment':extra_comment,'user':user},headers={
        "Authorization":f"Bearer {token}"
    })
    print(response.text)


# address('maz','bab','hab','to','4','123456789','not','18','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDE0OTA4LCJpYXQiOjE3MDQ4MDUzMDgsImp0aSI6IjJhMmYzZDJhMDE1ZjQ2MmU4MGMzMjFlMzYwY2U2NjFjIiwidXNlcl9pZCI6MTh9.mc9LwO6sL7RqrIJLngfLLke3nKSc3qQem_tIxsMrCg8')

def address(state,city,street,alley,plaque,postal_code,extra_comment,token):
    response = requests.put('http://127.0.0.1:8000/account/api-v1/edit-address/11',{'state':state,'city':city,'street':street,'alley':alley,'plaque':plaque,'postal_code':postal_code,'extra_comment':extra_comment},headers={
        "Authorization":f"Bearer {token}"
    })
    print(response.text)


# address('mazzzzz','bab','hab','to','4','123456789','not','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDE0OTA4LCJpYXQiOjE3MDQ4MDUzMDgsImp0aSI6IjJhMmYzZDJhMDE1ZjQ2MmU4MGMzMjFlMzYwY2U2NjFjIiwidXNlcl9pZCI6MTh9.mc9LwO6sL7RqrIJLngfLLke3nKSc3qQem_tIxsMrCg8')

def delete_address(token):
    response = requests.delete('http://127.0.0.1:8000/account/api-v1/edit-address/11',headers={
        "Authorization":f"Bearer {token}"
    })
    print(response.text)
# delete_address('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDE0OTA4LCJpYXQiOjE3MDQ4MDUzMDgsImp0aSI6IjJhMmYzZDJhMDE1ZjQ2MmU4MGMzMjFlMzYwY2U2NjFjIiwidXNlcl9pZCI6MTh9.mc9LwO6sL7RqrIJLngfLLke3nKSc3qQem_tIxsMrCg8')

