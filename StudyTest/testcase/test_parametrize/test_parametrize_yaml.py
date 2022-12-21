
import pytest

from utils.read_data import get_data



# 参数为字典
@pytest.mark.parametrize("args", get_data['heros_name'])
def test_parametrize_03(args):
    print(args)
