from DevKey import *
import json
import urllib.request
APIKey = key
summonerID='' 

def SumDetails():#function that retrieves summoner information from summoner name (EUW only for the moment)
    global summonerID
    SumName = input("Enter Summoner Name: ")
    NSN = SumName.replace(' ','%20')
    url="https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"
    url +=NSN
    url += "?api_key="
    url += APIKey
    contents = urllib.request.urlopen(url).read()
    infoList = (json.loads(contents))
    summonerID = str(infoList['id'])#stores summoner id for use with other api functions
    return infoList

def ChampDetails(): #function that returns information related to 
    if summonerID == '':
        SumDetails()
    else:
        url='https://euw1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/'
        url += summonerID
        url += '?api_key='
        url += APIKey
        contents = urllib.request.urlopen(url).read()
        ChampDetailsList = (json.loads(contents))
        return ChampDetailsList

print(SumDetails())
print(ChampDetails())