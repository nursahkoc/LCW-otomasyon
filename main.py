from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LCW:
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".sf-with-ul")  # 1
    CATEGORY_PAGE_2 = (By.CSS_SELECTOR, ".col-sm-4.pl-0.image_Box.visible-lg.visible-md") #1
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-item-wrapper")  # 2
    BEDEN_SECIMI = (By.CSS_SELECTOR, "a[size='M']")  # 0
    ADD_TO_CART = (By.ID, "pd_add_to_cart")
    CART_PAGE = (By.CSS_SELECTOR, ".header-bag-icon")
    MAIN_PAGE = (By.CSS_SELECTOR, ".header-logo")
    website = "https://www.lcwaikiki.com/tr-TR/TR"
    category = (By.CSS_SELECTOR, ".lazy-load-button")


    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/Users/nursahkoc/PycharmProjects/pythonProject/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[1].click()
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_2))[0].click()
        assert self.wait.until(ec.element_to_be_clickable(self.category)).is_displayed(), "daha fazla butonu yok"

        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[2].click()
        assert self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).is_displayed(), "add to cart butonu yok"

        self.wait.until(ec.presence_of_all_elements_located(self.BEDEN_SECIMI))[0].click()
        self.wait.until(ec.presence_of_element_located(self.ADD_TO_CART)).click()
        self.wait.until(ec.presence_of_element_located(self.CART_PAGE)).click()

        self.wait.until(ec.presence_of_element_located(self.MAIN_PAGE)).click()
        main_page_title = self.driver.title
        assert "LC Waikiki | İlk Alışverişte Kargo Bedava! - LC Waikiki" == main_page_title, "anasayfa değil"

        self.driver.quit()

    def tearDown(self):
        self.driver.quit()


LCW().test_navigate()
