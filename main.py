import time
class 主要():
    def __init__(self):
        self.分辨率=8
        self.画面 = [["、"] * self.分辨率 for _ in range(self.分辨率)]
    def 显像(self):
        print("\n"*(self.分辨率*4))
        for 指针 in self.画面:
            for 指针2 in 指针:
                print(指针2,end="")
            print()
    def 运行(self):
        while True:
            self.显像()
            time.sleep(0.1)
主体=主要()
主体.运行()