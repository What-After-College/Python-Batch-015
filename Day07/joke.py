import requests

url = "https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,racist,sexist"

response = requests.get(url)
# print(response)

recieved_data = response.json()
# print(recieved_data)
# print(type(recieved_data))
# print(recieved_data["category"])

for x in recieved_data.keys():
    if x == "id" or x=="type" or x=="flags" or x=="error":
        continue
    print("{} : {}".format(x, recieved_data[x]))

