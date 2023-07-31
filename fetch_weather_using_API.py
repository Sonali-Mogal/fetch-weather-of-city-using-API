def temp_in_celsius(K):
    C = K - 273.15
    return C


import requests, json

api_key = "a77433a5631c402c3cb5004de0b769ee"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise, city is not found

if x["cod"] != "404":

    # store the value of "main" key in variable y
    y = x["main"]

    # store the value corresponding to the "temp" key of y
    current_temperature = y["temp"]
    current_temperature = temp_in_celsius(current_temperature)
    print(" Temperature (in degree celsius) = ", round(current_temperature, 2), chr(176) + "C")
else:
    print(" City Not Found ")