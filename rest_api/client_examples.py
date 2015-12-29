# Basic connection with the api

import requests
import pprint
response = requests.get('http://localhost:8000/api/')
response.status_code
response.json()
response = requests.get(api['sprints'])
response.status_code
response = requests.get(api['sprints'], auth=('demo', 'test'))
response.status_code
pprint.pprint(response)


# Create new sprint

import datetime
today = datetime.date.today()
two_weeks = datetime.timedelta(days=14)
data = {'name': 'Current Sprint', 'end': today + two_weeks}
response = requests.post(api['sprints'], data=data, auth=('demo', 'test'))
response.status_code
sprint = response.json()
pprint.pprint(sprint)
