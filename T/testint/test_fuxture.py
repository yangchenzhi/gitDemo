import  pytest

@pytest.fixture()
def logon():
    print("登录")

    #获取token
    print("获取token")
    username = "tom"
    password = "123456"
    token = "173cm748ucmbsdel"
    # yield 关键字 可以做到激活fixtrue的teardown功能
    yield  [username,password,token]
    print("注销")

# 需要提前登录
def test_case1(logon):
    print('测试用例1')
    print(f"获取用户信息{logon}")


def test_case2(connectDB):
    print('测试用例2')

    # 需要提前登录
def test_case3(logon):
    print('测试用例3')
#用装饰器方式，实现提前登录
@pytest.mark.usefixtures("logon")
def test_case4():
    print('测试用例4')