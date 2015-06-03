require "selenium-webdriver"
browser = Selenium::WebDriver.for :phantomjs
browser.get "https://centralserver.one/login"
browser.save_screenshot "centralserver.one_phantomjs.png"
browser.quit
