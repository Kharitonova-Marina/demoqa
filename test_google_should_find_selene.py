from selene.support.shared import browser
from selene import be, have


browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_searching(preparations):
    browser.open('https://www.google.com')
    browser.element('[name="q"]').should(be.blank).type('артольрапвчрплпанверкпиамьпаоеикпвыввфсфыфычфыч').press_enter()
    browser.element('[id="center_col"]').should(have.text('По запросу артольрапвчрплпанверкпиамьпаоеикпвыввфсфыфычфыч ничего не найдено.'))
