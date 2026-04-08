import json

data = {
    "users":[
        {"id":1,"email":"test1@test.com","country":"IE"},
        {"id":2,"email":"test2@test.com","country":"US"}
    ],
    "orders":[
        {"id":101,"userId":1,"amount":100},
        {"id":102,"userId":3,"amount":200}
    ]
}

users = {u["id"] for u in data["users"]}

for order in data["orders"]:
    if order["userId"] not in users:
        print("Invalid user reference:", order)
