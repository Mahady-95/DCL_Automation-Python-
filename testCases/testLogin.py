import time
from pageObjects.LoginPage import LoginPage


class Test001Login:
    baseUrl = "https://sqa.deepchainlabs.com/login"
    username = "admindcl@gmail.com"
    password = "adminpassword"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        time.sleep(3)
        if act_title == "Deepchain Labs | Login":
            assert True
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_LoginTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        print("Login clicked")
        time.sleep(5)
        self.driver.save_screenshot(".\\screenshots\\" + "test_LoginTitle.png")
        time.sleep(5)
        self.driver.close()
    def test_AdminDashboard(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        dash_URL=self.driver.current_url
        print(dash_URL)
        act_dashboard_titile = self.driver.title
        if act_dashboard_titile=="Deepchain Labs | Admin | Dashboard":
            assert  True
            print("Admin DashBoard")
        else:
            assert False

        self.driver.save_screenshot(".\\screenshots\\" + "test_AdminDashboard.png")

        self.lp.clickAdmin()
        print("admin clicked")
        time.sleep(3)
        self.lp.clickLogout()
        print("logout clicked")
        time.sleep(3)
        self.driver.close()

    def testAdminBlogList(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.clickBlog()
        print("Blog clicked")
        time.sleep(4)
        act_url = self.driver.current_url
        print(act_url)
        expected_url = "https://sqa.deepchainlabs.com/admin/blogs"
        if act_url == expected_url:
            assert True
            print("This is Deepchain Labs | Admin | Blogs")
        else:
            assert False

        self.driver.save_screenshot(".\\screenshots\\" + "testAdminBlogList.png")
        self.lp.clickAdmin()
        time.sleep(3)
        self.lp.clickLogout()
        time.sleep(3)
        time.sleep(3)
        self.driver.close()

    def testCreateNewBlog(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.clickBlog()
        time.sleep(5)
        self.lp.clickCreateNewBlog()
        print("clicked CreateNewBlog")
        time.sleep(5)
        createBlogURL = self.driver.current_url
        print(createBlogURL)
        if createBlogURL=="https://sqa.deepchainlabs.com/admin/blogs/post":
            assert True
            print("This is create new blog page")
        else:
            assert False

        self.driver.save_screenshot(".\\screenshots\\" + "testCreateNewBlog.png")

        self.lp.fillTitle()
        print("Title field filled")
        time.sleep(2)
        self.lp.fillTags()
        print("Tags field filled")
        time.sleep(2)
        self.lp.fillContent()
        print("concent field filled")
        time.sleep(2)

        self.lp.selectDropDown()
        print("Drop-Down selected")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.lp.readTime()
        print("Read time given")
        time.sleep(2)

        self.lp.clickFileUpload()
        print("Image uploaded")
        time.sleep(2)

        self.lp.clickPublish()
        print("ok publish")
        time.sleep(2)
        # self.driver.get("https://sqa.deepchainlabs.com/admin/blogs")
        # time.sleep(3)
        url=self.driver.current_url
        print(url)
        time.sleep(3)

        self.driver.refresh()
        time.sleep(3)
        self.lp.searchBlog()
        time.sleep(5)
        self.driver.save_screenshot(".\\screenshots\\" + "BlogSection.png")
        print("Newly create blog is verified by search")
        time.sleep(3)

        self.driver.get("https://sqa.deepchainlabs.com/blogs")
        self.driver.refresh()
        time.sleep(2)
        self.lp.searchBlog()
        time.sleep(5)
        print("Active blogs is displayed in Block Section Page")
        time.sleep(5)
        self.driver.close()


