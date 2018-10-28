from DevKey import * #apikey must be stored in a DevKey.py file as variable 'key'
import json
import urllib.request
import os
APIKey = key
summonerID='' #numerical summoner identifier
champID='' #numerical champion identifier
SumChampInfo = []
def pathSel(fileName): #function that converts input filename to full ile path
    #file must be in same path as this file, and takes format 'FileName.FileExt'
    ProjectPath = (os.path.dirname(os.path.realpath(__file__)))
    output = ProjectPath + "\\" + fileName
    return output
  
with open(pathSel('champList.json')) as f:#load json champ info
   data = json.load(f)
CK=[]
CN=[]
for n in data["data"]: #goes through each champion, adds the key to one array,
    #and the id to another, to be put together in a dictionary
    CK.append(data["data"][n]['id'])
    CN.append(data["data"][n]['key'])
champDetails = dict(zip(CK,CN))#combines name and key of each champ into tuple dictionary
#print(champDetails['aatrox'])

def SumInfo():#function that retrieves summoner information from summoner name (EUW only for the moment)
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

def ChampNumber():#function that finds numerical id of a champ and stores in global champID var
    global champID
    champName = input("Enter Champion Name (Capitalise no spaces) ") #take champ name input to find id
    if champName in champDetails: #check validity of champ name
        champID = (champDetails.get(champName)) #if name is vaild, retrieve champ id
        return
        #print(champID) 
    else:    
        return("champ does not exist") #inform if champ name isn't valid
def ChampSumInfo(): #function that returns information related to a selected champion
    global SumChampInfo
    if summonerID == '':
        SumInfo()
    if champID == '':
        ChampNumber()
    url='https://euw1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/'
    url += summonerID
    url += '/by-champion/'
    url += champID
    url += '?api_key='
    url += APIKey
    contents = urllib.request.urlopen(url).read()
    SumChampInfo = (json.loads(contents))
    print(SumChampInfo)
    #above value has keys: playerId, championId, championLevel, championPoints, lastPlayTime
    #championPointsSinceLastLevel, championPointsUntilNextLevel, chestGranted, tokensEarned
    return

def champStats(): #return champion information from json file 
    CN = input('Enter Champion Name (Capitalise no spaces) ')
    return data['data'][CN]
  
def rankedInfo():#returns information about a summoner's rank
    if summonerID == '':
        SumInfo()
    url = 'https://euw1.api.riotgames.com/lol/league/v3/positions/by-summoner/'
    url += summonerID
    url += '?api_key='
    url += APIKey   
    contents = urllib.request.urlopen(url).read()
    sumRankedInfo = (json.loads(contents))
    return sumRankedInfo     




