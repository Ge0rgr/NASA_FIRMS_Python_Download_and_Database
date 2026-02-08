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

    print()
    for i,dat in enumerate(file_links, start = 1):

        filename = dat.split("/")[-1]

        filepath = os.path.join(foldername, filename)

        req = urllib.request.Request(dat, headers = headers)

        print("Downloading file ", i, "of ", len(file_links))

        open(filepath, "wb").write(urllib.request.urlopen(req).read())

    return