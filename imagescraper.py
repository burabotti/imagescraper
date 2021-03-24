import time
import schedule
import requests


time_to_wait = 5 # Looping time in seconds. The first download also takes this amount of time.
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/255px-Google_2015_logo.svg.png" # Image url


print("Waiting...")

def scrape_image():

    timestr = time.strftime("%d.%m--%H.%M.%S")
    hour = time.strftime("%H:%M:%S")
    response = requests.get(image_url)
    filename = str(timestr) + ".jpg"


    file = open(filename, "wb")
    file.write(response.content)
    file.close()
    print("Image saved..." + "\n Time:" + str(hour) + "\n##########" + "\n")

schedule.every(time_to_wait).seconds.do(scrape_image)

while 1:
    schedule.run_pending()
    time.sleep(1)
