from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

print(driver.title)
print(driver.find_element(By.XPATH, "//p[@class='site-title']//a[contains(text(),'California Real Estate')]").get_attribute("href"))
print(driver.find_element(By.CLASS_NAME, "wp-image-55").get_attribute("src"))
assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
print(driver.title)
print(driver.find_element(By.XPATH,"//h2[contains(text(),'Send Us a Message')]").is_displayed())
driver.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Daulet B")
driver.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("daulet@yahoo.com")
driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("Sample Message Selenium Webdriver Python")
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").submit()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))
driver.close()