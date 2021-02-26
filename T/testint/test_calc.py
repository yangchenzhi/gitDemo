from  python_code.cak import Caculator
import pytest
import  yaml

with open("./datas/calc.yaml") as f :

    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)


class TestCalc :

    def setup_class(self):
        print("类开始计算")
        #实例化计算器
        self.calc = Caculator()


    def teardown_class(self):
         print("类结束计算")


    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expec",add_datas,

          ids =myid
         # [
         #     (1,1,2),
         #     (0.1,0.1,0.2),
         #     (-1,-1,-2),
         #     [-1,-2,-3]
         #
         # ],
         #     ids = ['int','float','round','fail','negative']
                             )
    def test_add(self,a,b,expec):
        # 实例化计算器的类
        #calc = Caculator()
        #调用add方法
        result = self.calc.add(a,b)
        #浮点数判断，使用round保留两位小数
        if isinstance(result,float) :
            result = round(result,2)
        #得到的结果后做一个判断，需要写断言
        assert result == expec

    # 减法测试用例
    @pytest.mark.parametrize("a,b,expec",[(2,1,1),(3,2,1)])
    def test_sub(self,a,b,expec):
        #调用add的方法
        result = self.calc.sub(a,b)
        #浮点数判断，使用round保留两位小数
        if isinstance(result,float) :
            result = round(result,2)
        #得到的结果做一个断言
        assert  result == expec


    # 除法的测试用例

    # def test_add1(self):
    #     # 实例化计算器的类
    #    # calc = Caculator()
    #     #调用add方法
    #     result = self.calc.add(0.1,0.1)
    #     #得到的结果后做一个判断，需要写断言
    #     assert result == 0.2
    # def test_add2(self):
    #     # 实例化计算器的类
    #    # calc = Caculator()
    #     #调用add方法
    #     result = self.calc.add(-1,-1)
    #     #得到的结果后做一个判断，需要写断言
    #     assert result == -2