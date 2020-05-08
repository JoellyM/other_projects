from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.bot= webdriver.Firefox(executable_path="C:/Program Files/Mozilla Firefox/firefox.exe")

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(10)
        email =bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.RETURN)
        time.sleep(10)

    def like_tweet(self,hashtag):
        bot =self.bot
        bot.get(r'https://twitter.com/search?q=' + hashtag + '&src=typeahead_click')
        time.sleep()
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight')
            time.sleep(5)
            tweets = bot.find_elements_by_class_name('tweet')
            links =[elem.get_attribute('data-permalink-path') for elem in tweets10]

            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_elements_by_class_name('HeartAnimation').click()
                    time.sleep(10)

ed = TwitterBot('liljearsy@gmail.com', 'Madara12')
ed.login()

