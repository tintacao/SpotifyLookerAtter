# SpotifyLookerAtter
Check some Spotify Stats

*USES PYTHON3.8*

Check out Most Popular stats for Streaming and for Playlists. 

NOTE: If you have more than 3 playlist files or 5 streaming files, the program will not scan all of them. That's only because I figured those were good cut-off points. If you have more files let me know and I will update the code to accomodate them.


After Downloading Spotify Data, extract the files and open the extracted folder.
  On Windows: Right-Click, "Extract All"
  On Mac: This is done automatically -- the extracted folder is placed in the same folder as the .zip 

Paste the "analysis.py" file right into the "MyData" folder. Run the file using Terminal, IDLE, CMD, or PowerShell.


------------------------------------

***If you have literally no idea how to use Terminal, CMD, or PowerShell, read below***

:
:

*For Windows*

  Make sure Python is up to date
  
    Open Command Prompt: Open the Search Bar, type "cmd", hit enter
    Check Python Version: type "py" into CMD. If its not Python3.x you can download it here: https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe
    
  Use Command Prompt (CMD) to run the file:
  
    Open a new CMD window.
    Type "cd" into CMD, add a space, then paste the Location you copied (it will look something like C:\Users\UserName\Folder\my_spotify_data\MyData). Press Enter.
    Type "analysis.py", press Enter.
    
  Use PowerShell (PS):
  
    SHIFT+RightClick on the *background* of the folder with the analysis.py file, and click "Open PowerShell Window Here"
    Type "py analysis.py" to run the file. Press Enter.
 
*For Mac*

  Make sure Python is up to date
  
    Open Terminal: Press CommandKey + Space to open Search, type "terminal", and click it. (In Finder: its under Utilities)
    Type "python -- version". Hit Enter. If it says something like python2.7.3, type "python3 -- version." 
    If python3 is not installed you can install it here: https://www.python.org/ftp/python/3.8.5/python-3.8.5-macosx10.9.pkg
   
  Use Terminal to run the File
    
    Right-click analysis.py, hold the option key and Click "Copy analysis.py as Pathname"
    Open Terminal, type "cd", add a space, and paste. (It should end with ...\my_spotify_data\MyData. If there is "analysis.py" on the end, delete up to "\MyData")
    Type "python3 analysis.py"
 


