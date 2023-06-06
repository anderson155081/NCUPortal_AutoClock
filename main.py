import schedule
from time import sleep
import logging
import datetime
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from line_notification import send_line_notification
from get_work import get_entries_from_json

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

load_dotenv()

def checkdate(run_date):
    today = datetime.date.today()
    day_of_month = today.day
    if "," not in run_date:
        if day_of_month == int(run_date):
            return True
        else:
            return False
    elif "everyday" == run_date:
        return True
    else:
        run_date = run_date.split(",")
        if day_of_month >= int(run_date[0]) and day_of_month <= int(run_date[1]):
            return True
        else:
            return False


def signInOut(job_code, is_signin, run_date, message):
    if checkdate(run_date):
        if is_signin:
            logging.info("Starting Job Sign Out.")
        else:
            logging.info("Starting Job Sign In.")
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')

            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://portal.ncu.edu.tw/login?")
            wait = WebDriverWait(driver, 10)

            username = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="inputAccount"]')))
            password = driver.find_element(By.XPATH, '//*[@id="inputPassword"]')
            
            # change this if your system language is chinese
            #submit = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/div/div/form/fieldset/div[4]/button')
            submit = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/div/div/form/fieldset/div[3]/button')

            username.send_keys(os.getenv("USERNAME"))
            password.send_keys(os.getenv("PASSWORD"))

            submit.click()
            sleep(5)
            driver.get("https://cis.ncu.edu.tw/HumanSys/")
            login_inner = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="head-meunu"]/div/div/nav/ul/li/a')))
            login_inner.click()

            # change this if your system language is chinese
            #login_connect = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/form/fieldset/div[3]/div/div/div/button')
            login_connect = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/form/fieldset/div[3]/div/div/div/button')))
            
            login_connect.click()
            sleep(5)
            driver.get("https://cis.ncu.edu.tw/HumanSys/student/stdSignIn/create?ParttimeUsuallyId="+job_code)

            if is_signin:
                message_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="AttendWork"]')))
                message_input.send_keys(message)
                submit = driver.find_element(By.XPATH, '//*[@id="signout"]')
                submit.click()
                sleep(5)
                driver.get_screenshot_as_file("signout.png")
                logging.info("Sign Out Success")
                send_line_notification(f"{job_code} : Sign Out Success", "signout.png")
            else:   
                submit = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signin"]')))
                submit.click()
                sleep(5)
                driver.get_screenshot_as_file("signin.png")
                logging.info("Sign In Success")
                send_line_notification(f"{job_code} : Sign In Success", "signin.png")
            
            driver.quit()

        except Exception as e:
            logging.error(e)
            logging.info("Sign In/Out Failed")
            send_line_notification(f"{job_code} : Sign In/Out Failed")
    else:
        logging.info("Not the day to run the job.")


def jobs():
    entries = get_entries_from_json()
    for entry in entries:
        schedule.every().day.at(entry["start_time"]).do(lambda: signInOut(entry["job_code"],False, entry["run_date"], entry["message"]))
        schedule.every().day.at(entry["end_time"]).do(lambda: signInOut(entry["job_code"],True, entry["run_date"], entry["message"]))

        logging.info("Job Scheduled.")
        logging.info("Job Code: " + entry["job_code"]+ " Start Time: " + \
                     entry["start_time"] + " End Time: " + entry["end_time"] + " Run Date: " + entry["run_date"])
        
        send_line_notification("Job Code: " + entry["job_code"]+ "\nStart Time: " + \
                        entry["start_time"] + "\nEnd Time: " + entry["end_time"] + "\nRun Date: " + entry["run_date"])

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    jobs()