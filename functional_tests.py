from selenium import webdriver

browser = webdriver.Edge()
browser.get("http://localhost:8000")
print(browser.title)

#assert "django" in browser.title
