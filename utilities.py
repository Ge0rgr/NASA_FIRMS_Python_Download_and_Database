import time 
import datetime
import urllib.request
import os #creates f.e. folders
from pathlib import Path
import databasehandling as dbh

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
    
    while True:
        try:
            dbh.dbcreation()



            ### Change save dir for the downloaded files, current default is the same dir as where the script is saved

            '''
            save_location = Path.home()/"Downloads" #make the home Download folder the default one 
            

            print("\nWhere do you want to save the data (press enter for C:\\Users\\[username]\\Downloads) \nWrite path like D:\\[folder]\\ ,or else data will be saved in the same folder as the script :")
            userlocation = input()
            

            if userlocation != "":
                save_location = userlocation

            foldername = str(f"{save_location}/{chosendata}/{chosenregion}")
            '''

            foldername = str(f"{chosendata}/{chosenregion}")

            print("\nStarting download", end="")
            threedots()
            print("\n")

            os.makedirs(foldername, exist_ok= True) #create folders for the downloaded files

            headers = {
                "Authorization": f"Bearer {token}" ##out downloadtoken into the request header
            }

   
            for i,dat in enumerate(file_links, start = 1):

                filename = dat.split("/")[-1]

                year = int(filename[-11:-7])

                dayofyear=int(filename[-7:-4])

                tmpdate = datetime.date(year,1,1) + datetime.timedelta(days=dayofyear -1) #Takes first day of the year and adds the day of the year to it, then reformats it

                currdate = tmpdate.strftime("%d.%m.%Y") #reformat to dd.mm.YYYY

                if dbh.dbexistfile(filename):
                    print(f"The file {filename} already exists and will be skipped\n")
                    continue 

                filepath = os.path.join(foldername, filename) #create the correct path for the intended save location

                req = urllib.request.Request(dat, headers = headers)

                print("Downloading file ", i, "of ", len(file_links))

                open(filepath, "wb").write(urllib.request.urlopen(req).read())
            
                dbh.dbdatainsert(filename,chosendata,chosenregion,currdate)
                

        except FileNotFoundError:
            print("\nPlease enter a valid save location\n")
    

        return


#################################################################