import sqlite3

### Database will be created if it doesn't exist
def dbcreation():

    conn = sqlite3.connect('FIRMS_Data.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Files
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        filename TEXT UNIQUE, 
        system TEXT,
        area TEXT, 
        date TEXT)''') #use ''' for blocks of text
    
    conn.commit()
    conn.close()

###################################################


### Check if the file already exists in the database
def dbexistfile(filename):
    conn = sqlite3.connect('FIRMS_Data.sqlite')
    cur = conn.cursor()

    # Select the data from the db where the filename matches the input
    cur.execute(
        "SELECT 1  \
        FROM Files \
        WHERE filename = ?", # if not ''' is used, then you have to add \ before new lines
        (filename,)
    )

    result = cur.fetchone() #Does the file exist?
    conn.close()

    return result is not None #return none if it doesn't exist
    

def dbdatainsert(filename,system,area,date):
    conn = sqlite3.connect('FIRMS_Data.sqlite')
    cur = conn.cursor()

    try:
        cur.execute('''INSERT INTO Files (filename,system,area,date) 
                VALUES (?,?,?,?)''',
                    (filename, system, area, date,) 
        )
    
    except sqlite3.IntegrityError:
        print(f"The file {filename} already exists.")
        pass

    conn.commit()
    conn.close()

