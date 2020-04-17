#you need to get selenium and chromedriver to run this
#read readme i tried to explain some stuff
#see the bottom for the functions

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import random


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self, location):
        self.driver.get('https://tinder.com')

        sleep(2)

	#gg_btn = bot.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[1]/div/button') 
	#gg_btn.click()

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

    
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('YOUR USRNM')

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('YOUR PASS')


        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to.window(self.driver.window_handles[0])

        sleep(3)

        popup_cookies = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div/button')
        popup_cookies.click()

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

        sleep(2)

        """
        #declines the login set location prompt
        popup_setlocation = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button')
        popup_setlocation.click()
        """


        #from here to the end of the function is all setting the location from the login state

        popup_setlocation = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/a')
        popup_setlocation.click()

        sleep(2)

        location_in = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[5]/div[2]/div[1]/input')
        location_in.send_keys(location)

        sleep(2)

        searchlocation_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[5]/div[2]/div[1]/div[2]')
        searchlocation_btn.click()
        acceptlocation_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[2]/button')
        acceptlocation_btn.click()  
       

    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')	
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.1)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_z = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_z.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    #unfinished function
    def set_location(self, location):
        profile_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/aside/div/a')
        profile_btn.click()
        self.driver.execute_script("window.scrollBy(0,750)")
        sleep(2)

    def message(self):
        while(True):
            matches = self.driver.find_elements_by_class_name('matchListItem')[1:] 
            if len(matches) <2:
                break
            matches[0].click()
            sleep(0.2)

            responses = ['hi', 'howdy partner', 'Yeehaww!', '.oO0Oo.', 'BLEEP-BLOOP']

            msg_box = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            msg_box.send_keys(random.choice(responses))
            send_msg = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            send_msg.click()
            sleep(0.5)
            matches_tab = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            matches_tab.click()
            sleep(.5)

    def random_swipe(self):
        while True:
            sleep(0.1)     
            try:
                rand = random() 
                if rand < 0.95:             #95% like chance
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def swipe_and_message(self):
        while True:
            try:
                self.random_swipe()
            except Exception:
                try:
                    self.message()
                except Exception:
                    exit_msgs = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[1]/a/button')
                    exit_msgs.click()

bot = TinderBot()
bot.login('New York City')
bot.swipe_and_message()

#SOME FUNCTIONS:

#bot.login('location')
#bot.message()
#bot.auto_swipe()
#bot.random_swipe()
#bot.swipe_and_message()

