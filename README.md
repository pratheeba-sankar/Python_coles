
# Coles Automation Framework

This is a simple test automation framework using:

- Behave : for BDD test execution
- Playwright: for browser automation
- Allure: for reporting
- OpenPyXL: for writing results to Excel


## Requirements

Install dependencies:

pip install -r requirements.txt
playwright install



## How to Run Tests

Run tests and generate Allure results:

behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results


## Excel Output

After running tests, results will be written to: output.xlsx




