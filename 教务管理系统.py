'''
1.随机点名
2.随机生成处罚
技术选型:
    容器类型:int str double boolean
    元组:(1,5,7,4),不允许做任何修改
    列表:[1,5,7,8,10,41] 可以做任何操作
    字典:{}
    pop():默认移除列表最后一项数据

    列表的几个方式:
    append()
    remove pop()
    直接赋值
    直接打印即可
    len()取长度
'''
#import random
# names = ["1","2","3","4","5","6"]
#
# names.append("8")
# names.remove("")
# print(names)
# print("------------------------欢迎来到教务系统--------------------")
# while True:
#   chose=input("教务系统:1.随机点名 2.随机处罚:")
#   if chose == "1":
#     index = random.randint(0,len(names)-1)
#     print(names[index])
#   elif chose ==  "2":
#     num= random.randint(0,500)
#     print(num)
#   elif chose == "q" or chose == "Q":
#     print("欢迎下次使用")
#     break
#   else:
#     print("输入非法")
names = ["A","B","C","D"]
while True:
    options = input("请输入你的选择:")
    if options == "A":
        print("不是我哦!")
    elif options == "B":
        print("讨厌,不是人家啦~")
    elif options == "C":
        print("哼,这么半天才选到我！")
        break
    elif options == "D":
        print("为什么要选择人家呐~")
    else:
        print("只能先选其中之一哦！")
