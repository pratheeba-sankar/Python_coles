class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_icon = page.locator("//*[@id='coles-targeting-header-container']/div[1]/div[2]/div/div[3]/div/button[2]")
        self.total_value = page.locator("//*[@id='drawer-footer-trolley-drawer']/div/div[1]/div/div/div")

    def open_cart(self):
        self.cart_icon.click()

    def get_total_price(self):
        total_value = self.total_value.inner_text()
        return float(total_value.replace("$", "").strip())