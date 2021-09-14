'''
input()
键盘输入:都是"11" ----> 11

猜数字:
需求:
   1.猜的数字是系统产生，不是自己定义
    2.键盘输入
     input("提示")
   3.循环
   while条件循环
   开始，结束，自增，任务
   4.判断
   单分支:if
   多分支:if
   多分支:if...elif....elif....elif....else
范围:0-150
如果输入大了，温馨提示:大了
如果输入大了，温馨提示:小了
正好猜中，恭喜你，猜中，本次猜的数字为xxxx.
'''
# 1.让系统产生一个随机数
# import random
#
# num = random.randint(0, 150)
# # 开始输入您要猜的数
# i = 0
#
# while i < 10:
#     # 任务:输入数据对比数据
#     number = input("请输入您要猜的数:")
#     number = int(number)
#
#     # 判断
#     if number > num:
#         print("大了！")
#     elif number < num:
#         print("小了")
#     else:
#         print("恭喜猜中，本次数字为:", num)
#         break  # 跳出循环
'''
起始金币为5000，每猜错一次就扣500，猜错十五次系统自动锁定，猜中加3000金币
'''
import random
num = random.randint(0,200)
coin = 0
print("当前余额为:",coin)
coin=input("请输入你要充值的金额:")
print("当前余额为:",coin)
coin = int(coin)
i = 0
while i <= 10:
    number = input("请输入数字:")
    number = int(number)
    if number > num:
        coin = coin-500
        print("错误,数额大了,剩余次数为:",10-i,"次","当前余额为:",coin)
    elif number < num:
        coin = coin-500
        print("错误,数额小了,剩余次数为:",10-i,"次","当前余额为:",coin)
    else:
        coin = coin + 3000
        print("恭喜答对，当前余额为:",coin)
        break
    i = i + 1
