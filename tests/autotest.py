import os

from selene import browser, command, have
from selene.support.conditions.be import not_


def test_fill_and_send_form(preparations):
    browser.open('https://demoqa.com/automation-practice-form')

    # region DELETE ADVERTISEMENT
    browser.execute_script('document.querySelector("footer").remove()')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.execute_script('document.querySelector("#RightSide_Advertisement").remove()')
    # endregion

    # region FILL FORM
    browser.element('#firstName').type('Marina')
    browser.element('#lastName').type('Kharitonova')
    browser.element('#userEmail').type('tests@testmail.com')
    browser.element("[for='gender-radio-2']").click()
    browser.element('#userNumber').type('9112223344')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select > option[value="2"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select > option[value="1991"]').click()
    browser.element('div[aria-label*="March 7th"]').click()

    browser.element('#subjectsInput').type('ma').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(
        os.path.normpath(os.getcwd() + os.sep + os.pardir) + '/resources/picture.jpeg')
    browser.element('#currentAddress').type('Russia')

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').perform(command.js.click)
    # endregion

    # region ASSERTIONS FILL FORM
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('//table/tbody/tr[1]/td[2]').should(have.text('Marina Kharitonova'))
    browser.element('//table/tbody/tr[2]/td[2]').should(have.text('tests@testmail.com'))
    browser.element('//table/tbody/tr[3]/td[2]').should(have.text('Female'))
    browser.element('//table/tbody/tr[4]/td[2]').should(have.text('9112223344'))
    browser.element('//table/tbody/tr[5]/td[2]').should(have.text('07 March,1991'))
    browser.element('//table/tbody/tr[6]/td[2]').should(have.text('Maths'))
    browser.element('//table/tbody/tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//table/tbody/tr[8]/td[2]').should(have.text('picture.jpeg'))
    browser.element('//table/tbody/tr[9]/td[2]').should(have.text('Russia'))
    browser.element('//table/tbody/tr[10]/td[2]').should(have.text('NCR Delhi'))
    # endregion

    # region CLOSE
    browser.element('#closeLargeModal').perform(command.js.click)
    browser.element('#example-modal-sizes-title-lg').should(not_.enabled)
    # endregion
