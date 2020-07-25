import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = ''  #githup token code
    
    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+ username +'/repos')
        return response.json()

    def createRepository(self,name):
        response = requests.post(self.api_url+'/user/repos?access_token='+ self.token, json={
         
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()

bilgi = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\n Seçim:')

    if secim == '4':
        break
    else:
        if secim =='1':
            username=input('username:')
            result = bilgi.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
        if secim =='2':
            username = input('username:')
            result = bilgi.getRepositories(username)
            for repo in result:
                print(repo['name'])
        if secim =='3':
            name = input('repository name:')
            result = bilgi.createRepository(name)
            print(result)
        else:
            print('Error')