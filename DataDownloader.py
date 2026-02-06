from twill.commands import *
import sqlite3
import re

go('https://urs.earthdata.nasa.gov/oauth/authorize?response_type=code&client_id=sXTOeM-6RH5fuK3TacT_Ag&redirect_uri=https%3A%2F%2Fnrt3.modaps.eosdis.nasa.gov%2Foauth%2Fcallback&state=E53GLmbJWzjzsbXk2FG7XK9MeSjk1v')

mail = ""
passw = ""


#User has to make an input for mail and password; if you cannot log in, you have to re-enter the mail and password
while True:


    if mail == "" :
        mail = input('Please enter your email (Type "." if you do not wish to continue): ')

        if mail == ".":
            break

        y = bool(re.fullmatch(r"^[^@\s]+@{1}[^@\s]+$",mail)) #Check if it's a valid mail (simple check, no more than one @ and no whitespace)
        if y == False:
            print ("Please enter a valid email")
            mail =""
            continue
    if passw =="":
        passw = input("Please enter your password: ")
        continue

    fv("1", "username", mail)
    fv("1", "password", passw)


    submit()


    login_content = browser.html  # Capture raw HTML
    login_lines = login_content.split("\n") #Split words of html into a list


    substring = "Invalid username or password" #Will be searched for in the html document in order to retrieve the Username

    #go through enumerated list and find the index of the word in sp, which contains the Substring Username. If not found: enter -1
    tmp = next((i for i, word in enumerate(login_lines) if substring in word),-1)

    if tmp == -1:
        print("Success, you're logged in")
        break
    elif tmp != -1:
        print("Wrong e-mail or password. Try Again. ")
        mail = ""
        passw = ""
        continue
    

'''
    #If no Username detected, close the script
    if tmp == -1:
        print("Success")
        break

    else:
        print("Login failed. Please enter a valid email and password.")
        continue




go("https://urs.earthdata.nasa.gov/users/")



html_content = browser.html  # Capture raw HTML
html_words = html_content.split() #Split words of html into a list

substring = "Username:" #Will be searched for in the html document in order to retrieve the Username

#go through enumerated list and find the index of the word in sp, which contains the Substring Username. If not found: enter -1
tmp = next((i for i, word in enumerate(html_words) if substring in word),-1)

#If no Username detected, close the script
if tmp == -1:
    print("No Username found")
    exit() 


username = html_words[tmp + 1].strip()
print("Username:", username)


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