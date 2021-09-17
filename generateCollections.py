from osAPI import *
import json
import time
garbage = []

def gen(cName, start , end):
    lst = {}
    for i in range(start , end+1 , 30):
       # print(i)
        try:
            json_data = getAssets(cName , i , min(i+29 , end))
            traits = parseTraits(json_data)
            lst.update(traits)
            time.sleep(0.25)
        except:
            garbage.append((i,i+29))
    f = open(f'{cName}.json', 'w', encoding='utf-8')
    print(garbage)
    json.dump(lst, f, ensure_ascii=False, indent=4)
    f.close()
gen('koala-intelligence-agency',0,9999)
