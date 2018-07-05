import protocol
from api import API

def login(id, pw):
    body = {
       'user_id': id,
       'user_pw': pw
    }

    res = protocol.post(API['login'], body).json()
    return res[0]

def guest(name, pw):
    data = {
        'type': 'guest',
        'name': name,
        'password': pw,
        'stype': 'C'
        #유동 C, 고닉 A, 반고닉 B

    }
    return data
