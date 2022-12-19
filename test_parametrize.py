import pytest


@pytest.mark.parametrize("a,b,final",[(2,3,5),(3,5,7)])
def test_fxture_param(a,b,final):
    assert a+b ==final
# def testlogin(demo_fxture_param):
#     print("login succesful")