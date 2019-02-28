import webbrowser
from googleapiclient.discovery import build
import json
from pprint import pprint
import requests
from PIL import Image
import apistore #make your own, this is private data
APIKEY=apistore.APIKEY #assign your own API KEY
cxID=apistore.cxID  #assign your own custom search engine ID
##Open the term that was extracted from the speech in the default web browser
def openInBrowser(searchTerm):
    webbrowser.open_new_tab('https://www.google.com/search?tbm=isch&q='+searchTerm)

##Download the image for future implementation
def downloadImage(searchTerm):
    #use google custom search to retrieve the first image the serach returns
    service = build("customsearch", "v1",
            developerKey=APIKEY)
    res = service.cse().list(
      q=searchTerm,
      cx=cxID,
      num=1,
      searchType='image',
      fileType='jpg',
      safe='off',
    ).execute()
    #pprint(res)
    linkImg=""

    #extract link from returned JSON String
    for data in res['items']:
        linkImg=data['link']
        print(linkImg)

    #download image
    filename=searchTerm+'.jpg'
    f=open(filename,'wb') 
    f.write(requests.get(linkImg).content)

    f.close() 
    im = Image.open(filename)
    width=485
    height=270
    im=im.resize((485,270),Image.ANTIALIAS)
    im.save(filename)
    import unknown_support
    unknown_support.setImage(filename)
    

    #uncomment to open image automatically
    """
    img=Image.open(searchTerm+'.jpg')
    img.show()
    """