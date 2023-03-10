import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def preparations():
    browser.config.hold_browser_open = False
    browser.config.window_width = 1920
    browser.config.window_height = 1080
