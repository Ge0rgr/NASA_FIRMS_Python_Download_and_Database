This script was specifically developed for the daily NASA FIRMS data.

The Python script downloads the daily NASA FIRMS fire data, which are provided as .txt files. The user logs into NASA through the script and selects the folder containing the data to be downloaded. In addition, a database is created to prevent duplicate downloads. During the download of the .txt files, a single .csv file is also generated, into which all data from the text files are appended.

The delimiters in the CSV file are adjusted for the use in Germany.

NASA uploads at least one new dataset every day. By running the script, users can easily save the latest (new) data.
