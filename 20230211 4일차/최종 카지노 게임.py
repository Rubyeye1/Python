""" """# 이건 이 세개의 쌍따음표 사이 부분 전부를 싹다 주석처리하는것!
from random import randint, random

print("Welcome to Python Casino")

pc_choice = randint(1,50)

playing = True

while playing:
    user_choice = int(input("Choose number."))
    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower! Computer chose")
    elif user_choice < pc_choice:
        print("Higher! Computer chose") 

