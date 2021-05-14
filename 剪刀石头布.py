# coding=utf-8
#2021-05-15 06:41
@ Author:xyj
import random
# 获胜次数
win_times = 0
number = 0
choice = ['0','1','2']
punches=['剪刀','石头','布']
while win_times <= 1:
  print('第'+str(win_times+1)+'局')
  while True:
    player = input('请输入：剪刀(0)  石头(1)  布(2):')
    if player in choice:
      break
    else:
      print('输入有误，请重输！')
  number+=1
  computer = random.choice(choice)
  print("你出了：",punches[int(player)])
  print("电脑出了：",punches[int(computer)])
  if player == choice[choice.index(computer)-1]:
    print('输了，不要走，洗洗手接着来，决战到天亮')
  elif player == computer:
    print('平局，要不再来一局')
  else:
    win_times += 1
    print('获胜，哈哈，你太厉害了')
print("共出了"+str(number)+'手')
