from playwright.sync_api import sync_playwright


def main():
    # Start playwright in context manager
    with sync_playwright() as p:
        # Set browser and other options
        browser = p.chromium.launch(slow_mo=500, channel="chrome", headless=False)
        # Create page object
        page = browser.new_page()
        # Go to login page
        page.goto("http://quotes.toscrape.com/login")
        # Find and fill username element
        page.fill("input[name=username]", "test")
        # Find and fill password element
        page.fill("input[name=password]", "test")
        # Find and click login button
        page.click("input[value=Login]")
        page.wait_for_timeout(100000)
        browser.close()


if __name__ == "__main__":
    main()
