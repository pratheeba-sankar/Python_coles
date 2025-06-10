class SpecialsPage:
    def __init__(self, page):
        self.page = page
        self.fruit_item = page.locator('text=Fruit & Vegetables')
        self.milk_item = page.locator('text=Dairy, Eggs & Fridge')
        self.add_to_cart_button = page.locator("text=Add")
        self.price_tags = page.locator("[data-testid='product-price']")

    def add_fruit_to_cart(self):
        self.fruit_item.click()
        self.page.wait_for_timeout(2000)
        self.add_to_cart_button.first.hover()
        self.add_to_cart_button.first.click()
        price_text = self.price_tags.first.text_content()
        return self.extract_price(price_text)

    def add_milk_to_cart(self):
        self.milk_item.click()
        self.page.wait_for_timeout(2000)
        self.add_to_cart_button.nth(1).click()
        price_text = self.price_tags.nth(1).text_content()
        return self.extract_price(price_text)

    def navigate_and_add_fruit_and_milk(self):
        self.add_fruit_to_cart()
        self.page.go_back()
        self.page.wait_for_timeout(2000)
        self.add_milk_to_cart()

    def extract_price(self, price_text):
        if price_text:
            return float(price_text.replace("$", "").strip())
        return 0.0