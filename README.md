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

<details>
  <summary>Project Structure</summary>

-  <kbd>[framework/](framework/)</kbd> - Reusable components, helpers, and custom fields for tests<br/>
    <details>
        <summary>framework/</summary>
        - <kbd>[fields/](framework/fields/)</kbd> - Custom field objects<br/>
            <details>
                <summary>fields/</summary>
                - <kbd>[base_field](framework/fields/base_field.py)</kbd>Base class for all field types<br/>
                - <kbd>[button_field](framework/fields/button_field.py)</kbd>Button field types<br/>
                - <kbd>[dropdown_field](framework/fields/dropdown_field.py)</kbd>Dropdown field types<br/>
                - <kbd>[link_field](framework/fields/link_field.py)</kbd>link field types<br/>
                - <kbd>[navigation_field](framework/fields/navigation_field.py)</kbd>Navigation field types<br/>
                - <kbd>[static_field](framework/fields/static_field.py)</kbd>static text field types<br/>
                - <kbd>[table_field](framework/fields/table_field.py)</kbd>table field types<br/>
                - <kbd>[textbox_field](framework/fields/textbox_field.py)</kbd>textbox field types<br/>
            </details>
        - <kbd>[helpers/](framework/helpers/)</kbd> - Helper classes like wait utilities, verifications<br/>
            <details>
                <summary>helpers/</summary>
                - <kbd>[verifications/](framework/helpers/verifications/)</kbd>Verification Objects for field types<br/>
                    <details>
                        <summary>verifications/</summary>
                        - <kbd>[verify_base](framework/helpers/verifications/verify_base.py)</kbd>Verification class for base fields<br/>
                        - <kbd>[verify_button](framework/helpers/verifications/verify_button.py)</kbd>Verification class for button fields<br/>
                        - <kbd>[verify_cell](framework/helpers/verifications/verify_cell.py)</kbd>Verification class for cells<br/>
                        - <kbd>[verify_dropdown](framework/helpers/verifications/verify_dropdown.py)</kbd>Verification class for dropdown fields<br/>
                        - <kbd>[verify_link](framework/helpers/verifications/verify_link.py)</kbd>Verification class for link fields<br/>
                        - <kbd>[verify_static](framework/helpers/verifications/verify_static.py)</kbd>Verification class for static text fields<br/>
                        - <kbd>[verify_textbox](framework/helpers/verifications/verify_textbox.py)</kbd>Verification class for textbox fields<br/>
                    </details>
                - <kbd>[wait_utilities](framework/helpers/wait_utilities/)</kbd>Utility objects for waits<br/>
                    <details>
                        <summary>wait utilities/</summary>
                        - <kbd>[wait_helper](framework/helpers/wait_utilities/wait_helper.py)<kbd>Utility methods for waiting for loads<br/>
                    </details>
                - <kbd>[window_utilities](framework/helpers/window_utilities/)</kbd>Utility objects for window handles<br/>
                    <details>
                        <summary>window_utilities/</summary>
                        - <kbd>[window_helper](framework/helpers/window_utilities/window_helper.py)</kbd>Utility methods for switching window handles<br/>
                    </details>
    </details>
-  <kbd>[pages/](pages/)</kbd> - Page Object Model (POM) classes representing different pages<br/>
    <details>
        <summary>pages/</summary>
        - <kbd>[performance_pages/](pages/performance_pages/)</kbd>Pages belonging to Performance area<br/>
            <details>
                <summary>performance_pages/</summary>
                - <kbd>[employee_reviews_page](pages/performance_pages/employee_reviews_page.py)</kbd>Employee Review Page object<br/>
                - <kbd>[my_reviews_page](pages/performance_pages/my_reviews_page.py)</kbd>My Review Page object<br/>
                - <kbd>[performance_base_page](pages/performance_pages/performance_base_page.py)</kbd>Performance Base Page object<br/>
            </details>
        - <kbd>[time_pages/](pages/time_pages/)</kbd>...<br/>
            <details>
                <summary>time_pages/</summary>
                - <kbd>[punch_in_out_page](pages/time_pages/punch_in_out_page.py)</kbd>Punch In/Out Page object<br/>
                - <kbd>[time_base_page](pages/time_pages/time_base_page.py)</kbd>Time Base Page object<br/>
            </details>
        - <kbd>[base_page](pages/base_page.py)</kbd>Universal Base Page object<br/>
        - <kbd>[dashboard_page](pages/dashboard_page.py)</kbd>Dashboard Page object<br/>
        - <kbd>[login_page](pages/login_page.py)</kbd>Login Page object<br/>
    </details>
-  <kbd>[reports/](reports/)</kbd> - Stores test results and Allure reports<br/>
    <details>
        <summary>reports/</summary>
        - <kbd>[results/](reports/results/)</kbd>Test results<br/>
    </details>
-  <kbd>[tests/](tests/)</kbd> - Contains all automated test cases<br/>
    <details>
        <summary>tests/</summary>
        - <kbd>[conftest](tests/conftest.py)</kbd>Base Test configuration<br/>
        - <kbd>[dashboard_test](tests/dashboard_test.py)</kbd>Dashboard functionality tests<br/>
        - <kbd>[punch_in_out_test](tests/punch_in_out_test.py)</kbd>Punch In/Out functionality tests<br/>
    </details>
-  <kbd>[tips/](tips/)</kbd> - Running tests through command line guide<br/>
    <details>
        <summary>tips/</summary>
        - <kbd>[running_reports.txt](tips/running_reports.txt)</kbd>Guide to running and generating test reports in the CLI<br/>
    </details>

</details>
