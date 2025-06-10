from behave import given, when, then
from utils.excel_writer import write_to_excel

@given("I have launched the Coles website")
def step_impl(context):
    context.page.goto("https://www.coles.com.au/")

@given("I have a valid Coles account")
def step_impl(context):
    context.email = "pratheebasydney@gmail.com"
    context.password = "159765@TCS"

@when("I login to the Coles account")
def step_impl(context):
    context.login_page.login(context.email, context.password)
    context.login_successful = context.login_page.is_login_successful()

@then("I should see a login result")
def step_impl(context):
    context.login_result = "Login successful" if context.login_successful else "Login failed"

@then("I write the login result to the excel file")
def step_impl(context):
    write_to_excel("Login Functionality", context.login_result, "")

@when("I navigate to the specials section and add fruit and milk to the cart")
def step_impl(context):
    print("commented")
    context.fruit_price = context.specials_page.add_fruit_to_cart()
    context.milk_price = context.specials_page.add_milk_to_cart()
    print(f"Fruit Price: {context.fruit_price}")
    print(f"Milk Price: {context.milk_price}")

@when("I view the cart and get the total price")
def step_impl(context):
    context.cart_page.open_cart()
    context.total_price = float(context.cart_page.get_total_price())


@then("I verify the total price is correct")
def step_impl(context):
    expected_total = round(context.fruit_price + context.milk_price, 2)
    actual_total = round(context.total_price, 2)
    print(f"Fruit Price: ${context.fruit_price:.2f}")
    print(f"Milk Price: ${context.milk_price:.2f}")
    print(f"Expected Total: ${expected_total:.2f}")
    print(f"Actual Total from Cart: ${actual_total:.2f}")
    assert abs(expected_total - actual_total) < 0.01, f"Expected ${expected_total:.2f}, got ${actual_total:.2f}"

@then("I write the total price to the excel file")
def step_impl(context):
    #login_result = getattr(context, "login_result", "N/A")
    write_to_excel("Total Value", context.login_successful, f"${context.total_price:.2f}")

