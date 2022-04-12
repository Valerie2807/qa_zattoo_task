from helpers.generators import mail_generator, password_generator, gen_date_of_birth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fixture.application import Application


class TestTest():
    def setup_method(self):
        self.app = Application()

    def teardown_method(self):
        self.app.destroy()

    def test_signup_exist_email(self, login_='valerialetter@yandex.ru'):
        self.app.open_home_page()
        self.app.change_language_EN()
        self.app.sign_up_now()

        self.app.free_plan()
        login = self.app.driver.find_element(By.ID, "login")
        assert login.is_displayed()
        self.app.driver.find_element(By.ID, "login").send_keys(login_)
        self.app.driver.find_element(By.ID, "password").send_keys(password_generator())

        select = Select(self.app.driver.find_element_by_id('gender'))
        select.select_by_value('female')
        self.app.driver.find_element(By.ID, "domborn").click()
        self.app.driver.find_element(By.ID, "domborn").send_keys(gen_date_of_birth()[2])
        self.app.driver.find_element(By.ID, "monthborn").send_keys(gen_date_of_birth()[1])
        self.app.driver.find_element(By.ID, "yearborn").send_keys(gen_date_of_birth()[0])
        submit_button = self.app.driver.find_element_by_xpath("//*[@class='zrs_iBUnv zrs_LQBab']")
        self.app.driver.execute_script("arguments[0].click();", submit_button)
        self.app.driver.execute_script("window.scrollTo(0,10.5)")

        error_email = self.app.driver.find_element_by_xpath('//*[@data-soul="SIGNUP_FORM_EMAIL_ERROR"]').text
        assert error_email == 'Email address is already in use.'
