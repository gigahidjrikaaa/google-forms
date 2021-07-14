Use this code to fill in a google form automatically.
The form I used in the code is a replica of a previous attendance form.

   1.  Download [Python](https://www.python.org/downloads/) 
   2.  Open cmd (command prompt) and type "pip install selenium" 
   3.  Download any code editor that can run python. I use [VS code](https://code.visualstudio.com/) with a [python extension](https://code.visualstudio.com/docs/languages/python).
   4.  Download [geckodriver (Mozilla Firefox)](https://github.com/mozilla/geckodriver/releases) or [chromedriver (Chrome)](https://chromedriver.chromium.org/downloads) or [msedgedriver (Microsoft Edge)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
   5.  After you install a driver go to the corresponding branch
   6.  Copy the code into the code editor (I don't recommend this as you don't learn anything, or at least understand the code) 
   7.  Change `config.json` accordingly (might need to change the email to add a number)  
for example from `{firstName}.{lastName}@student.tdsb.on.ca` to `{firstName}.{lastName}3@student.tdsb.on.ca`
   9.  Run it


If you want to use a specific driver, you need the corresponding browser.

------------------------------------------
To find an elements xpath:

First open the inspector
![step1](https://user-images.githubusercontent.com/75402062/124668587-176a7e00-de7f-11eb-8c1a-9da0f63c37f9.png)
Then select the element
![step2](https://user-images.githubusercontent.com/75402062/124668639-26e9c700-de7f-11eb-9d64-7873fadd7e9a.png)
Finally right click, select copy, and select xpath
![step3](https://user-images.githubusercontent.com/75402062/124668702-39640080-de7f-11eb-8e54-2215e936eb71.png)

Note that all the xpaths were fetched from google chrome but the example uses mozilla firefox
