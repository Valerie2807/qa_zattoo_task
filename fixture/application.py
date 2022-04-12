from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}
        # self. driver.get('chrome://settings/clearBrowserData')
        # self.driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)


    def teardown_method(self, method):
        self.driver.quit()

    def finish_registration(self):
        self.driver.execute_script("window.scrollTo(0,10.5)")
        watch_for_free_button = self.driver.find_element_by_xpath("//*[ text() = 'Watch for free']")
        self.driver.execute_script("arguments[0].click();", watch_for_free_button)
        choose_channel = self.driver.find_element_by_xpath("//*[@title='ZDF']")
        self.driver.execute_script("arguments[0].click();", choose_channel)
        finish_button = self.driver.find_element_by_xpath("//*[ text() = 'Finish']")
        self.driver.execute_script("arguments[0].click();", finish_button)
        self.driver.find_element(By.LINK_TEXT, "Stream now").click()
        self.driver.find_element(By.CSS_SELECTOR, ".M2lWM").click()

    def free_plan(self):
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app-node"]/div/main/div[2]/div/table/thead/tr/th[2]/button').click()
        free_plan_button = self.driver.find_element_by_xpath("//*[ text() = 'Continue with FREE']")
        self.driver.execute_script("arguments[0].click();", free_plan_button)

    def sign_up_now(self):
        self.driver.find_element(By.XPATH, "//nav[2]/a[2]/span").click()
        self.driver.implicitly_wait(2)

    def change_language_EN(self):
        self.driver.find_element(By.CSS_SELECTOR, ".\\_1pHW-:nth-child(1) > .\\_3fImi").click()

    def log_out_from_account(self):
        self.driver.find_element(By.CSS_SELECTOR, ".jBbAK > .ZBzY1").click()

    def go_to_settings(self):
        self.driver.find_element(By.CSS_SELECTOR, ".SVB9z:nth-child(7) .XnvNe").click()

    def open_home_page(self):
        self.driver.get("https://zattoo.com/de")
        self.driver.find_element(By.XPATH, "//button[@id=\'onetrust-accept-btn-handler\']").click()

    def destroy(self):
        self.driver.quit()
