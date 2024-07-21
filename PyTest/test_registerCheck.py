
import pytest
@pytest.mark.usefixtures("setup")
class myfixture:
    def test_myTest(self,setup):
        print("After configure i will execute MyTest")
    def test_Sanity(self,setup):
        print("this is sanity")
    def test_regression(self,setup):
        print("this is regression")