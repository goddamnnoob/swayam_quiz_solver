# swayam_quiz_solver
  A Python script that brutefore answers and finds the correct one. Swayam validates the answers client side also expose the score after every submission, by using this data I wrote a simple python script that completes every single answer 4 choices MCQs for you. It doesn't work with multiple answer quizes it is possible to bruteforce them too but that would put heavy load on the backend servers which might end up as DOS.
## Usage: 
  * Specify path for driver or create a drivers directory and add the driver file there
  * Make sure the driver works with the browser 
  $ python3 swayamscript.py
  * Browser will open signin and navigate to the assignment page 
  * Press enter in the terminal/CMD
  * Wait 3 to 4 minutes 
## Libraries & Drivers:
 * Selenium $ pip3 install selenium
 * [Firefox driver](https://github.com/mozilla/geckodriver/releases/latest)
 * Check your chrome version using https://settings/help
 * [Chrome driver](https://chromedriver.chromium.org/downloads) 
