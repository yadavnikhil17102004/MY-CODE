from selenium import webdriver
import time

# Specify the path to the Chrome WebDriver executable
webdriver_path = '/home/linux-mint/Desktop/chromedriver'

# Path to your CSV or text file containing the participants' information
participants_file = '/home/linux-mint/Desktop/Untitled Document'

# Create a new Chrome WebDriver instance
driver = webdriver.Chrome(webdriver_path)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code and log in
input('Press Enter after scanning QR code and logging in...')

# Open the desired group chat
group_name = 'Group Name'  # Replace with the actual name of your WhatsApp group
group_xpath = f'//span[@title="{group_name}"]'
group_element = driver.find_element_by_xpath(group_xpath)
group_element.click()

# Read the participants' information from the file
with open(participants_file, 'r') as file:
    for line in file:
        name, number = line.strip().split(',')

        # Click on the input box to activate it
        input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
        input_box.click()

        # Type the name in the input box
        input_box.send_keys(name)
        time.sleep(2)  # Adjust as needed

        # Press Enter to confirm the name
        input_box.send_keys('\n')
        time.sleep(2)  # Adjust as needed

        # Type the number in the input box
        input_box.send_keys(number)
        time.sleep(2)  # Adjust as needed

        # Press Enter to confirm the number
        input_box.send_keys('\n')
        time.sleep(2)  # Adjust as needed

# Close the browser
driver.quit()
