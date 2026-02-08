import time
import urllib.request
import os #creates f.e. folders

#Just print out thre dots with a delay for a cool show
def threedots():
    three_dots = "..."
    for char in three_dots:
        print(char,end="",flush=True)
        time.sleep(0.3)
    print("\n")

##################################################################################################################################


#print out names slowly for fancyness
def coolPrint(text, sleep = 0.1):
    for char in text:
        print(char, end ="",flush = True)
        time.sleep(sleep)


##################################################################################################################################


def downloader(file_links, token, chosendata, chosenregion):
    
    foldername = str(f"{chosendata}/{chosenregion}")

    os.makedirs(foldername, exist_ok= True)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    filelink = file_links[0]

    filename = filelink.split("/")[-1]

    filepath = os.path.join(foldername, filename)

    req = urllib.request.Request(filelink, headers = headers)

    open(filepath, "wb").write(urllib.request.urlopen(req).read())
    
    return