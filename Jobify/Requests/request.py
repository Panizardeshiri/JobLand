import requests

def profile_list():
    response = requests.get('http://127.0.0.1:8000/account/api-v1/profile-list/')
    return response

# print(profile_list())

def edit_profile(first_name,last_name,bio,skill,token):
    response = requests.post('http://127.0.0.1:8000/account/api-v1/edit-profile/', {'first_name':first_name,'last_name':last_name,'bio':bio,'skill':skill,},headers={
        "Authorization": f"Bearer {token}"}
    )

    print(response.text)


# edit_profile('pann','hosi','nothing',' 2','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDE0OTA4LCJpYXQiOjE3MDQ4MDUzMDgsImp0aSI6IjJhMmYzZDJhMDE1ZjQ2MmU4MGMzMjFlMzYwY2U2NjFjIiwidXNlcl9pZCI6MTh9.mc9LwO6sL7RqrIJLngfLLke3nKSc3qQem_tIxsMrCg8')


def address(token):
    response = requests.get('http://127.0.0.1:8000/account/api-v1/add-address/',headers={
        "Authorization":f"Bearer {token}"
    })
    print(response.text)


# address('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDE0OTA4LCJpYXQiOjE3MDQ4MDUzMDgsImp0aSI6IjJhMmYzZDJhMDE1ZjQ2MmU4MGMzMjFlMzYwY2U2NjFjIiwidXNlcl9pZCI6MTh9.mc9LwO6sL7RqrIJLngfLLke3nKSc3qQem_tIxsMrCg8')


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
    response = requests.delete('http://127.0.0.1:8000/account/api-v1/edit-address/8',headers={
        "Authorization":f"Bearer {token}"
    })
    print(response.text)
# delete_address('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDE0OTA4LCJpYXQiOjE3MDQ4MDUzMDgsImp0aSI6IjJhMmYzZDJhMDE1ZjQ2MmU4MGMzMjFlMzYwY2U2NjFjIiwidXNlcl9pZCI6MTh9.mc9LwO6sL7RqrIJLngfLLke3nKSc3qQem_tIxsMrCg8')

def add_skill(skill,token):
     response = requests.post('http://127.0.0.1:8000/account/api-v1/add-skill/',{'skill':skill}, headers={
        "Authorization":f"Bearer {token}"
     })

     print(response.json())

add_skill('2','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDk1NTU2LCJpYXQiOjE3MDQ4ODU5NTYsImp0aSI6IjI3MmY2ZDFiY2QzODQ2Mjc5ZDYzNGNiNDc1NDc2Y2FlIiwidXNlcl9pZCI6MTh9.oVUJpOBvNtd53ySTchZ3QNdJQNwVTUIZxrpHDbIofsw')
