"""  # 이건 이 세개의 쌍따음표 사이 부분 전부를 싹다 주석처리하는것!
from random import randint, random

user_choice = int(input("Choose number."))
pc_choice = randint(1,50) # I imported this 주석..

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer chose",pc_choice) 
"""

distance = 0

while distance < 20:
    print("I'm running", distance, "km")
    distance = distance + 1