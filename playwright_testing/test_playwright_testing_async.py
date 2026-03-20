import pytest
from playwright.sync_api import Page, expect
from playwright.async_api import async_playwright, Page, expect

@pytest.mark.asyncio
# verify the url is correct
async def test_verify_page_url():
    # create customized async function
    async with async_playwright() as p:
        # using p alias, create chromium browser and launch it and wait for it to complete
        browser = await p.chromium.launch()
        # return the new page
        mypage = await browser.new_page()
        # specify the url
        await mypage.goto("https://john11co.com/")
        # expected url to return
        await expect(mypage).to_have_url("https://john11co.com/")

# verify the title is correct
#def test_verify_page_title(page: Page):
#    page.goto("https://john11co.com/")

    # retrieve the title before expect
#    mytitle = page.title
#    print("Title of application:", mytitle)

#    expect(page).to_have_title("John 1:1 Co.")