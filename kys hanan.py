from selenium import webdriver
import requests
import time


#initialize the variables for selenium webdriver stuffs
driver = webdriver.Chrome()
name = driver.find_element_by_id("FullName")
email = driver.find_element_by_id("Email")
year = driver.find_element_by_id("Year")
college = driver.find_element_by_id("Institution")
terms = driver.find_element_by_id("AffAcceptance")  
submit = driver.find_element_by_id("btn-Enter")


# availability website
api_url = "https://www.dominos.com/emergency-pizza-for-student-loans/availability.json"

# discord webhok
discord_webhook_url = "https://discord.com/api/webhooks/1167672427833196584/mpZ2Q14vt6ZglvgOPw5Yp_CSEPHvQ4tWb-NReGoLVxRDc73bmIxhL8V5d6kv90RIrU4V"

def check_status():
    while True:
        response = requests.get(api_url)
        data = response.json()

        if data.get("status"):
            print("The status is true.")
            send_discord_message("Site is true")
            

            driver.get("https://www.dominosemergencypizzaforstudentloans.com/")

            
            name.send_keys("pogger")

            
            email.send_keys("jackyang7410@gmail.com")

            
            college.send_keys("emory")

            
            year.send_keys("2024")

            
            terms.click()

            submit.click()
 

        print("The status is false.")
        time.sleep(1) 

def send_discord_message(message):
    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(discord_webhook_url, json=payload, headers=headers)

if __name__ == "__main__":
    check_status()








