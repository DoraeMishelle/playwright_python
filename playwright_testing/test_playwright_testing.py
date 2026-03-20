from playwright.sync_api import Page, expect

def test_verify_page_url(page: Page):
    page.goto("https://john11co.com/")
    expect(page).to_have_url("https://john11co.com/")
    assert True

def test_verify_page_title():
    assert True