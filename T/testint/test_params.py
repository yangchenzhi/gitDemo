import  pytest

@pytest.fixture(params=[1,2,3])
def longin1(request):
    data = request.param
    print(data)
    print("获取测试数据")
    return data



def test_case1 (longin1):
    print(longin1)
    print("测试用例1")
