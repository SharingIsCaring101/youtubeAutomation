import webbrowser
from selenium import webdriver
import time

url = 'https://pythonexamples.org'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Users//TAASPAL8//AppData//Local//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open_new(url)


driver = webdriver.Chrome('//ss002207//TAASPAL8$//Desktop//M122//chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.youtube.com/channel/UCzQUP1qoWDoEbmsQxvdjxgQ');
time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
driver.quit()