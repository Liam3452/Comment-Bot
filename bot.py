from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

def login(browser):
    browser.get("https://www.instagram.com/?hl=en")
    time.sleep(5)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login = browser.find_element_by_css_selector("button")

    #YOUR USERNAME GOES HERE
    username.send_keys("")
    #YOUR Password GOES HERE
    password.send_keys("")
    login.click()



    time.sleep(5)


def Vist_Tag(browser, url):
    sleepy_time = 5
    browser.get(url)
    time.sleep(sleepy_time)

    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")

    image_count = 0

    for picture in pictures:
        if image_count >= 3:
            break

        picture.click()
        time.sleep(sleepy_time)

        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
        text = "go follow @_python.exe_ if you want to see cool computer hacking content "
        sleep(70)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(text)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()


        close = browser.find_element_by_css_selector("[aria-label='Close']")
        close.click()

        image_count += 1
        time.sleep(sleepy_time)

def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = [
        "cars",
        "humor",
        "python",
        "java",
        "rock",
        "hacker",
        "javascript",
        "food",
    ]

    while True:
        for tag in tags:
            Vist_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        time.sleep(3600)

main()