from twill.commands import *
import sqlite3
import re
import sys
import time
from bs4 import BeautifulSoup
from DD_methods import *

'''
######    Go to nasa login site and log in

go('https://urs.earthdata.nasa.gov/')

mail = ""
passw = ""


#User has to make an input for mail and password; if you cannot log in, you have to re-enter the mail and password
while True:

    if mail == "" :
        mail = input('Please enter your email (Type "." if you do not wish to continue): ')

        if mail == ".":
            sys.exit()

        y = bool(re.fullmatch(r"^[^@\s]+@{1}[^@\s]+$",mail)) #Check if it's a valid mail (simple check, no more than one @ and no whitespace)
        if y == False:
            print ("Please enter a valid email")
            mail =""
            continue
    if passw =="":
        passw = input("Please enter your password: ")
        continue

    #Enters the username and password in the form
    fv("1", "username", mail)
    fv("1", "password", passw)


    submit() #presses the commit button to log in


    login_content = browser.html  # Capture raw HTML
    login_lines = login_content.split("\n") #Split lines of html into a list


    substring = "Invalid username or password" #Will be searched for in the html document in order to retrieve the info if login was successful or not


    failed = False

    #if substring is found, then login has failed
    for lines in login_lines:
        if substring in lines:
            failed = True


    if failed == False:
        print("\nSuccess, you're logged in!\n")
        break

    elif failed == True:
        print("\n Wrong e-mail or password. Try Again. \n")
        mail = ""
        passw = ""
        continue

#Delay for visual purposes
#time.sleep(2)

####          Go to nasa user-profile to retrieve the username

go('https://urs.earthdata.nasa.gov/profile')

html_content = browser.html  # Capture raw HTML
html_words = html_content.split() #Split words of html into a list

substring = "Username:" #Will be searched for in the html document in order to retrieve the Username

#go through enumerated list and find the index of the word, which contains the Substring Username. If not found: enter -1
tmp = next((i for i, word in enumerate(html_words) if substring in word),-1)

#If no Username detected, close the script;  
if tmp == -1:
    print("ERROR: No Username found\n")
    sys.exit("Existing Account without a Username is not possible") 


#username is needed to access to download token
username = html_words[tmp + 1].strip()
print("\nRetrieving your Username: ")

#Cool way of displaying username
for char in username:
    print(char,end="",flush=True)
    time.sleep(0.3)

print("\n")

#time.sleep(2)
'''



####     Choose the Data-Collection that you want to get the Data from

go("https://nrt3.modaps.eosdis.nasa.gov/archive/FIRMS")


data_links = LinkCleaner() #Method to retrieve only desirable links in a list


data_foldernames = LinkShort(data_links) #Last slash of a link, so you can see what folder you will follow


data_foldernumber = FolderChooser(data_foldernames) # get the one number of the enumerated links to follow; chosen by the user

print("\nEntering folder: ", data_foldernames[data_foldernumber],"\n" )


ThreeDots() #print three Dots with a delay


###   Follow the Link that has been chosen with the number from FolderChooser
follow(data_links[data_foldernumber])
 



###   Choose the Region you want the Data for


region_links = LinkCleaner()

region_foldernames = LinkShort(region_links)

region_foldernumber = FolderChooser(region_foldernames) 


print("\nEntering folder: ", region_foldernames[region_foldernumber], "\n")

ThreeDots()

###   Enter the folder that has been chosen

follow(region_links[region_foldernumber])



'''
###  Download the Data



#Logout from Website

go("https://urs.earthdata.nasa.gov/logout")
print("\n Successfully logged out from the Website\n")






#####    for download token
#baseurl = "https://urs.earthdata.nasa.gov/users/"

#html = urllib.request.urlopen("https://urs.earthdata.nasa.gov/users/")

#soup = bs(html)
#print(soup)

#url = baseurl + str(start) + '/' + str(start + 1)

#text = "None"


#document = urllib.request.urlopen(url, None, 30, context=ctx)
#text = document.read().decode()
#if document.getcode() != 200 :
#    print("Error code=",document.getcode(), url)

'''