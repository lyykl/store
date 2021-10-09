from threading import Thread
import time
egg=0
class cook(Thread):
    username=""
    num=0
    def run(self) -> None:

        global egg
        while True:
            if egg<500:
                egg=egg+1
                print(self.name,"成功做了",egg,"个蛋挞")
                time.sleep(0.1)
            else:
                print(self.name,"总共做了",egg,"个蛋挞")
                time.sleep(3)
                print("休息3秒")
                break


class customer(Thread):
    username=""
    num1=0
    money = ""
    def run(self) -> None:

        while True:
            if self.money > 0:
                self.money=self.money -2
                self.num1=self.num1+1
                print(self.username,"买了",self.num1,"个蛋挞","还剩",self.money,"￥")
                time.sleep(0.3)
            else:
                print(self.username,"总共买了",self.num1,"个蛋挞")
                break












p1=cook()
p2=cook()
p3=cook()
p4=customer()
p5=customer()
p6=customer()
p7=customer()
p8=customer()
p9=customer()
p4.money=3000
p5.money=3000
p6.money=3000
p7.money=3000
p8.money=3000
p9.money=3000
p1.name="老头"
p2.name="刘傻子"
p3.name="闫帅哥"
p4.username="小老头"
p5.username="孙孙"
p6.username="刘傻"
p7.username="孙傻"
p8.username="闫帅"
p8.username="闫凯龙无敌帅"


p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()
