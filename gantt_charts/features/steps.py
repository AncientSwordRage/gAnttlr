# Disable the "wildcard import" warning so we can bring in all methods from
# course helpers and ui helpers
# pylint: disable=W0401

# Disable the "Unused import %s from wildcard import" warning
# pylint: disable=W0614

# Disable the "unused argument" warning because lettuce uses "step"
# pylint: disable=W0613
# pylint: disable=W0621
# pylint: disable=E0602


from lettuce import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nose.tools import eq_

@step('I am logged out')
def log_out(step):
    world.client.logout()

@step(r'I am logged in as "(\w*)"')
def log_in(step, name):
    can_login = world.client.login(username=name, password=name)
    if can_login:
        session_key = world.client.cookies['sessionid'].value
        world.browser.add_cookie({'name':'sessionid', 'value':session_key})
        world.browser.refresh()
        element = WebDriverWait(world.browser, 50).until(
            EC.presence_of_element_located((By.ID, "footer"))
            )
    else: 
        raise Exception("Could not login with those credentials")

@step(r'I find a link called "(.*?)" that goes to "(.*?)"$')
def find_link(step, link_name, link_url):
    elem = world.browser.find_element_by_xpath(r'//a[@href="%s"]' % link_url)
    eq_(elem.text, link_name)
