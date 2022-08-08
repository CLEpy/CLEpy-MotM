from playwright.sync_api import sync_playwright

""" 
Run script with load playwright inspector
$env:PWDEBUG=1
 
Run with playwright dev tools
$env:PWDEBUG="console"
"""


def hidden_info():
    # Start playwright in context manager
    with sync_playwright() as p:
        # Set browser and other options
        # Play with slowmow and headless to see how that works
        browser = p.chromium.launch(slow_mo=2000, channel="chrome", headless=False)
        # Create page object
        page = browser.new_page()

        # Pause and start playwright inspector
        # page.pause()

        # Go to Lebron's Basketball Ref page
        page.goto("https://www.basketball-reference.com/players/j/jamesle01.html")
        # Click playoff per game button
        page.click("a[data-show='.assoc_playoffs_per_game']")
        # Click share/export button
        page.click("div.assoc_playoffs_per_game .hasmore")
        # Click get table as csv(excel)
        page.click(
            "div#all_per_game-playoffs_per_game div.assoc_playoffs_per_game  button[tip='Get a link directly to this table on this page']"
        )
        # Get text from transformed table
        csv_text = page.inner_text("pre#csv_playoffs_per_game")
        print(csv_text)
        page.wait_for_timeout(100000)
        browser.close()


if __name__ == "__main__":
    hidden_info()
