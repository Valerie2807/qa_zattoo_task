from selenium.webdriver.common.by import By
from fixture.application import Application


class TestTest():
    def setup_method(self):
        self.app = Application()

    def teardown_method(self):
        self.app.destroy()

    def test_happy_path_full_sign_up(self):
        self.app.open_home_page()
        self.app.change_language_EN()
        self.app.sign_up_now()

        self.app.free_plan()
        login = self.app.driver.find_element(By.ID, "login")
        assert login.is_displayed()
        submit_button = self.app.driver.find_element_by_xpath("//*[@class='zrs_iBUnv zrs_LQBab']")
        self.app.driver.execute_script("arguments[0].click();", submit_button)

        error_email = self.app.driver.find_element_by_xpath('//*[@data-soul="SIGNUP_FORM_EMAIL_ERROR"]').text
        assert error_email == 'Please enter a valid email address'
        error_password = self.app.driver.find_element_by_xpath('//*[@data-soul="SIGNUP_FORM_PASSWORD_ERROR"]').text
        assert error_password == 'Please enter a password'
        error_gender = self.app.driver.find_element_by_xpath('//*[@data-soul="SIGNUP_FORM_GENDER_ERROR"]').text
        assert error_gender == 'Please select a gender'
        error_dob = self.app.driver.find_element_by_xpath('//*[@data-soul="SIGNUP_FORM_BIRTH_DATE_ERROR"]').text
        assert error_dob == 'Please enter your date of birth'
