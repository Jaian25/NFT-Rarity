import json


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
    prev = 0
    prev_cnt = 0
    rare_dict = {}
    for i in s:
        cnt = i[0]
        tag = (i[1],i[2])
        
        val = 0
        if cnt == prev_cnt: 
            val = prev
        else:
            val = prev+1
        prev = val
        prev_cnt = cnt
        rare_dict[tag] = val
    return rare_dict

def calc_Traits_point(ranks):
    point_dict = {}
    a = 99999999999999999999
    for rank in ranks:
        power = a / 2**(ranks[rank]-1)
        point_dict[rank] = power
        #print(rank,power)
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
    
trait_ranks = calc_traits_rank('koala-intelligence-agency')
trait_points = calc_Traits_point(trait_ranks)
#print(trait_points)
rank = []

for i in range(10000):
    b = get_points_of_token('koala-intelligence-agency',i,trait_points)
    rank.append((b,i))
print('done')
rank.sort(reverse=True)
q = open(f'result.json', 'w', encoding='utf-8')
json.dump(rank, q, ensure_ascii=False, indent=4)


#calc_Traits_point(calc_traits_rank('koala-intelligence-agency'))

#print(calc_traits_rank('koala-intelligence-agency'))
