import requests
poke_name = input("Enter the name of Pokemon: ")
url = "https://api.pokemontcg.io/v1/cards?name={}".format(poke_name)

response = requests.get(url)
# print(response)
recieved_data = response.json()
# print(recieved_data)

import matplotlib.pyplot as plt
# url_data = recieved_data["cards"][1]["imageUrl"]
# print(url_data)
url_data = requests.get(recieved_data["cards"][0]["imageUrl"])
with open('./poke.png','wb') as f:
    for item in url_data.iter_content(4096):
        f.write(item)

image_data = plt.imread('./poke.png')
plt.imshow(image_data)
plt.show()        