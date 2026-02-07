from bs4 import BeautifulSoup
from twill.commands import *
import re

# link_cleaner requires that you entered a link with go([Link]) or follow([Link] with twill in the main file)
# returns a list of links of the html site (with undesirable Links removed (for my personal purpose))

def LinkCleaner():

    data_content = browser.html  # Capture raw HTML

    soup = BeautifulSoup(data_content,"html.parser")
    data_links = []

    #Retrieve specific links that are saved in html and add them to a list
    for link in soup.find_all("tr"):
        if link.has_attr("data-href"):
            data_links.append(link["data-href"])


    # remove unwanted links from the list
    substring = "https" 

    tmp_data_links = []

    for link in data_links:
        if substring in link:
            tmp_data_links.append(link)

    data_links = tmp_data_links

    return data_links


#####################################################################################################################################


# Takes the last slash value from a link (https://nrt3.modaps.eosdis.nasa.gov/archive/FIRMS/noaa-21-viirs-c2/Europe/ -> Europe)
# requires a list and returns a list

def LinkShort(list_links):

    #Save just the Folder names for visual presentation (and to get used to regex)
    data = []

    for foldername in list_links:
        x = re.findall(r"/([^/]+)/$",foldername) #has a slash, then extract that (what has one or more non slash characters); and has a Slash at the end, where after that, nothing follows
        if x:
            data.append(x[0])
    
    return data


#####################################################################################################################################

# asks the user for a number input, with which the user can follow a link to the desired folder
# this method itself doesn't follow the link, it has to be done manually in the main file
# it returns the number representing the folder that the user wants to follow

def FolderChooser(FoldersToChoose):

    print("\n\n From which Data-Collection do you want to download the Data?\n")

    for i,val in enumerate(FoldersToChoose): #enumerate the list to have to user choose a number connected to the links
        print(i,val)


    folder = int(input("\n Please enter the number to the left of the desired folder: "))

    #only continue when a valid number is entered
    while True:
        if folder not in range(0,len(FoldersToChoose)):
            print("\n Please enter a valid number (0 -",len(FoldersToChoose)-1,") : ")
            folder = int(input())
        elif folder in range(0,len(FoldersToChoose)):
            break

    return folder

################################################################################################################################