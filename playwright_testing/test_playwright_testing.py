from playwright.sync_api import Page, expect

# verify the url is correct
def test_verify_page_url(page: Page):
    page.goto("https://john11co.com/")

    # retrieve the URL before expect
    myurl = page.url
    print("URL of application:", myurl)

    expect(page).to_have_url("https://john11co.com/")

# verify the title is correct
def test_verify_page_title(page: Page):
    page.goto("https://john11co.com/")

    # retrieve the title before expect
    mytitle = page.title
    print("Title of application:", mytitle)

    expect(page).to_have_title("John 1:1 Co.")