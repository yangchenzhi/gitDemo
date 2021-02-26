import  pytest
import yaml
from time  import  sleep
from selenium import webdriver


def  func(x) :
    return  x+1
@pytest.mark.parametrize('a,b',yaml.safe_load(open("./date.yaml")))
def test_answer(a,b):
    assert  func(a) == b





def test_ces ():
    print("开始")
    driver = webdriver.Chrome()
    driver.get("http://oa.tansun.com.cn:20080/oa/pages/indexnew.jsp")
    driver.implicitly_wait(3)

if __name__ == '__main__':
    pytest.main(["test_a.py"])


