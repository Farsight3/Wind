import json
import requests
p = requests.get("https://gist.githubusercontent.com/Farsight3/5c046fb91c880a5c03a207e030970f64/raw/0cbf7cfe80bb2b8add48c85ce514665473f815ba/person.json")
data_person = p.json()

c = requests.get("https://raw.githubusercontent.com/Farsight3/Wind/main/company.json")
data_company = c.json()

list_of_persons = (
    data_person["person"][0],
    data_person["person"][1]
    )

list_of_companies = (
    data_company["company"][0],
    data_company["company"][1],
    data_company["company"][2],
    data_company["company"][3],
    data_company["company"][4]
    )

class Lead():
    def __init__(self,full_name="",profile_url="",job_title="",location="",email="",phone_number="" ):
        self.full_name = full_name
        self.job_title = job_title
        self.profile_url = profile_url
        self.location = location
        self.email = email
        self.phone_number = phone_number





class Company():
    def __init__(self,name="",company_url="",location="",revenue="" ):
        self.name = name
        self.company_url = company_url
        self.location = location
        self.revenue = revenue



a = input("Введіть категорію company or person: ")
if a  == "person":
    a = Lead
    a = input("Введіть url person: ")
    if a == list_of_persons[0]["profile_url"]:
        print(list_of_persons[0])
    elif a == list_of_persons[1]["profile_url"]:
        print(list_of_persons[1])
elif a == "company":
     a = Company
     a = input("Введіть назву компанії :")
     if a == list_of_companies[0]["name"]:
        print(list_of_companies[0])
     elif a == list_of_companies[1]["name"]:
        print(list_of_companies[1])
     elif a == list_of_companies[2]["name"]:
        print(list_of_companies[2])
     elif a == list_of_companies[3]["name"]:
        print(list_of_companies[3])
     elif a == list_of_companies[4]["name"]:
        print(list_of_companies[4])











