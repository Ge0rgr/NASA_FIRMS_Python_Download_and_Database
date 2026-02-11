from twill.commands import *
import time
import utilities as ut
import navigate as nav
import access as ac

def main():
 
    #Login to the Website, retrieve the username and downloadtoken
    ac.login()

    
    username = ac.get_username()

    print("\nWelcome ",end="")
    ut.coolPrint(username,0.3)
    print("\n")

    dtoken = ac.get_downloadtoken(username)

    print("\nretrieving your download token",end="")
    ut.threedots()
    print("\n")
    
    
    ####     Choose the Data-Collection that you want to get the Data from
    go("https://nrt3.modaps.eosdis.nasa.gov/archive/FIRMS")

    
    data_links = nav.linkCleaner() #Method to retrieve only desirable links in a list
    
    data_foldernames = nav.linkShort(data_links) #Last slash of a link, so you can see what folder you will follow
    
    data_foldernumber = nav.folderChooser(data_foldernames) # get the one number of the enumerated links to follow; chosen by the user

    chosendata = data_foldernames[data_foldernumber]

    print("\nEntering folder: ", end ="")


    ut.coolPrint(data_foldernames[data_foldernumber])

    ut.threedots() #print three Dots with a short delay



    ###   Follow the Link that has been chosen with the number with FolderChooser
    follow(data_links[data_foldernumber])
    

    ###   Choose the Region you want the Data for

    region_links = nav.linkCleaner()

    region_foldernames = nav.linkShort(region_links)

    region_foldernumber = nav.folderChooser(region_foldernames) 

    chosenregion = region_foldernames[region_foldernumber]

    print("\nEntering folder: ", end ="")
    
    ut.coolPrint(region_foldernames[region_foldernumber])

    ut.threedots()


    ###   Follow the Link that has been chosen with the number with FolderChooser
    follow(region_links[region_foldernumber])


    ###  Download the Data nad possibly create a .csv with the downloaded data
    file_links = nav.linkCleaner()

    ut.downloader(file_links,dtoken,chosendata, chosenregion)


    print("\nDownload complete!\n")


    ### Logout from the website
    ac.logout()
    

 #prevents the script from running after the import
if __name__ == "__main__":
    main()   

    


