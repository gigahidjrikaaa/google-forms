from utils import get_data
from FillForm import fillForm
from selenium import webdriver

user = get_data()
data = {
  "web" : webdriver.Edge("C:\\Edge Webdriver\\msedgedriver.exe"),
  "_id" : user["id"],
  "fName" : user["first"],
  "lName" : user["last"],
  "passw" : user["password"],
  "email" : f"{user['first']}.{user['last']}@mail.ugm.ac.id", # there might be a number after the last name
  "link" : user['link']
}

f = fillForm(**data)
f.start()
