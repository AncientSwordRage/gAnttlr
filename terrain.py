# pylint: disable=W0611

from lettuce import before, after, world
from selenium import webdriver
from django.test import Client
import lettuce_webdriver.webdriver
from time import time

@before.all
def setup_browser():
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.dns.disableIPv6', True)
    world.browser = webdriver.Firefox(profile)
    world.browser.implicitly_wait(10)
    world.client = Client(HTTP_USER_AGENT='Mozilla/5.0')

@after.all
def close_browser(*args, **kwargs):
    world.browser.close()

@before.each_feature
def start_feature_time(feature):
    world.feature_start = time()

@after.each_feature
def end_feature_time(feature):
    world.feature_end = time()
    world.feature_duration = world.feature_end-world.feature_start
    print("Feature: '{0}' took {1:.2f} seconds to run".format(feature.name, world.feature_duration))

@before.each_scenario
def start_scenario_time(scenario):
    world.scenario_start = time()

@after.each_scenario
def end_scenario_time(scenario):
    world.scenario_end = time()
    world.scenario_duration = world.scenario_end-world.scenario_start
    print("Scenario: '{0}' took {1:.2f} seconds to run".format(scenario.name, world.scenario_duration))
