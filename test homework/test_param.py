import pytest
from selene import browser


@pytest.mark.parametrize("browse_conf",
                         [pytest.param("mob", marks=[pytest.mark.skip(reason="Test to mob")]), pytest.param("desk")],
                         indirect=True)
def test_mob(browse_conf):
    browser.open('https://github.com/')
    browser.element('a[href="/login"]').click()


@pytest.mark.parametrize("browse_conf", [pytest.param("desk", marks=[pytest.mark.skip(reason="Test to desk")]),
                                         pytest.param("mob")], indirect=True)
def test_desk(browse_conf):
    browser.open('https://github.com/')
    browser.element("div>button[aria-label='Toggle navigation']").click()
    browser.element('a[href="/login"]').click()
