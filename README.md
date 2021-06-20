Use this code to fill in a google form automatically.
The form I used in the code is a replica of a previous attendance form.

   1.  Download [python](https://www.python.org/downloads/) 
   2.  Open cmd (press windows key and type cmd.exe) and type "pip install selenium" 
   3.  Download any code editor that can run python. I used [VS code](https://code.visualstudio.com/) 
   4.  Download [geckodriver (Mozilla Firefox)](https://github.com/mozilla/geckodriver/releases) or [chromedriver (Chrome)](https://chromedriver.chromium.org/downloads) or [msedgedriver (Microsoft Edge)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
   5.  After you install a driver go to the corresponding branch
   6.  Copy the code into the code editor (I don't recommend this as you don't learn anything, or at least understand the code) 
   7.  Change 'student id', 'password', 'First name', and 'Last name' to your info and run the program ('firstname.lastname@student.tdsb.on.ca' is aumatically changed with the f-string)
   8.  Run it

If you encounter a "Unable to locate element" error, add "time.sleep()" above the line with the error and re-run it.
If there is alreeady a time.sleep() increase the value.

You will encounter an error if you directly copy ```time.sleep()```
Not gonna explain it so you people actually learn

If you want to use a specific driver, you need the corresponding browser.

------------------------------------------

### Todo

- [x] Firefox users
- [x] Edge users


