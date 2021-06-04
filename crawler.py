from selenium import webdriver
path_to_chromedriver = 'C:/images/chromedriver_win32_89/chromedriver.exe'

driver = webdriver.Chrome(path_to_chromedriver)


def check_scores():
    driver.get("https://www.csgoroll.com/en/crash")
    upload_field = driver.find_element_by_xpath("cw-root")
    driver.implicitly_wait(5)
    # last_games = driver.find_element_by_class_name("ng-tns-c481-3 ng-tns-c478-7")
    for game in upload_field:
        print(game.text)

check_scores()