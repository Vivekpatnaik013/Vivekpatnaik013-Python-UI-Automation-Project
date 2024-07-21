import pytest
@pytest.fixture(scope="class")
def setup():

    print("I will configure here ")
    yield
    print("*****Completed****")
@pytest.fixture()    
def dataLoad():
    print("User Profile data is created")
    return["vivek","patnaik","vivekpatnaik@yahoo.com"]

