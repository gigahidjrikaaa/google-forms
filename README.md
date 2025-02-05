# Google forms
Use this code to fill in a google form.

You can also use this to automate any browser task.

Backstory
---------------------------
When virtual learning started due to covid, we had a google form to fill in for attendance. At that time, I felt that it was pointless to fill-in and submit the same form everyday. So then, I decided to use python and automate this task. When I first starter this, it only worked on 1 browser. When I tested it on a differet browser, I realized that it had performed a bit differently. Now it has support for 3 different browsers.

Before using the code, not that selemium has bee updated and xpaths are used differently.
Now you would probably use

```py
from selenium.webdriver.common.by import By
...
driver.find_element(By.XPATH, '//*[@id="Email"]')
```



Instructions
---------------------------  
   1.  Download [Python](https://www.python.org/downloads/) along with pip (you will need to do this manually during the installation of python)
   2.  Open cmd (command prompt) and type `pip install selenium` 
   3.  Download any code editor that can run python. I use [VS code](https://code.visualstudio.com/) with a [python extension](https://code.visualstudio.com/docs/languages/python).
   4.  Download [geckodriver (Mozilla Firefox)](https://github.com/mozilla/geckodriver/releases), [chromedriver (Chrome)](https://chromedriver.chromium.org/downloads) or [msedgedriver (Microsoft Edge)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it directly in the C:\ drive. If you know how paths work, place it wherever you want and change the path. (Windows only) if you use Linux/MacOS you should know how to use paths on said OS
   5.  After you install a driver go to the corresponding folder
   6.  Download the files
   7.  Change `config.json` accordingly 
   8.  You might need to change the email in the `main.py` file to add a number 
for example from:  
`{firstName}.{lastName}@student.tdsb.on.ca` to `{firstName}.{lastName}7@student.tdsb.on.ca`<br>
    you might need to change the email depending on the form and your domain.
   9.  Run the `main.py` file

Notes
------------------------------------------  

 - You could open the file with a normal text editor, and run the file from the command line.

 - If you want to use a specific driver, you need the corresponding browser.

To find an elements xpath:

First open the inspector
![step1](https://user-images.githubusercontent.com/75402062/128521955-bc71050f-3748-443a-b092-0ad35ace52d4.png)
Then select the element
![step2](https://user-images.githubusercontent.com/75402062/128522125-0e027566-43b9-48a5-88bb-9254af0f91f8.png)
Finally right click, select copy, and select xpath
![step3](https://user-images.githubusercontent.com/75402062/128522228-c6e119e2-bdd0-4c20-8640-4db57b9f31d3.png)


All the xpaths were fetched from Google Chrome but the examples use Mozilla Firefox

All code is working as of August 26th, 2021
