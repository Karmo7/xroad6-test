require "selenium-webdriver"
browser = Selenium::WebDriver.for :phantomjs
browser.get "https://centralserver.one.one/login"
browser.save_screenshot "securityserver.one.one_phantomjs.png"
browser.quit
