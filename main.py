from twill.commands import *
import time
import utilities as ut
import navigate as nav
import access as ac


def main():

    #Login to the Website and retrieve the username
    ac.login()
    username = ac.get_username()

    print("\nWelcome ",end="")
    for char in username:
        print(char,end="",flush=True)
        time.sleep(0.3)
    print("\n")

    
    ####     Choose the Data-Collection that you want to get the Data from
    go("https://nrt3.modaps.eosdis.nasa.gov/archive/FIRMS")


    data_links = nav.LinkCleaner() #Method to retrieve only desirable links in a list

    data_foldernames = nav.LinkShort(data_links) #Last slash of a link, so you can see what folder you will follow

    data_foldernumber = nav.FolderChooser(data_foldernames) # get the one number of the enumerated links to follow; chosen by the user

    print("\nEntering folder: ", end ="")

    for char in data_foldernames[data_foldernumber]:
        print(char, end ="",flush = True)
        time.sleep(0.1)

    ut.ThreeDots() #print three Dots with a short delay



    ###   Follow the Link that has been chosen with the number with FolderChooser
    follow(data_links[data_foldernumber])
    

    ###   Choose the Region you want the Data for

    region_links = nav.LinkCleaner()

    region_foldernames = nav.LinkShort(region_links)

    region_foldernumber = nav.FolderChooser(region_foldernames) 


    print("\nEntering folder: ", end ="")
    
    for char in region_foldernames[region_foldernumber]:
        print(char, end = "", flush = True)
        time.sleep(0.1)

    ut.ThreeDots()


    ###   Follow the Link that has been chosen with the number with FolderChooser
    follow(region_links[region_foldernumber])


    ###  Download the Data

    
    ### Logout from the website
    ac.logout()

    
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



#prevents the script from running after the import
if __name__ == "__main__":
    main()