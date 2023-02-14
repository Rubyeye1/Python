''' print("nico".upper())         # 메소드
print("nico".endswith("a")) '''

''' numbers = [5,3,1,5,7,3,"True",True,12] # 리스트
numbers.append(["emoge"])
print(numbers)
numbers.clear()
print(numbers)
numbers.append("happy")
print(numbers)
print(numbers[3]) '''

''' numbers = (1,2,3,4,5)       # 튜플
print(numbers[-1]) '''

player = {                      # 딕셔너리
    "name":"nico",
    "age":12,
    "alive":True,
    "fav_food":("emoge","hamburger"),
    "friend":{
    "name":"lynn",
    "fav_food":["apple"]
    }
}

print(player["friend"]["fav_food"])
print(player["name"])

player['fav_food']="apple"
player.pop("alive")
player["friend"]["fav_food"].append("banana")
print(player)

