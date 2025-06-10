from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.specials_page import SpecialsPage
from pages.cart_page import CartPage
import os


def before_all(context):
    context.playwright = sync_playwright().start()

    user_data_dir = os.path.join(os.getcwd(), "user_data")

    context.browser = context.playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
        viewport={"width": 1280, "height": 720},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36",
        slow_mo=500
    )

    context.page = context.browser.pages[0] if context.browser.pages else context.browser.new_page()

    context.login_page = LoginPage(context.page)
    context.specials_page = SpecialsPage(context.page)
    context.cart_page = CartPage(context.page)


def after_all(context):
    context.browser.close()
    context.playwright.stop()