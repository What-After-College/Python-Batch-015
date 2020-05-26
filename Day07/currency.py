import requests

url = "https://currencyapi.net/api/v1/rates?key=AZcoollxIoPSPU9G5GeS6rsOtf9odRYRATKw"

response = requests.get(url)
# print(response)

data = response.json()
# print(data)

for x in data.keys():
    if x == "rates":
        currency_data = data['rates']
        for d in currency_data.keys():
            if d == 'INR':
                # print("{} : {}".format(d, currency_data[d]))
                inr = currency_data[d]
                break

# inr = data["rates"]["INR"]

user_input = int(input("Enter the Dollars: "))
k = user_input*inr
print("The Dollars when converted in Indian Rupees will be equal to: {}".format(k))

