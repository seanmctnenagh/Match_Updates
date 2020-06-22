from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from PIL import Image
from io import BytesIO
import time

user = input("Username: ")
password = input("Password: ")

################################################################################################################
def getProg(driver):
    driver.get('http://www.nenagheireog.club/progression.html#'+str(j)) # Open prog
    driver.maximize_window()
    time.sleep(0.5)
    png = driver.get_screenshot_as_png()

    im = Image.open(BytesIO(png))

    im = im.crop((15,15,600,375))

    im.save("progression.png")

################################################################################################################

def getScores(driver,j):
    driver.get('http://www.nenagheireog.club/match-updates.html#'+str(j)) # Open scores
    driver.maximize_window()

    driver.execute_script("window.scrollTo(0,scrollY + 25)") # Scroll to top
    png = []
    png.append(driver.get_screenshot_as_png())

    width = 640
    height = 600
    gapLeft = 15

    scores = Image.new("RGB", (640,3000))

    for i in range(5): # Take screenshots and save
        driver.execute_script("window.scrollTo(0,scrollY + 600)")
        time.sleep(0.5)
        png.append(driver.get_screenshot_as_png())
        im = Image.open(BytesIO(png[i]))
        name = 'scores'+str(i+1)+'.png'
        
        left = gapLeft
        top = 0
        right = gapLeft + width
        bottom = height

        im = im.crop((left, top, right, bottom))

        x = 0
        y = i * 600

        scores.paste(im,(x,y)) # Merge

        im.save(name)


    scores.save("scores.png")


###########################################################################################################

def getTeams(driver, j):
    driver.get('http://www.nenagheireog.club/teams.html#'+str(j)) # Open teams
    driver.maximize_window()

    driver.execute_script("window.scrollTo(0,scrollY + 15)") # Scroll to top
    png = []
    png.append(driver.get_screenshot_as_png())

    width = 640
    height = 600
    gapLeft = 15
    lastTeams = 222

    teams = Image.new("RGB", (640,2024))

    for i in range(4): # Take screenshots and save
        driver.execute_script("window.scrollTo(0,scrollY + 600)")
        png.append(driver.get_screenshot_as_png())
        im = Image.open(BytesIO(png[i]))
        name = 'teams'+str(i+1)+'.png'
        
        left = gapLeft
        if i == 3:
            top = 600 - lastTeams
        else:
            top = 0
        right = gapLeft + width
        bottom = height

        im = im.crop((left, top, right, bottom))

        
        x = 0
        y = i * height

        teams.paste(im,(x,y)) # Merge

        im.save(name)


    teams.save("teams.png")



###########################################################################################################

chrome_path = r"C:\Users\seanm\Desktop\chromedriver_win32\chromedriver.exe"
j=0
while(True): # Update scores
    j+=1
    driver = webdriver.Chrome(chrome_path)
    driver.delete_all_cookies()
    driver.get('chrome://settings/clearBrowserData')
    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    
    getScores(driver, j)
    getTeams(driver, j)
    getProg(driver)

    # driver.find_element_by_id("link").click() # Open uploads page

    driver.get("http://www.nenagheireog.com/wp-admin/upload.php")
    time.sleep(1)

    driver.find_element_by_id("user_login").send_keys(user) # Input username
    driver.find_element_by_id("user_pass").send_keys(password+Keys.ENTER) # Input password
    
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[4]/a").click() # Click add new

    driver.find_element_by_xpath("/html/body/div[7]/input").send_keys(r"C:\Users\seanm\Documents\MatchUpdates\Match_Updates\scores.png") # Give new image path
    driver.find_element_by_xpath("/html/body/div[7]/input").send_keys(r"C:\Users\seanm\Documents\MatchUpdates\Match_Updates\teams.png") # Give new image path
    driver.find_element_by_xpath("/html/body/div[7]/input").send_keys(r"C:\Users\seanm\Documents\MatchUpdates\Match_Updates\progression.png") # Give new image path
    time.sleep(20)

    print("Don't")
    driver.find_element_by_id("media-search-input").send_keys("scores .png") # Search for scores image
    time.sleep(4)
    try:
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/div[3]/div[2]/div/ul/li[2]").click() # Click Image
        driver.find_element_by_xpath("/html/body/div[8]/div[1]/div/div/div[3]/div/div[2]/div[4]/button").click() # Delete Image
        driver.switch_to.alert.accept() # Confirm delete
    except:
        pass


    driver.find_element_by_id("media-search-input").send_keys(Keys.CONTROL+"a") # Search for teams image        
    driver.find_element_by_id("media-search-input").send_keys("teams .png") # Search for teams image
    time.sleep(4)
    try:
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/div[3]/div[2]/div/ul/li[2]").click() # Click Image
        driver.find_element_by_xpath("/html/body/div[8]/div[1]/div/div/div[3]/div/div[2]/div[4]/button").click() # Delete Image
        driver.switch_to.alert.accept() # Confirm delete
    except:
        pass

    driver.find_element_by_id("media-search-input").send_keys(Keys.CONTROL+"a") # Search for teams image        
    driver.find_element_by_id("media-search-input").send_keys("progression .png") # Search for teams image
    time.sleep(4)
    try:
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]/div[3]/div[2]/div/ul/li[2]").click() # Click Image
        driver.find_element_by_xpath("/html/body/div[8]/div[1]/div/div/div[3]/div/div[2]/div[4]/button").click() # Delete Image
        driver.switch_to.alert.accept() # Confirm delete
    except:
        pass
    
    print("Clear")
    driver.quit() # Quit tabs
