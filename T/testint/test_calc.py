from  python_code.cak import Caculator
class TestCalc :

    def test_add(self):
        # 实例化计算器的类
        calc = Caculator()
        #调用add方法
        result = calc.add(1,1)
        #得到的结果后做一个判断，需要写断言
        assert result == 2

    def test_add1(self):
        # 实例化计算器的类
        calc = Caculator()
        #调用add方法
        result = calc.add(0.1,0.1)
        #得到的结果后做一个判断，需要写断言
        assert result == 0.2
    def test_add2(self):
        # 实例化计算器的类
        calc = Caculator()
        #调用add方法
        result = calc.add(-1,-1)
        #得到的结果后做一个判断，需要写断言
        assert result == -2