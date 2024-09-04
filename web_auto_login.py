# Import the Selenium library and webdriver to automate the browser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Initialize the Chrome driver and maximize the browser window
driver = webdriver.Chrome()
driver.maximize_window()


# Function to start the bot with URL, email, and password as parameters
def startbot(url, email, password):
    driver.get(url)
    
    # decide for yourself in what way you will find the elements...  
    
    # Find email form elements then fill it in
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email) 
    # Find password form elements then fill it in
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)        
    # Find login button then click it
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/form/button').click()


# Ask the user to input the URL, email, and password
url = input("Enter your website URL: ")
email = input("Enter your email: ")
password = input("Enter your password: ")


# Call the startbot function with user input
startbot(url, email, password)


# Wait for 10 seconds before closing the browser
time.sleep(10)

driver.quit()