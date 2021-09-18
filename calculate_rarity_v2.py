import json
import datetime

version = 1.02

name = 'koala-intelligence-agency'

lowest = 99999999
highest = -9999999

def calc_traits_rank(cName):
    f = open(f'{cName}.json')
    jsondata = json.load(f)
    s = set()
    for i in jsondata : 
        #print(i)
        for j in jsondata[i] : 
            #print(j)
            s.add((j[2] , j[0] , j[1]))
    s = sorted(s)
    global highest
    global lowest
    rare_dict = {}
    for i in s:
        cnt = i[0]
        tag = (i[1],i[2])
        lowest = min(lowest , cnt)
        highest = max(highest , cnt)
        rare_dict[tag] = cnt
    return rare_dict

def calc_Traits_point(ranks):
    point_dict = {}
    y1 = 1000000
    y2 = 5
    x1 = lowest
    x2 = highest
    m = (y1 - y2) / (x1 -x2)
    #print(m)
    for rank in ranks:
        points = y1 + m*(ranks[rank] - x1)
        if ranks[rank] == x1:
            points = 10000000
        point_dict[rank] = points

        #print(rank , ranks[rank] , points)
        
   # print(lowest,highest)
    return point_dict

def get_points_of_token(cName, token , point_dict):
    f = open(f'{cName}.json')
    jsondata = json.load(f)
    zed_points = 0
    for i in jsondata[str(token)]:
        tag = (i[0],i[1])
        
        zed_points = zed_points + point_dict[tag]
    print(zed_points,token)
    return zed_points
    
trait_ranks = calc_traits_rank(name)
trait_points = calc_Traits_point(trait_ranks)
#print(trait_points)
rank = []

for i in range(10000):
    b = get_points_of_token(name,i,trait_points)
    rank.append((b,i))
print('done')
rank.sort(reverse=True)
q = open(f'{name}_result.json', 'w', encoding='utf-8')
json.dump(rank, q, ensure_ascii=False, indent=4)


#calc_Traits_point(calc_traits_rank('koala-intelligence-agency'))

#print(calc_traits_rank('koala-intelligence-agency'))
