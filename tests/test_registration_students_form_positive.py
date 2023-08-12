from selene import browser, be, have
import os

first_name = 'Ivan'
last_name = 'Ivanov'
email = 'qwerty@mail.ru'
phone = '1234567890'
current_address = 'CUrrent aDDress 12a Here'


def test_registration_students_form_positive():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').should(be.blank).type(first_name)
    browser.element('[id="lastName"]').should(be.blank).type(last_name)
    browser.element('[id="userEmail"]').should(be.blank).type(email)
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type(phone)
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]>option[value="1"]').click()
    browser.element('[class="react-datepicker__year-select"]>option[value="1999"]').click()
    browser.element('.react-datepicker__day--001').click()
    browser.element('[id="subjectsInput"]').click().type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('../data/test.png'))
    browser.element('[id="currentAddress"]').type(current_address)
    browser.element('[id="react-select-4-input"]').should(be.not_.enabled)
    browser.element('[id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').should(be.enabled).type('Delhi').press_enter()
    browser.element('[id="submit"]').press_enter()
    #     Проверка итоговой таблицы
    browser.element('[class="table-responsive"]').should(have.text(
        f"{first_name} {last_name}"
        and f"{email}"
        and f"Male"
        and f"{phone}"
        and "01 February,1999"
        and "Maths"
        and "Reading, Music"
        and "test.png"
        and "CUrrent aDDress 12a Here"
        and "NCR Delhi"
    ))

