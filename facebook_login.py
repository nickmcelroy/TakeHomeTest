from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (in this case, Chrome)
driver = webdriver.Chrome()

# Open the login page URL
login_page_url = "https://identity.hudl.com/login?state=hKFo2SB4S0pDMjViUmFVY19oWlBHYXdKTXp2eUZYRUN4S3FzTaFupWxvZ2luo3RpZNkgNm5ReWR3aUxzbUJXd3JIMG5IaHFsejhYMEJHbG1ibE2jY2lk2SBuMTNSZmtIektvemFOeFdDNWRaUW9iZVdHZjRXalNuNQ&client=n13RfkHzKozaNxWC5dZQobeWGf4WjSn5&protocol=oauth2&response_type=id_token&redirect_uri=https%3A%2F%2Fwww.hudl.com%2Fapp%2Fusers%2Foidc%2Fcallback&scope=openid%20profile%20email&nonce=FdXEBg6dm5OXX62%2FbqXhej4ZkqhVfHlD55RKZ9DMH9g%3D&response_mode=form_post&screen_hint="
driver.get(login_page_url)

# Find the facebook button by id
fb_button = driver.find_element(By.ID, "btn-facebook-login")

fb_button.click()

# This is to delay the page from closing prematurely, in my case the driver would be killed before the test could run
input("Press Enter to test and exit...")

# Test to make sure that the title of the driver after the button is pressed contains Facebook
assert "Facebook" in driver.title, "Not directed to correct page"

# If the assertion passes, you can print a success message
print("Facebook button test passed!")

# Graceful teardown
driver.quit()