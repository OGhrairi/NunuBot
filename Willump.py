from DevKey import * #apikey must be stored in a DevKey.py file as variable 'key'
import json
import urllib.request
import os
APIKey = key
summonerID='' 
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
    CK.append(data["data"][n]['id'].lower())
    CN.append(data["data"][n]['key'])
champDetails = dict(zip(CK,CN))#combines name and key of each champ into tuple dictionary
#print(champDetails['aatrox'])
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

def ChampDetails(): #function that returns information related to a selected champion
    if summonerID == '':
        SumDetails()
    else:
        champName = input("Enter Champion Name (no spaces)") #take champ name input to find id
        if champName in champDetails: #check validity of champ name
            champID = (champDetails.get(champName)) #if name is vaild, retrieve champ id
            #print(champID) 
        else:    
            return("champ does not exist") #inform if champ name isn't valid
        url='https://euw1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/'
        url += summonerID
        url += '?api_key='
        url += APIKey
        contents = urllib.request.urlopen(url).read()
        ChampDetailsList = (json.loads(contents))

        return ChampDetailsList

print(SumDetails())
print(ChampDetails())