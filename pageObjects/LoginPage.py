import time
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller


class LoginPage:
    text_username_id = "emailField"
    text_password_id = "passwordField"
    button_login_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/div[3]/div[1]"
    link_admin_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]"
    button_blog_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
    link_createblog_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]"
    txt_blogtitle_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    txt_tags_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
    txt_content_xpath="//div[@class='ql-editor ql-blank']"
    dropdown_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/input[1]"
    file_upload_xpath="//label[@role='presentation']"
    read_time_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/input[1]"
    button_publish_xpath ="//button[normalize-space()='Publish']"
    search_blog_xpath = "//input[@placeholder='Search']"
    button_logout_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[3]/span[1]"


    def __init__(self, driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.text_username_id).clear()
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickAdmin(self):
        self.driver.find_element(By.XPATH, self.link_admin_xpath).click()

    def clickBlog(self):
        self.driver.find_element(By.XPATH, self.button_blog_xpath).click()

    def clickCreateNewBlog(self):
        self.driver.find_element(By.XPATH, self.link_createblog_xpath).click()

    def fillTitle(self):
        self.driver.find_element(By.XPATH, self.txt_blogtitle_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_blogtitle_xpath).send_keys("Etherenium-2")
    def fillTags(self):
        self.driver.find_element(By.XPATH, self.txt_tags_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_tags_xpath).send_keys("Crypto")
        time.sleep(2)
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def fillContent(self):
        self.driver.find_element(By.XPATH, self.txt_content_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_content_xpath).send_keys(" Popular Digital Currency")
    def selectDropDown(self):
        drp=self.driver.find_element(By.XPATH, self.dropdown_xpath).click()
        sel="//li[normalize-space()='Blockchain']"
        option_to_select = self.driver.find_element(By.XPATH, sel)
        option_to_select.click()

    def clickFileUpload(self):
        fileupload = self.driver.find_element(By.XPATH, self.file_upload_xpath)
        fileupload.click()
        time.sleep(5)
        keyboard = Controller()
        keyboard.type("C:\\Users\\User\\Documents\\Photos\\immg.jpg")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
    def readTime(self):
        self.driver.find_element(By.XPATH, self.read_time_xpath).send_keys("3")

    def clickPublish(self):
        publish=self.driver.find_element(By.XPATH, self.button_publish_xpath)
        if publish.is_enabled:
            print("enable")
            publish.click()
            time.sleep(5)
        else:
            print("not enabled")
    def searchBlog(self):
        search=self.driver.find_element(By.XPATH, self.search_blog_xpath)
        search.click()
        search.send_keys("Etherenium")
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
