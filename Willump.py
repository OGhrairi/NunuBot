from DevKey import *
import json
import urllib.request
APIKey = key
print(APIKey)
SumName = input("Enter Summoner Name: ")

NSN = SumName.replace(' ','%20')
url="https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"
url +=NSN
url += "?api_key=RGAPI-38dcd00d-16b6-4912-b44d-97941d03b644"
print(url)
contents = urllib.request.urlopen(url).read()
infoList = (json.loads(contents))

print(infoList)