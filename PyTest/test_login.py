import logging
import pytest


def test_logintestDemo():


    logerObj=logging.getLogger(__name__)
    fileObj=logging.FileHandler('logFile.log')
    logerObj.addHandler(fileObj)
    formatterObj=logging.Formatter("%(asctime)%s :%(levelname)%s :%(name)s :%(message)%s")
    fileObj.setFormatter(formatterObj)
    logerObj.setLevel(logging.DEBUG)


    logerObj.debug("Debugging TestCase")
    logerObj.info("TestCse Information")
    logerObj.warning("Warning for testCase")
    logerObj.error("fatal error")
    logerObj.critical("Critical error")