# XboxHawkEye

Uses selenium web automation to check if the new Xbox Series X is in stock at Walmart, Target, Amazon, and Bestbuy.
If found it will auto add the xbox to your cart and emit a loud 10 second beep to notify you to hurry up and check out. 

# Requirements 
Must have python 3, selenium, and pyautogui installed.

**Install on Windows**
1. install python 3.8 from the main python website by naviagting to https://www.python.org/downloads/release/python-386/ and using the "windows x86-64 executable installer" and installing like any other windows program.

2. after install open a powershell command prompt and run the following commands to update pip and install selenium/pyautogui
  a. cd .\AppData\Local\Programs\Python\Python38\
  b. .\python.exe -m pip install --upgrade pip
  c. .\python.exe -m pip install selenium
  d. .\python.exe -m pip install pyautogui

You can now run xboxHawkEye by double clicking on xboxHawkEye.py <br />
**Note**:
You may need to right click on xboxHawkEye.py and select "open with" and choose "python" to run for the first time.)
