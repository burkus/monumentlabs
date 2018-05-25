# You did not specify a MySQL API
# I googled around for some and found a seemingly nice one
# link: https://www.tutorialspoint.com/python3/python_database_access.htm
# This is the requests library
# Link: http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
import PyMySQL
import requests
from requests_oauthlib import OAuth1

db = PyMySQL.connect(....)

cursor = db.cursor()

intercomURL = "https://api.intercom.io/users"
auth = OAuth1('INTERCOM_APP_KEY', 'APP_SECRET', 'TOKEN', 'TOKEN_SECRET')
postToIntercom = lambda user: requests.post(intercomURL, user, auth=auth)

def getUsers():
    users = []
    q = "SELECT id, name, email FROM user"
    try:
        cursor.execute(q)
        results = cursor.fetchall()
        for row in results:
            id, name, email = row[:3]
            users.append((id, name, email))
        return users
    except:
        print("RIP.")
        return []

def postUsers(users):
    for user in users:
        id, name, email = user
        postToIntercom({ 'id': id, 'name': name, 'email': email })

postUsers(getUsers())
