Use this code to fill in a google form automatically.

   1.  Download [Python](https://www.python.org/downloads/) 
   2.  Open cmd (command prompt) and type "pip install selenium" 
   3.  Download any code editor that can run python. I use [VS code](https://code.visualstudio.com/) with a [python extension](https://code.visualstudio.com/docs/languages/python).
   4.  Download [geckodriver (Mozilla Firefox)](https://github.com/mozilla/geckodriver/releases), [chromedriver (Chrome)](https://chromedriver.chromium.org/downloads) or [msedgedriver (Microsoft Edge)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it directly in the C:\ drive. If you know how paths work, place it wherever you want and change the path.
   5.  After you install a driver go to the corresponding folder
   6.  Copy the code into the code editor (I don't recommend this as you don't learn anything, or at least understand the code) 
   7.  Change `config.json` accordingly (might need to change the email to add a number)  
for example from `{firstName}.{lastName}@student.tdsb.on.ca` to `{firstName}.{lastName}7@student.tdsb.on.ca`
   9.  Run the `main.py` file


If you want to use a specific driver, you need the corresponding browser.

------------------------------------------
To find an elements xpath:

First open the inspector
![step1](https://user-images.githubusercontent.com/75402062/128521955-bc71050f-3748-443a-b092-0ad35ace52d4.png)
Then select the element
![step2](https://user-images.githubusercontent.com/75402062/128522125-0e027566-43b9-48a5-88bb-9254af0f91f8.png)
Finally right click, select copy, and select xpath
![step3](https://user-images.githubusercontent.com/75402062/128522228-c6e119e2-bdd0-4c20-8640-4db57b9f31d3.png)
Note that all the xpaths were fetched from google chrome but the example uses mozilla firefox
