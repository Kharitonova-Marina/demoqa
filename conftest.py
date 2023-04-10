import pytest
from selene.support.shared import browser


@pytest.fixture
def browse_conf(request):
    browser.config.hold_browser_open = False
    browser.open('https://github.com/')
    if (request.param == "mob"):
        browser.config.window_width = 390
        browser.config.window_height = 844
    elif (request.param == "desk"):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
