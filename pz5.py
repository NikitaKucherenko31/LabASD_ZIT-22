import requests
import json
# Вариант по последней цифре студенческого: №8 https://github.com/ansible/ansible
# Полное имя репозитория: ansible/ansible
def git_json_request():
   repos_name=str(input("Введите полное имя репозитория репозитория: "))
   full_name = repos_name.split("/")
   owner = full_name[0]
   repos = full_name[1]
   repos_url = f"https://api.github.com/repos/{owner}/{repos}"
   user_url = f"https://api.github.com/users/{owner}"
   user_response = requests.get(user_url)
   repos_response = requests.get(repos_url)
   if user_response.status_code == 200 and repos_response.status_code == 200:
      with open("get_json_repos_data.json","w+") as f:
           user_data = user_response.json()
           repos_data = repos_response.json()
           repos_json_items = {
                  "company": user_data["company"],
                  "created_at": repos_data["created_at"],
                  "email": user_data["email"],
                  "id": repos_data["id"],
                  "name": repos_data["name"],
                  "url": repos_data["url"],
           }
           json.dump(repos_json_items, f, indent=4) 
   else:
      print("Ошибка установки соединения!")
git_json_request()
