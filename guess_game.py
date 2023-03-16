import random

# 1.增加勝負判斷
# 2.猜對時顯示猜了幾次
# 3.提示區間


x = random.randint(1, 100)

win = False
start, end = 1, 100

for i in range(5):
    y = eval(input(f'[{i+1}/5]請猜一個數字(1~50之間):'))
    if x == y:
        win = True
        break

    if x > y:
        start = y
        print(f'猜大一點({start}~{end})')

    else:
        if y < end:
            end = y
        print(f'猜小一點({start}~{end})')
if win:
    print(f'恭喜過關!共猜了{i+1}次')
else:
    print(f'遊戲結束!答案為:{x},共猜了{i+1}次')
