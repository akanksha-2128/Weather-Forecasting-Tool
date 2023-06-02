import argparse
API_KEY='my api key'
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

# Construct API URL with query parameters 

parser = argparse.ArgumentParser()
parser.add_argument('city', help='City name')
args = parser.parse_args()
url=f"{BASE_URL}?q={args.city}&appid={API_KEY}&units=metric"

# Send HTTP GET request
# Make API request and parse response using request module
#import request module

import requests
response=requests.get(url)
# Check status code of response to confirm success
if response.status_code!=200:
    print('Sorry! Could not get details for the city. Please try again later.')
    exit()
# Parse JSON response
data=response.json()

# get information from data

country=data['sys']['country']
city=data['name']
temperature=data['main']['temp']
feels_like=data['main']['feels_like']
clouds=data['clouds']['all']
#rain=data['rain']['1h']
wind=data['wind']['speed']

# Print weather details
output=f"Country:{country}\n"
output+=f"City:{city}\n"
output+=f"Temperature:{temperature}deg C\n"
output+=f"feels_like:{feels_like}deg C\n"
output+=f"clouds:{clouds}\n"
#output+=f"rain:{rain}\n"
output+=f"wind:{wind}\n"

print(output)

