from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (in this case, Chrome)
driver = webdriver.Chrome()

# Open the login page URL
login_page_url = "https://identity.hudl.com/login?state=hKFo2SB4S0pDMjViUmFVY19oWlBHYXdKTXp2eUZYRUN4S3FzTaFupWxvZ2luo3RpZNkgNm5ReWR3aUxzbUJXd3JIMG5IaHFsejhYMEJHbG1ibE2jY2lk2SBuMTNSZmtIektvemFOeFdDNWRaUW9iZVdHZjRXalNuNQ&client=n13RfkHzKozaNxWC5dZQobeWGf4WjSn5&protocol=oauth2&response_type=id_token&redirect_uri=https%3A%2F%2Fwww.hudl.com%2Fapp%2Fusers%2Foidc%2Fcallback&scope=openid%20profile%20email&nonce=FdXEBg6dm5OXX62%2FbqXhej4ZkqhVfHlD55RKZ9DMH9g%3D&response_mode=form_post&screen_hint="
driver.get(login_page_url)

# Find the email and password input fields and continue button by their id's
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")
continue_button = driver.find_element(By.ID, "logIn")

# Send email and empty password credentials
email = "email@email.com"  # enter valid or invalid email
empty_password = ""

email_field.send_keys(email)
password_field.send_keys(empty_password)

# Click the continue button
continue_button.click()

# This is to delay the page from closing prematurely, in my case the driver would be killed before the test could run
input("Press Enter to test and exit...")

# Find error message and test it displays
error_message = driver.find_element(By.CLASS_NAME, "error-message")

assert "Please fill in all of the required fields" in error_message.text, "Error message for empty password not displayed"

# If the assertion passes print a success message
print("Empty password test passed successfully!")

# Graceful teardown
driver.quit()