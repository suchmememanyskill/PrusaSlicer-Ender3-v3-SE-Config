# Pre Print Info 

On the stock firmware, just before starting a print, statistics like estimated time, filament used and layer height are displayed. 
Anything sliced currently with this profile will not show these statistics. But there is a way to make that work using a post processing script

## Setup (Dotnet AOT, faster, Windows only)
1. Download [PrintMetadataRelocator.exe](https://github.com/suchmememanyskill/PrusaSlicer-Ender3-v3-SE-Config/releases/latest/download/PrintMetadataRelocator.exe)
2. Copy the file somewhere and note down its full path. 
    - To geht the full path in Windows, hold the shift key on your keyboard and do a right-click on PrintMetadataRelocator.exe. Then click ob copy path. This does add quotes to the path but you can just remove those.
    - For this example, i'll place it on the root of my C:/ drive
3. Open PrusaSlicer
    - Make sure you are in 'Expert' mode
4. Go to Print Settings then Output Options
5. Enter the following into the Post-processing scrips field: `C:\PrintMetadataRelocator.exe;`
    - Replace `C:\PrintMetadataRelocator.exe` with the actual location of the file
6. Optionally save the print profile settings
    - You have to apply this for each print (speed, layer height) profile

## Setup (Python, slower, Cross Platform)
0. This uses a Python script to modify the .gcode after prusaslicer generates it. Please install the latest version of Python before proceeding. Make sure to check 'Add to PATH' during installation, otherwise this will not work.
1. Download [info.py](https://raw.github.com/suchmememanyskill/PrusaSlicer-Ender3-v3-SE-Config/main/img/info.py) from this repo
    - If you see text instead of getting a file download, right click the page and select 'Save As'
2. Copy the file somewhere and note down its full path. 
    - Windows makes it unneseseraily difficult to get the full path from something. I'm unsure if this in standard windows, but i can right click a file > Copy as Path. This does add quotes to the path but you can just remove those
    - For this example, i'll place it on the root of my C:/ drive
3. Open PrusaSlicer
    - Make sure you are in 'Expert' mode
4. Go to Print Settings then Output Options
5. Enter the following into the Post-processing scrips field: `C:\Windows\py.exe C:\info.py;`
    - This will only work on Windows, but you can ajust it to work on other OS' too
    - Replace `C:\info.py` with the actual location of the file
6. Optionally save the print profile settings
    - You have to apply this for each print (speed, layer height) profile

## Result

After doing this, after 'Export G-Code' a command prompt will open for a split second, and your .gcode files will now contain the needed metadata for the display to work. Enjoy!
