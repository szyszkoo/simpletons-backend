from flask import jsonify

from models import *


def jsonToUser(json):
    username = json.get('username')
    email = json.get('email')
    password = json.get('password')
    firstname = json.get('firstname')
    return User(xid=0, username=username, email=email, password=password, name=firstname)


def getUserResponse(user):
    return jsonify({"id": user.xid,
                    "username": user.username,
                    "email": user.email,
                    "firstname": user.name})


def createUserResponse(user_id):
    return jsonify({"id": user_id})


def getCategoriesResponse(categories):
    response = []
    for category in categories:
        response.append({"id": category.xid,
                         "user_id": category.user_id,
                         "name": category.name})
    return jsonify(response)


def getFiszkiResponse(fiszki):
    response = []
    for fiszka in fiszki:
        response.append({"id": fiszka.xid,
                         "category_id": fiszka.category_id,
                         "language": fiszka.src_lang,
                         "text": fiszka.name})
    return jsonify(response)
