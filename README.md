# Web Automation Pytest Project

## Description

Fully functional web automation framework written in Python using the Pytest testing framework automating OrangeHRM software!


## Overview

**WebAutomationPytest** is a web automation testing framework built with [Pytest](https://docs.pytest.org/) and [Selenium](https://www.selenium.dev/).  
It follows the **Page Object Model (POM)** design pattern to keep test cases clean, reusable, and easy to maintain.  

The framework is designed to:  
- Automate end-to-end web UI tests.  
- Provide detailed, interactive test reports with [Allure](https://allurereport.org/).  
- Support scalability for adding new test cases and page components.  
- Run locally or be integrated into CI/CD pipelines (e.g., GitHub Actions, Jenkins).  

This project is ideal for:  
- Demonstrating automation skills in a portfolio project.
- QA engineers learning automation with Python.  
- Teams needing a structured, maintainable Selenium + Pytest setup.
## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Live Tests](#live-tests)
- [Project Structure](#project-structure)

## Prerequisites

Before installing, make sure you have the following:

- [Python](https://www.python.org/downloads/) (latest version recommended)
- [pip](https://pip.pypa.io/en/stable/installation/) (comes with Python)
- [Allure commandline](https://docs.qameta.io/allure/#_get_started) (for generating and viewing reports)

To verify installation:
```bash
python --version
pip --version
allure --version
```
- An IDE or code editor of your choice:
  - [PyCharm](https://www.jetbrains.com/pycharm/) (recommended)
  - [VS Code](https://code.visualstudio.com/) (with extensions)
  - Or any other Python-compatible IDE

> [!NOTE]
> Make sure to install Python first before running pip.
> If Allure is not recognized as a command, you may need to add it to your system PATH.

## Installation

Clone the repository:
```bash
git clone https://github.com/noah-jones-dev/WebAutomationPytest.git
cd WebAutomationPytest
```
Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate   # On Linux / macOS
.venv\Scripts\activate      # On Windows
```
> [!NOTE]
> Using a virtual environment ensures your dependencies don’t conflict with global Python packages.

Install required dependencies:
```bash
pip install pytest selenium allure-pytest
```

## Running Tests

### To run tests, run the following commands:

Run all tests
```bash
  pytest
```
Run all tests and save Allure results:
```bash
  pytest --alluredir=reports/results
```
Generate and view the report:
```bash
allure serve reports/results
```
Export the report to share:
```bash
allure generate reports/results -o reports/html --clean
allure open reports/html
```



## Live Tests

![TestDashboard](https://github.com/user-attachments/assets/92d16e2c-d016-451a-8865-066b4ede1b37)

![TestPunchIn](https://github.com/user-attachments/assets/84bc08c8-ae38-4cb2-b4a0-33ef5e5fec1d)

## Project Structure

- [framework/](framework/) - Reusable components, helpers, and custom fields for tests
  - [fields/](framework/fields/) - Custom field objects
    - [base_field.py](framework/fields/base_field.py) - Base class for all field types
    - [button_field.py](framework/fields/button_field.py) - Button field types
    - [dropdown_field.py](framework/fields/dropdown_field.py) - Dropdown field types
    - [link_field.py](framework/fields/link_field.py) - Link field types
    - [navigation_field.py](framework/fields/navigation_field.py) - Navigation field types
    - [static_field.py](framework/fields/static_field.py) - Static text field types
    - [table_field.py](framework/fields/table_field.py) - Table field types
    - [textbox_field.py](framework/fields/textbox_field.py) - Textbox field types
  - [helpers/](framework/helpers/) - Helper classes like wait utilities, verifications
    - [verifications/](framework/helpers/verifications/) - Verification objects for field types
      - [verify_base.py](framework/helpers/verifications/verify_base.py) - Verification class for base fields
      - [verify_button.py](framework/helpers/verifications/verify_button.py) - Verification class for button fields
      - [verify_cell.py](framework/helpers/verifications/verify_cell.py) - Verification class for cells
      - [verify_dropdown.py](framework/helpers/verifications/verify_dropdown.py) - Verification class for dropdown fields
      - [verify_link.py](framework/helpers/verifications/verify_link.py) - Verification class for link fields
      - [verify_static.py](framework/helpers/verifications/verify_static.py) - Verification class for static text fields
      - [verify_textbox.py](framework/helpers/verifications/verify_textbox.py) - Verification class for textbox fields
    - [wait_utilities/](framework/helpers/wait_utilities/) - Utility objects for waits
      - [wait_helper.py](framework/helpers/wait_utilities/wait_helper.py) - Utility methods for waiting for loads
    - [window_utilities/](framework/helpers/window_utilities/) - Utility objects for window handles
      - [window_helper.py](framework/helpers/window_utilities/window_helper.py) - Utility methods for switching window handles

- [pages/](pages/) - Page Object Model (POM) classes representing different pages
  - [performance_pages/](pages/performance_pages/) - Pages belonging to Performance area
    - [employee_reviews_page.py](pages/performance_pages/employee_reviews_page.py) - Employee Review Page object
    - [my_reviews_page.py](pages/performance_pages/my_reviews_page.py) - My Review Page object
    - [performance_base_page.py](pages/performance_pages/performance_base_page.py) - Performance Base Page object
  - [time_pages/](pages/time_pages/) - Time-related pages
    - [punch_in_out_page.py](pages/time_pages/punch_in_out_page.py) - Punch In/Out Page object
    - [time_base_page.py](pages/time_pages/time_base_page.py) - Time Base Page object
  - [base_page.py](pages/base_page.py) - Universal Base Page object
  - [dashboard_page.py](pages/dashboard_page.py) - Dashboard Page object
  - [login_page.py](pages/login_page.py) - Login Page object

- [reports/](reports/) - Stores test results and Allure reports
  - [results/](reports/results/) - Test results

- [tests/](tests/) - Contains all automated test cases
  - [conftest.py](tests/conftest.py) - Base Test configuration
  - [dashboard_test.py](tests/dashboard_test.py) - Dashboard functionality tests
  - [punch_in_out_test.py](tests/punch_in_out_test.py) - Punch In/Out functionality tests

- [tips/](tips/) - Running tests through command line guide
  - [running_reports.txt](tips/running_reports.txt) - Guide to running and generating test reports in the 
