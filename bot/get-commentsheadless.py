from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from pyvirtualdisplay import Display
import datetime
import time
import mysql.connector
global db_connection


db_connection = mysql.connector.connect(
  host="localhost",
  user="user",
  password="password",
  charset='utf8',
  use_unicode=True,
  database="db"
)

global db_cursor
db_cursor = db_connection.cursor()
global display
db_cursor.execute('SET NAMES utf8mb4')
db_cursor.execute("SET CHARACTER SET utf8mb4")
db_cursor.execute("SET character_set_connection=utf8mb4")


def main():
    setup()
    geturl()
    checkurlindatabase()
    cookiesconsent()
    lookforcommentssection()
    lookupcomments()
    lookupanswers
    writeurl()

def setup():
    global options
    global driver
    global display
    display = Display(visible=0, backend="xvfb", size=(800, 600))
    display.start()
    options = Options()
    print("Sleeping for 70 seconds before startup")
    #time.sleep(70)
    print("\n" + "loading driver" + "\n")
    options.add_argument("--start-maximized")
    #desired_caps = options.to_capabilities()
    #prox = Proxy()
    #prox.proxy_type = ProxyType.MANUAL
    #prox.ssl_proxy = "x.botproxy.net:8443"
    #prox.http_proxy = "x.botproxy.net:8080"
    #prox.add_to_capabilities(desired_caps)
  #  options.add_argument('headless')
    driver = webdriver.Firefox(executable_path='/home/user/nationen-bot/geckodriver')
    driver.implicitly_wait(10)
    print("\n" + "Finished loading driver" + "\n")

def geturl():
    global my_file
    global url
    my_file = open("eblinks-cleaned-1.txt", "r")
    for url in my_file:
        try:
            print("\n" + "Trying for " + url + "\n")
            driver.get(url)
            print("\n" + "Successfully loaded" + " " + url + "\n")

            Aselecturl = "SELECT IF ( EXISTS(select * from url where url = '"
            Bselecturl = "'),1,0);"
            db_cursor.execute(Aselecturl + url + Bselecturl)
            results = db_cursor.fetchall()

            if  results ==[(1,)]:
                print("already exists in database")
                time.sleep(2)
                continue
            else:
                Ainserturl = "REPLACE INTO url (url) VALUES ('"
                Binserturl = "');"
                db_cursor.execute(Ainserturl + url + Binserturl)
                db_connection.commit()
                cookiesconsent()


        except Exception as e:
            print(e)
            print("URL not working")
            continue



def cookiesconsent():
    try:
        print("Sleeping for 3 seconds")
        time.sleep(3)
        WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@id="sp_message_iframe_393238"]')))
        print("\n" + "Loaded modal cookie consent successfully  " + "\n")
        print("\n" + "Pressing cookie consent Button" + "\n")
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="OK"]'))).click()
        print("Successfully pressed cookie consent button")
        print("\n" + "switching back from modal cookie consent" + "\n")
        driver.switch_to.default_content()
        print("\n" + "Successfully switched back from modal cookie consent" + "\n")
        lookforcommentssection()
    except Exception as e:
        print(e)
        print("no cookies module, fine if already accepted")
        lookforcommentssection()

def lookforcommentssection():
    try:
        print("Sleeping for 3 seconds")
        time.sleep(3)
        print("running javascript scroll for comment section")

        #place div in a variable and move to the div with js in next line
        element0 = driver.find_element_by_xpath('//div[contains(@id,"fnfetchTalk")]')
        driver.execute_script("arguments[0].scrollIntoView(true);", element0);
        print("running javascript button click on show comment section")
        #click the show comments button
        driver.execute_script("arguments[0].click();", element0)
        print("Successfully pressed comments section button")
        print("Attempting to switch to iframe")
        WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@name="talkStream_iframe"]')))
        print("Loaded modal comment section successfully")
        #print("Switching back to get title")
        #driver.switch_to.default_content()
        #global title
        #title = driver.find_element_by_xpath('//h1[contains(@class, "art-title")]')
        #print("Retrieved title successfully")
        #print("Attempting to switch to iframe")
        #WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@name="talkStream_iframe"]')))
        #print("Loaded modal comment section successfully")
        lookupcomments()
    except Exception as e:
        print(e)
        print("No comment section")
        print("Closing driver")
        geturl()

def lookupcomments():
    try:
        print("Sleeping for 2 seconds")
        time.sleep(2)
        print("running javascript scroll on show more comments")
        #place button in a variable and move to the button with js in next line
        element1 = driver.find_element_by_xpath('//button[text()="se flere kommentarer"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", element1);
        print("Sleeping for 2 seconds")
        time.sleep(2)
        print("running javascript button click on show more comments")
        #click the show comments button
        driver.execute_script("arguments[0].click();", element1)
        print("Succesfully loaded more comments")
        lookupcomments()
    except Exception as e:
        print(e)
        print("No more comments")
        print("Sleeping for 5 seconds")
        time.sleep(5)
        lookupanswers()

def lookupanswers():
    try:
        print("running javascript scroll on show more answers")
        #place button in a variable and move to the button with js in next line
        global elementanswers
        elementanswer = driver.find_elements_by_xpath('//button[text()="Vis flere svar"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", elementanswer);
        print("Sleeping for 2 seconds")
        time.sleep(2)
        print("running javascript button click on show more answers")
        #click the show comments button
        driver.execute_script("arguments[0].click();", elementanswer)
        print("Succesfully loaded more answers")
        lookupanswers()
    except Exception as e:
        print(e)
        print("No more answers")
        print("Sleeping for 3 seconds")
        time.sleep(3)
        writeurl()

def writeurl():
        global comments
        global datenow
        datenow = datetime.datetime.now()
        #global authors
        Acomment = "INSERT INTO comments (url, dateimported, comment) VALUES ('"
        Bcomment = "', curdate(), '"
        Dcomment = "');"
        comments = driver.find_elements_by_xpath('//div[contains(@data-slot-name, "commentContent")]')
        #authors = driver.find_elements_by_xpath('//div[contains(@class,"ShowDisplayname__myAuthorName___MCE8_")]')
        for comment in comments:
                try:
                        db_cursor.execute(Acomment + url + Bcomment + comment.text + Dcomment)
                        db_connection.commit()
                except Exception as e:
                        print(e)
                        continue
        print("Finished writing to database")

print("Starting program")
main()
