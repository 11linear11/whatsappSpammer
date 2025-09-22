# whatsappSpammer

This Python script uses **Selenium** to automate sending messages on WhatsApp Web.

---

## Features

* Log in to WhatsApp Web.
* Send multiple custom messages to a specific contact.
* Randomly select messages if multiple are provided.
* Send messages multiple times.
* Logout after sending messages.

---

## Requirements

* Python 3.x
* Selenium
* Chrome WebDriver

Install Selenium:

```bash
pip install selenium
```

Download [ChromeDriver](https://sites.google.com/chromium.org/driver/).

---

## Code Explanation

### 1. Import Libraries

```python
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
import time
```

* `webdriver`: Control the browser.
* `random`: Choose random messages.
* `Keys`: Simulate keyboard input.
* `time`: Add delays between messages.

---

### 2. Login Function

```python
def login_to_whatsapp(driver):
    driver.get('https://web.whatsapp.com')
    input('Please log in and then press Enter')
```

* Opens WhatsApp Web.
* Waits for the user to scan QR code and log in manually.

---

### 3. Get Messages Function

```python
def get_messages():
    contact_name = input('Enter the contact name: ')
    num_words = int(input('How many messages do you want to send? '))
    
    words = []
    for num in range(1, num_words + 1):
        msg = input(f'Enter message {num}: ')
        words.append(msg)

    num_msgs = int(input('How many times do you want to send a message? '))
    return contact_name, words, num_msgs
```

* Collects contact name.
* Collects multiple messages.
* Determines how many times messages should be sent.

---

### 4. Send Messages Function

```python
def send_messages(driver, contact_name, words, num_msgs):
    contact = driver.find_element_by_xpath(f'//span[@title="{contact_name}"]')
    contact.click()
    
    text_box = driver.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div[2]")
    
    for _ in range(num_msgs):
        msg = random.choice(words)
        text_box.send_keys(msg)
        text_box.send_keys(Keys.RETURN)
        time.sleep(1)
```

* Finds the contact.
* Finds the message input box.
* Sends a random message from the list multiple times.

---

### 5. Logout Function

```python
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
```

* Optional logout after sending messages.
* Checks for message completion.

---

### 6. Main Function

```python
def main():
    driver = webdriver.Chrome()
    
    login_to_whatsapp(driver)
    contact_name, words, num_msgs = get_messages()
    send_messages(driver, contact_name, words, num_msgs)
    logout(driver)

if __name__ == "__main__":
    main()
```

* Orchestrates login, message sending, and logout.
* Initializes Chrome WebDriver.

---

## Usage

1. Run the script:

```bash
python whatsapp_auto_sender.py
```

2. Scan the QR code in WhatsApp Web to log in.
3. Enter contact name, messages, and number of times to send.
4. Messages will be sent automatically.
