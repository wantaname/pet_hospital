
import requests

baseURL = "http://127.0.0.1:5000"

login = {
    "url":baseURL+"/user/login",
    "wish":""
}
res = requests.post("/user/login",json={
    "username":"test123",
    "password":"test123"
})
print(res.json())