import requests
import json



def getAssets(cName, from_token , to_token):

    url = "https://api.opensea.io/api/v1/assets"
    arr= []
    for i in range(from_token , to_token+1,1):
        arr.append(i)
    lim = -from_token + to_token+1
    querystring = {"token_ids":arr,"order_direction":"asc","offset":"0","limit":lim,"collection":cName}

    response = requests.request("GET", url, params=querystring)
    if response.status_code!=200:
        return []
    jsonn = json.loads(response.text)
    return jsonn['assets']

def parseTraits(obj):
    dic = {}
    for i in obj:
        try:
            token = i['token_id']
            dic[token] = []
            for trait in i['traits']:
                dic[token].append((trait['trait_type'], trait['value'], trait['trait_count']))
        except:
            continue
    return dic
