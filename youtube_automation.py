import json
import time
import urllib.request as urllib
from selenium import webdriver

def open_video():
    api_key = "AIzaSyALnIX9P1s37TfhNE1pnOLW6bijOfHMu8Q"
    channel_id_2 = "user/PowerfulJRE"
    channel_id = "UCzQUP1qoWDoEbmsQxvdjxgQ"

    base_video_url = 'https.//www.youtube.com/watch?v='
    vidID = 'GO_rW0Bvy1I'

    url = 'https://www.youtube.com/watch?v=GO_rW0Bvy1I'

    driver = webdriver.Chrome('//ss002207//TAASPAL8$//Desktop//M122//chromedriver.exe')
    #driver.get(base_video_url + vidID)
    driver.get(url)
    time.sleep(3)
    driver.quit()


def check_for_new_video():

    api_key = "AIzaSyALnIX9P1s37TfhNE1pnOLW6bijOfHMu8Q"
    channel_id = "UCzQUP1qoWDoEbmsQxvdjxgQ"

    base_video_url = 'https.//www.youtube.com/watch?v='
    base_search_url = 'https://googleapis.com/youtube/v3/search?'
    base_search_url_2 = 'https://developers.google.com/youtube/v3/docs/channels/list?apix=true#try-it'

    url = base_search_url + 'key={}&channelID={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
    inp = urllib.urlopen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']
    video_exists = False

    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:
            driver = webdriver.Chrome('//ss002207//TAASPAL8$//Desktop//M122//chromedriver.exe')
            driver.get(base_video_url + vidID)
            video_exists = True

        if video_exists:
            with open('videoid.json', 'w') as json_file:
                data = {'videoId': vidID}
                json.dump(data, json_file)


open_video()

try:
    while True:
        check_for_new_video()
        print('No new video found!')
        time.sleep(30)
except KeyboardInterrupt:
        print('Youtube-Automation-Script is stopping')


