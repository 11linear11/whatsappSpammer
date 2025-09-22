from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
import time

# Function to log into WhatsApp
def login_to_whatsapp(driver):
    driver.get('https://web.whatsapp.com')
    input('Please log in and then press Enter')

# Function to get message details from user
def get_messages():
    contact_name = input('Enter the contact name: ')
    num_words = int(input('How many messages do you want to send? '))
    
    words = []
    for num in range(1, num_words + 1):
        msg = input(f'Enter message {num}: ')
        words.append(msg)

    num_msgs = int(input('How many times do you want to send a message? '))
    return contact_name, words, num_msgs

# Function to send messages
def send_messages(driver, contact_name, words, num_msgs):
    # Find the contact in WhatsApp
    contact = driver.find_element_by_xpath(f'//span[@title="{contact_name}"]')
    contact.click()
    
    # Find the message input box
    text_box = driver.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div[2]")
    
    # Send the messages
    for _ in range(num_msgs):
        msg = random.choice(words)
        text_box.send_keys(msg)
        text_box.send_keys(Keys.RETURN)
        time.sleep(1)  # Add a small delay to prevent spamming

# Function to logout after sending messages
def logout(driver):
    print('Messages sent!')
    while True:
        if "msg-time" not in driver.page_source:
            menu = driver.find_element_by_css_selector('.\\_2n-zq:nth-child(3) > div > span')
            menu.click()
            logout_button = driver.find_element_by_xpath('//li[7]/div')
            logout_button.click()
            break
        else:
            print('Sending...')

# Main function to run the script
def main():
    driver = webdriver.Chrome()
    
    # Login to WhatsApp
    login_to_whatsapp(driver)

    # Get user input for messages
    contact_name, words, num_msgs = get_messages()

    # Send messages to the contact
    send_messages(driver, contact_name, words, num_msgs)

    # Log out after sending messages
    logout(driver)

if __name__ == "__main__":
    main()
