from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\\AnshuRahul\\Selenium\\Selenium-python\\\chromedriver_win32\\chromedriver.exe")

    # Below code needs to be changed for multiple browsers
    # def setup(browser):
    #   if browser == 'chrome':
    #      driver = webdriver.Chrome(
    #         executable_path="C:\\Users\\\AnshuRahul\\Selenium\\Selenium-python\\\chromedriver_win32\\chromedriver.exe")
    #    print("Launching Chrome Browser")

    # elif browser == 'firefox':
    #   driver=webdriver.Firefox(
    #      executable_path="C:\\Users\\\AnshuRahul\\Selenium\\Selenium-python\\geckodriver-v0.27.0-win64\\geckodriver.exe")
    # print("Launching Firefox browser")

    # else
    # driver=webdriver.ie()

    return driver


# def pytest_addoption(parser): # This will get the value from CLI/hooks
# parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):
#   return request.config.getoption("--browser") #This will return the browser value to setup method

# command to run in specific browser - pytest -v -s testCases/test_Login.py --browser chrome
# command to run parallel test cases. here n is number of test cases- pytest -v -s -n=2 testCases/test_Login.py --browser chrome

########## Pytest HTML Report #######################
# pytest -v -s --html=Reports\report.html testCases/test_Login_ddt.py


# This is a hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['project name'] = 'Test Python App'
    config._metadata['Module name'] = 'Customers'
    config._metadata['Tester'] = 'Rahul'


# This ia a hook for delete/modify Environment info to HTML Report
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
#    metadata.pop["JAVA_HOME", None]
#    metadata.pop["Plugins", None]
