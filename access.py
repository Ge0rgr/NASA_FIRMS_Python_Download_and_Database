import re
import sys
from twill.commands import *
import getpass
import urllib.request
from bs4 import BeautifulSoup as bs
from utilities import coolPrint

def login():

    #### if by any chance loggged in, then logout first
    go("https://urs.earthdata.nasa.gov/logout")

    ######    Go to nasa login site and log in
    go('https://urs.earthdata.nasa.gov/')

    mail = ""
    passw = ""


    #User has to make an input for mail and password; if you cannot log in, you have to re-enter the mail and password
    while True:

        if mail == "" :
            mail = input('Please enter your email (Enter "." to quit): ')

            if mail == ".":
                sys.exit()

            y = bool(re.fullmatch(r"^[^@\s]+@{1}[^@\s]+$",mail)) #Check if it's a valid mail (simple check, no more than one @ and no whitespace)
            if y == False:
                print ("Please enter a valid email")
                mail =""
                continue
        if passw =="":
            passw = getpass.getpass("Please enter your password: ", echo_char="*")
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


#####################################################################################


def get_username():

    go('https://urs.earthdata.nasa.gov/profile')

    html_content = browser.html  # Capture raw HTML
    html_words = html_content.split() #Split words of html into a list

    substring = "Username:" #Will be searched for in the html document in order to retrieve the Username

    #go through enumerated list and find the first(because of next) index of the word, which contains the Substring Username. If not found: enter -1
    # word_index for word_index: Both have to have the same name. Right word_index represents the enumeratin value and the left one will be returned 
    #(if left has differend name, then the programm doesn't know what to return (like in word_index, word = (3, "Username:"), then return the number 3))
    tmp = next((word_index for word_index, word in enumerate(html_words) if substring in word),-1)

    #If no Username detected, close the script;  
    if tmp == -1:
        print("ERROR: No Username found\n")
        sys.exit("Existing Account without a Username is not possible") 


    #username is needed to access to download token
    username = html_words[tmp + 1].strip()

    return username


##############################################################################################

    #####    Retrieve download token (Bearer Token) from the user profile
def get_downloadtoken(username):

    token =""
    buttonspressed = 0

    while token == "":

        go(f"https://urs.earthdata.nasa.gov/users/{username}/user_tokens") ##get Token here

        html_content = browser.html

        soup = bs(html_content,"html.parser")

        dotoks = []

        #Retrieve Existing Tokens from html
        for tok in soup.find_all("input"):
            if tok.get("id") == ("clippy"):
                    dotoks.append(tok["value"])

        if len(dotoks) == 0: #if no tokens exist, generate one
            buttonspressed = buttonspressed +1
            submit() #generate token

        elif len(dotoks) == 1: #if one token exists, but you didn't generate it for this purpose, then generate a new one
            match buttonspressed:
                case 0:
                    #generate Token
                    submit(None,"2")
                    buttonspressed = buttonspressed +1
                case 1: #if on token exists, because you generated one with the script, then take that one
                    token = dotoks[0]
                    return token
            
        elif len(dotoks) == 2: #if 2 (maximum possible) tokens exist, then take newest one
            token = dotoks[1]
            return token


##########################################################################################################




def logout():
    go("https://urs.earthdata.nasa.gov/logout")
    print("\n Successfully logged out from the Website\n")

    text = "\nThank you!"
    coolPrint(text,0.2)
    print("\n")
    