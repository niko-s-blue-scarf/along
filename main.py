import time
import os
class 主要():
    def __init__(self):
        self.分辨率=8
        self.画面 = [["、"] * self.分辨率 for _ in range(self.分辨率)]
    def 显像(self):
        self.清屏()
        for 指针 in self.画面:
            for 指针2 in 指针:
                print(指针2,end="")
            print()
    def 添加元素(self,坐标,元素):
        self.画面[坐标[0]][坐标[1]]=str(元素)
    def 清屏(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def 运行(self):
        while True:
            操作=input(">")
            try:
                exec(操作)
            except:
                print("执行失败")
            self.显像()
        """
        while True:
            self.显像()
            time.sleep(0.1)
        """
主体=主要()
主体.运行()