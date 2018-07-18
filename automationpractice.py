import sys
import unittest
import time
from selenium import webdriver
from HTMLTestRunner_report import HTMLTestRunner

from testscripts.browser.browser import DriverBrowser
from testscripts.login.login import Login
from testscripts.logout.logout import Logout
from testscripts.forgot.forgot import ForgotPassword
from testscripts.search.search import Search
from testscripts.cart.cart import AddToCart
from testscripts.createaccount.createaccount import CreateAccount

import random
from random import randint

SERVER = None
EMAIL = None
PASSWORD = None
BROWSER = None

class Test1_Login(unittest.TestCase):#hapus unittest.TestCase to skip
    "Class to run tests against the AutomationpracticeTest Login"
    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = DriverBrowser(BROWSER)

    def test_Login_001(self):
        "AutomationpracticeTest Login - Valid data"
        self.startTime = time.time()
        self.driver.get(SERVER)
        driver, logging, status = Login(self.driver, EMAIL, PASSWORD)
        if "PASS" in status:
            print logging
            driver, logging, status = Logout(self.driver)
        else:
            self.fail(logging)
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    def test_Login_002(self):
        "AutomationpracticeTest Login - Invalid password"
        self.startTime = time.time()
        #self.driver.get(SERVER)
        driver, logging, status = Login(self.driver, EMAIL, "123")
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    def test_Login_003(self):
        "AutomationpracticeTest Login - Invalid email"
        self.startTime = time.time()
        #self.driver.get(SERVER)
        driver, logging, status = Login(self.driver, "xxx@mailinator.com", PASSWORD)
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    @classmethod
    def tearDownClass(self):
        "Tear down the test"
        self.driver.quit()

class Test2_Forgotpassword(unittest.TestCase):
    "Class to run tests against the AutomationpracticeTest Forgot Password"
    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = DriverBrowser(BROWSER)

    def test_Forgot_001(self):
        "AutomationpracticeTest Forgot - Valid email"
        self.startTime = time.time()
        self.driver.get(SERVER)
        driver, logging, status = ForgotPassword(self.driver, EMAIL)
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    def test_Forgot_002(self):
        "AutomationpracticeTest Forgot - Invalid email"
        self.startTime = time.time()
        #self.driver.get(SERVER)
        driver, logging, status = ForgotPassword(self.driver, "xxx@mailinator.com")
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    @classmethod
    def tearDownClass(self):
        "Tear down the test"
        self.driver.quit()

class Test3_Createanaccount(unittest.TestCase):
    "Class to run tests against the AutomationpracticeTest Create An Account"
    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = DriverBrowser(BROWSER)

    def _CreateAnAccount_001(self):
        "AutomationpracticeTest Create an account - Valid email"
        self.startTime = time.time()
        self.driver.get(SERVER)
        driver, logging, status = CreateAccount(self.driver, EMAIL)
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    def test_CreateAnAccount_002(self):
        "AutomationpracticeTest Create an account - Invalid email"
        self.startTime = time.time()
        self.driver.get(SERVER)
        driver, logging, status = CreateAccount(self.driver, EMAIL)
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    @classmethod
    def tearDownClass(self):
        "Tear down the test"
        self.driver.quit()

class Test4_Cart(unittest.TestCase):
    "Class to run tests against the AutomationpracticeTest Add to Cart"
    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = DriverBrowser(BROWSER)

    def test_Cart_001(self):
        "AutomationpracticeTest Cart"
        self.startTime = time.time()
        self.driver.get(SERVER)
        driver, logging, status = Search(self.driver, "dress")
        print logging
        driver, logging, status = AddToCart(self.driver)
        print logging
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    @classmethod
    def tearDownClass(self):
        "Tear down the test"
        self.driver.quit()

if __name__ == '__main__':
    command = len(sys.argv)
    if command == 5:
        BROWSER = sys.argv.pop()
        SERVER = sys.argv.pop()
        if "http" not in SERVER:
            SERVER = "http://"+SERVER
        PASSWORD = sys.argv.pop()
        EMAIL = sys.argv.pop()
    else:
        sys.exit("ERROR : Please check again your argument")
    HTMLTestRunner.main()
    #unittest.main()
