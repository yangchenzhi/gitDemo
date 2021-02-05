import  pytest
import yaml


def  func(x) :
    return  x+1
@pytest.mark.parametrize('a,b',yaml.safe_load(open("./date.yaml")))
def test_answer(a,b):
    assert  func(a) == b


if __name__ == '__main__':
    pytest.main(["test_a.py"])