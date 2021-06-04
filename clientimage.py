import requests


resp = requests.post(" https://fauzantorch.herokuapp.com/",
                     files={'file': open('dog.png', 'rb')})
print(resp.text)
