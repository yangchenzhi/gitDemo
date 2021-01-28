class Animal :
    """"
    比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
    """

    Name = None
    Colour = None
    Age = None
    Sex = None

    def __init__(self,Name,Colour,Age,Sex):
        self.Name = Name
        self.Colour = Colour
        self.Age = Age
        self.Sex = Sex


    def call (self):
        print("我会叫的")


    def run (self):
        print("我会跑的")

