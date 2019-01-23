##Open the term that was extracted from the speech in the default web browser

import webbrowser
def openInBrowser(searchTerm):
    webbrowser.open_new_tab('https://www.google.com/search?tbm=isch&q='+searchTerm)