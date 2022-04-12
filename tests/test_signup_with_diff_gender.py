import pytest
from helpers.generators import mail_generator, password_generator, gen_date_of_birth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fixture.application import Application
gender = ["female", "male", "other"]


class TestTest():
    def setup_method(self, method):
        self.app = Application()

    def teardown_method(self, method):
        self.app.destroy()

    @pytest.mark.parametrize("gender", gender)
    def test_happy_path_full_sign_up(self, gender):
        self.app.open_home_page()
        self.app.change_language_EN()
        self.app.sign_up_now()

        self.app.free_plan()
        login = self.app.driver.find_element(By.ID, "login")
        assert login.is_displayed()
        self.app.driver.find_element(By.ID, "login").send_keys(mail_generator())
        self.app.driver.find_element(By.ID, "password").send_keys(password_generator())

        select = Select(self.app.driver.find_element_by_id('gender'))
        select.select_by_value(gender)
        self.app.driver.find_element(By.ID, "domborn").click()
        self.app.driver.find_element(By.ID, "domborn").send_keys(gen_date_of_birth()[2])
        self.app.driver.find_element(By.ID, "monthborn").send_keys(gen_date_of_birth()[1])
        self.app.driver.find_element(By.ID, "yearborn").send_keys(gen_date_of_birth()[0])
        submit_button = self.app.driver.find_element_by_xpath("//*[@class='zrs_iBUnv zrs_LQBab']")
        self.app.driver.execute_script("arguments[0].click();", submit_button)
        self.app.driver.execute_script("window.scrollTo(0,10.5)")

        self.app.finish_registration()

        self.app.go_to_settings()
        self.app.log_out_from_account()
        self.app.driver.delete_all_cookies()
