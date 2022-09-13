from playwright.sync_api import sync_playwright


def multiple_pages():
    # Start playwright in context manager
    with sync_playwright() as p:
        # Set browser and other options
        browser = p.chromium.launch(slow_mo=500, channel="chrome", headless=False)
        # Create page object
        page = browser.new_page()

        # Start with Dirk's Basketball Ref page
        page.goto("https://www.basketball-reference.com/players/n/nowitdi01.html")
        # Get most similar player and go to their page
        for i in range(5):
            # waiting for this to be clickable is done for you!
            page.click("div#switcher_sims tr[data-row='1'] th a")

        page.wait_for_timeout(100000)
        browser.close()


if __name__ == "__main__":
    multiple_pages()
