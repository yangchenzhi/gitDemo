from  zuoye.zuoye_1 import Animal





class Cat (Animal):

    hair = None

    def __init__(self,hair):

        self.hair = hair
        super().__init__("猫","黑","1岁","母")




    def catches_mice (self):
        print("我会捉老鼠")


    def call (self):
        print("我会喵叫叫")



if __name__ == '__main__':
    cat = Cat("Short_hair")
    print(f"我的毛发是{cat.hair}，我的年龄是{cat.Age},我的性别是{cat.Sex},我的名字是{cat.Name},我的颜色是{cat.Colour},")

    cat.catches_mice()
    cat.call()