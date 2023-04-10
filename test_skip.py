import pytest
from selene import browser


@pytest.fixture(params=['desk', 'mob'])
def setup_window(request):
    if request.param == "desk":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com/')
    if request.param == "mob":
        browser.config.window_width = 390
        browser.config.window_height = 844
        browser.open('https://github.com/')


def test_desktop(setup_window):
    if setup_window == 'desk':
        browser.element('[href="/login"]').click()
    elif setup_window == 'mob':
        pytest.skip()


def test_mobile(setup_window):
    if setup_window == 'mob':
        browser.element("div>button[aria-label='Toggle navigation']").click()
        browser.element('[href="/login"]').click()
    elif setup_window == 'desk':
        pytest.skip()
