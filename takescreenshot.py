def takescreenshot(query):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import unknown_support

    CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    CHROMEDRIVER_PATH = 'chromedriver.exe'
    WINDOW_SIZE = "1366,768"

    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                            chrome_options=chrome_options
                            )  
    driver.get("https://news.google.com/search?q="+query+"&hl=en-IN&gl=IN&ceid=IN%3Aen")
    driver.get_screenshot_as_file("screenshotOfWebPage.png")
    driver.close()

    import cv2
    from PIL import Image
    
    #crop
    img = cv2.imread("screenshotOfWebPage.png")
    crop_img = img[70:740, 280:980]
    cv2.imwrite("screenshotOfWebPage.png",crop_img)

    #resize
    im=Image.open("screenshotOfWebPage.png")
    width=350
    height=600
    im=im.resize((width,height),Image.ANTIALIAS)
    im.save("screenshotOfWebPage.png")
    
    unknown_support.setNewsImage()
