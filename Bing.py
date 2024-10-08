import random
# import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# def search_word_generator(num_words=30, word_length=4):
#     for _ in range(num_words):
#         generated_word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
#         yield generated_word

def words_getter():
    with open('words.txt', 'r') as file:
        words = [line.strip() for line in file]     
    return words

def random_word(words):
    return random.choice(words)
    
def user_agent_getter():
    with open('user_agents.txt', 'r') as file:
        user_agents = [line.strip() for line in file]
    return user_agents

def random_user_agent(user_agents):
    return random.choice(user_agents)

def Script(name, daily_sets = False, mobile = False, words = 30):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument('--user-data-dir='+name)
    # options.add_argument('--headless=new')
    if mobile:
        user_agents = user_agent_getter()
        user_agent = random_user_agent(user_agents)
        options.add_argument('--user-agent='+user_agent)
    with webdriver.Chrome(options=options) as driver:
        driver.implicitly_wait(5)
        driver.get("https://www.bing.com/?toWww=1&redig=A0BE546CDCFD45F29C3EB49164F90364&wlexpsignin=1")
        wait = WebDriverWait(driver, timeout=10)
        if False:  
            accept = driver.find_element(by=By.ID, value="bnp_btn_accept")
            wait.until(lambda d: accept.is_displayed())
            accept.click()

        driver.get("https://www.bing.com/search?")
        words_list = words_getter()
        for i in range(words):
            word = random_word(words_list) +'+'+ random_word(words_list)
            #     srch_cls = driver.find_element(by=By.ID, value="sb_form_q").clear()
            #     srch_ins = driver.find_element(by=By.ID, value="sb_form_q").send_keys(word)
            #     srch_sub = driver.find_element(by=By.ID, value="sb_form_q").send_keys(Keys.RETURN)
            driver.get(f"https://www.bing.com/search?q={word}&form=QBLH")
            time.sleep(6)

            
        if daily_sets:
            driver.get("https://rewards.bing.com/")
            time.sleep(10)
            activities = []
            for i in range(1,10):
                try:
                    activity = driver.find_element(by=By.XPATH,
                        value=f"//*[@id=\"daily-sets\"]/mee-card-group[1]/div/mee-card[{i}]")
                    activities.append(activity)
                    
                except NoSuchElementException:
                    print(f"found no item {i}")
                    break
            
            for i in range(1,10):
                try:
                    activity = driver.find_element(by=By.XPATH,
                        value=f"//*[@id=\"more-activities\"]/div/mee-card[{i}]/div/card-content/mee-rewards-more-activities-card-item/div/a")
                    if "Take the tour" in activity.text:
                        break
                    activities.append(activity)
                    
                except NoSuchElementException:
                    print(f"found no item {i}")
                    break
            
            for item in activities:
                item.click()
                time.sleep(3)
                    


names = ['amadoabad']
for name in names:
    Script(name=name, daily_sets=True, words=33)
    Script(name=name, words=23, mobile=True)


