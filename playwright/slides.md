---
marp: true
theme: uncover
---
# Playwright

---
https://playwright.dev/
https://playwright.dev/python/
getting started - https://playwright.dev/python/docs/library

---
# Why Playwright?

---
### If you're lucky, you dont need Playwright

HTML, API, etc

---
1_no_webdriver.ipynb

---
### What about Javascript?
Buttons, Forms, Cookies, Menus, the DOM, etc

---
# Web Driver
https://www.w3.org/TR/webdriver/
"...language-neutral wire protocol as a way for out-of-process programs to remotely instruct the behavior of web browsers"

---
# Selenium?
https://www.selenium.dev/
https://selenium-python.readthedocs.io/

---
# Playwright
![](https://playwright.dev/python/img/playwright-logo.svg)

---
- Handles downloading and managing the webdrivers
- handles waits out of the box
- easier syntax
- documentation is better
- headless mode is one parameter
- Among many others

---
# 2_simple_login.py
1. pip install playwright
2. playwright install

---
# 3_multiple_pages.py
- auto-waiting

---
# 4_non_linked_elements.py
- slowmo, headless mode

---
# Debugging
https://playwright.dev/python/docs/debug-selectors

---
# 5_debugging.py

---
# Playwright inspector
https://playwright.dev/python/docs/debug
```python
page.pause()
```
or set it to start for every script with command line 
```powershell
$env:PWDEBUG=1
```


---
# dev tools
https://playwright.dev/python/docs/debug-selectors

---

```powerhell
$env:PWDEBUG="console"
```

---
Try the following in dev console window:
```js
playwright.$('.button2')
```

---

# HAPPY SCRAPING