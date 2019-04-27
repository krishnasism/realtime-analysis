# Realtime Data Analysis
The internet is increasing at a fast rate, therefore, there is also a hurry to present a set of data to your client. So, welcome to a project that understands what you are talking about and shows relevant information about it. Or, if you are in a noisy room, just type it in!

## What it looks like 
This is a screenshot, after a topic has been searched for. This is the screen where you can find the relevant data.
![OutputScreen](https://user-images.githubusercontent.com/21293324/56851284-ec915080-692a-11e9-9816-96d1f5561343.png)

## Anatomy of the screen
* The top text bar is the place to type in a query, or to enable the voice feature by clicking on the button.
* The first label - "indian elections" is the query that is being currently looked for
* The first image on the left most side, is a image from google images. 
* The second images, where the graph is being shown, is the general sentiment of twitter users. 
* The third image, on the right most side, is a screenshot of Google news.
* The bottom list, is a list of tweets summarized, by a novel summarization algorithm, using cluster based summarization techniques.

## Installing the project
### The automatic way but might not work always! 
* Navigate to setup directory
* Run the setup.bat

### The manual way
For non-Windows users(and for Windows users for whom the setup.bat file didn't work), please install manually. Follow the steps below : 
* Navigate to the setup folder in Command Prompt, or a shell
```
pip install -r requirements.txt
```
or
```
python -m pip install -r requirements.txt
```
This will download and install the required libraries. 
## Install tweet-preprocessor-0.4.0.zip
```
pip install YOUR_CURRENT_DIRECTORY_PATH/libs/tweet-preprocessor-0.4.0.zip
```
or

```
python -m pip install YOUR_CURRENT_DIRECTORY_PATH/libs/tweet-preprocessor-0.4.0.zip
```

This library is not hosted properly online, therefore you have to install the .zip file that is provided. Simply follow the step above. Example after replacing YOUR_CURRENT_DIRECTORY_PATH
```
pip install C:\Users\Krishnasis\Desktop\your-powerpoint-realtime\setup\libs\tweet-preprocessor-0.4.0.zip
```
or
```
python -m pip install C:\Users\Krishnasis\Desktop\your-powerpoint-realtime\setup\libs\tweet-preprocessor-0.4.0.zip
```

### Running
* Simply navigate to the previous folder, i.e., root. 
* Run the run.bat file 
or 
```
python unknown.py
```
You will get a window(hopefully).
Have fun!
