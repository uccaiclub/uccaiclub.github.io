import random
ch = ['石头',   '剪子',   ' 布']
while True:
    player = input('你出什么?')️
    n = random.randint(0,2)
    computer = ch[n]
    print('电脑出' + computer)
    if player == computer:
        print('平')
    elif player == '石头' and computer == '剪子':
        print('你赢了')
    elif player == '剪子' and computer == '布'':
        print('你赢了')
    elif player == '布' and computer == '石头:
        print('你赢了')
        
    elif computer == '石头' and player == '剪子':
        print('你输了')
    elif computer == '剪子' and player == '布':
        print('你输了')
    elif computer == '布' and player == '石头':
        print('你输了')