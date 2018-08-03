import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from contextlib import suppress
#Firefox Options
options = Options()
options.set_headless(headless=True)
#email address goes here
userName = open("myemail.txt").read().strip()
password = open("mypassword.txt").read().strip()
#You can change the phrase before the tweet
phraseToTweet = 'O SHIT WADDUP'

twitter_login_url = 'https://twitter.com/login'

def OpenTwitterAndLogIn(username, password):
    browser.get(twitter_login_url)
    try:
        usernameElement = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'js-username-field')))
        passwordElement = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'js-password-field')))
    finally:
        #I put a few sleeps in here just for good measure
        usernameElement.clear()
        passwordElement.clear()
        time.sleep(0.5)
        usernameElement.send_keys(username)
        passwordElement.send_keys(password)
        time.sleep(0.5)
        passwordElement.send_keys(Keys.TAB)
        passwordElement.send_keys(Keys.ENTER)

def WriteTweet(tweetString):
    #this allows customizable inputs
    tweet = phraseToTweet + ' ' + tweetString

    tweetTextBox = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tweet-box.rich-editor')))
    tweetTextBox.send_keys(tweet)
    time.sleep(2)
    tweetTextBox.send_keys(Keys.COMMAND, Keys.ENTER)

    print(tweet)

if __name__ == '__main__':
    print('...DDDDD.........A......TTTTTTT...BBBBBBB......OOOO.....IIIIIII...')
    print('...D....D.......A.A........T......B......B....O....O.......I......')
    print('...D.....D.....A...A.......T......B......B...O......O......I......')
    print('...D......D...AAAAAAA......T......BBBBBBB....O......O......I......')
    print('...D.....D....A.....A......T......B......B...O......O......I......')
    print('...D....D.....A.....A......T......B......B....O....O.......I......')
    print('...DDDDD......A.....A......T......BBBBBBB......OOOO.....IIIIIII...')

    with suppress(KeyboardInterrupt, SystemExit):
        while True:
            stringToTweet = input(phraseToTweet + ' + : ')
            browser = webdriver.Firefox(firefox_options=options)
            browser.set_window_position(0, 0)
            browser.set_window_size(1024, 768)
            OpenTwitterAndLogIn(userName, password)
            WriteTweet(stringToTweet)
            browser.quit()

    browser.quit()
    print('\n BROWSER QUIT SUCCESSFULLY AFTER INTERUPT BOI.')        
