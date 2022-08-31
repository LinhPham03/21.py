
from random import randint
check = 0
current_sum=0
#0= human /// 1= computer
while current_sum <= 21:
    print("Tổng: ", current_sum)
    player_choice= input('Nhập số bạn muốn nhập: ') 
    if player_choice == '1' or player_choice == '2' or player_choice =='3':
        current_sum+= int(player_choice)
        if current_sum > 21:
            print(current_sum)
            print('Bạn đã thua cuộc')
            check = 1 
        else:
            print('Đến lượt máy')
            computer_choice = randint(1,3)
            print("Computer pick :", computer_choice)
            current_sum+= computer_choice
            if current_sum> 21:
                print(current_sum)
                print('Bạn đã thắng')
                check = 1 
            else: 
                print('Đến lượt bạn')
    else:
        print('Nhập lại số! Hãy nhập 1/2/3')
    if check == 1: 
        again = input('Bạn có muốn chơi nữa không (y/n): ')
        if again[0]== "y":
            continue
        else:
            break