import random
import requests

rand = random.randrange(1,17)
url = 'http://192.168.10.1:8080/lockers/' + str(rand)
print(url)
x = requests.post(url, 'action=OPEN')

print(x.text)
