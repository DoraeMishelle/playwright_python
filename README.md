# Awesome Agile Automation! 
# Playwright and Pytest Automation with Python

## Table Of Contents
- [Introduction](#introduction)
- [Setup Environment](#setup_environment)
- [Python Refresher](#python-refresher)

### Introduction
This project serves as my python refresher and automation/API testing project using playwright, pytest, and python.

Follow along with me on this journey of executing automated tests with python!

### Setup Environment (Prereqs: Python, Pytest, Playwright)

#### Playwright with Pytest Plugin

    pip install pytest-playwright

#### Install Browsers for Playwright
    playwright install


#### Update Playwright to Latest Version
    pip install pytest-playwright playwright -U


#### CLI commands

Run all tests (default → headless mode):
   
    pytest test_playwright.py -s -v


Run tests in headed mode:

    pytest test_playwright.py -s -v --headed


Run tests on different browsers:

    pytest test_playwright.py -s -v --headed --browser firefox
    pytest test_playwright.py -s -v --headed --browser chromium
    pytest test_playwright.py -s -v --headed --browser chromium --browser firefox


Run a specific test:

    pytest test_playwright.py::test_verify_page_title -s -v


Running Tests in Parallel (Requires pytest-xdist)
    
    pytest test_playwright.py -s -v --headed --browser chromium -n=2
    pytest test_playwright.py -s -v --headed --browser chromium -n 2

or

    pytest test_playwright.py -s -v --headed --browser chromium --numprocesses=2
    pytest test_playwright.py -s -v --headed --browser chromium --numprocesses 2

>_Note: Anyone one of these is the correct syntax for specifying the number of processes!_





### Python Refresher
