player = {               # 딕셔너리.
    'name': 'nico',
    'age' : 12,
    'alive' : True,
    'fav_food' : ["pizza","hamburger"]
}

print(player.get('age'))      # 12 출력
print(player.get('fav_food')) # ["pizza","hamburger"] 출력
print(player['fav_food'])
player.pop('age')
print(player)
player['xp'] = 1500
print(player)
player['fav_food'].append("asdf")
print(player.get('fav_food'))
print(player['fav_food'])
print(player)
