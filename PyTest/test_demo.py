import pytest
@pytest.mark.regression
def test_firstTest():
    print("hello World")
def test_test2():
    print("2nd test")

def test_test3():
    print("hello hi")

def test_SecondCheckLogin():
    UserName="Vivek"
    Password="@123"
    assert Password=="@123", "Login is not true"
@pytest.mark.smoke
def test_productAdd():
    product="honda"
    print(product)



