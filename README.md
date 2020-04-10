![Jackbox Party Crasher](banner.png)

This program quickly tries random 4 character long codes as Jackbox.tv codes to attempt to join random games. 

## Description
This program uses PyAutoGUI to type several codes of 4 characters into https://jackbox.tv/ in an attempt to join a random game. The program will first ask the user how many games are being stored in the Past Games menu of the site as this affects how the code field is selected. Once that number is found, the program begins with a countdown (results may vary) and then begins typing the codes and pressing enter accordingly. The user, before the countdown concludes, must have selected the code field (empty or with all text selected ideally, though this theoretically shouldn't matter). 

### Notes
Depending on the various errors that Jackbox may serve, results, success, and experience will likely vary quite a lot. In one case, I got a game on the first code. For others, it took most of the 100 tries or I ended up with an unexpected error that threw the automation plan out the window.

There is a time.sleep() function with a parameter of 0.2. If the automation takes too long for your liking, you may certainly try decreasing that number (I recommend starting with 0.1 and then cutting it in half until you experience issues). I found that with my slower internet connection, 0.2 worked best for me.

**Important:** As soon as you notice you've found a working code, immediately switch to the terminal and press "Ctrl - C" to stop the program! I do not have an automatic stop worked into the program so you must force quit it with Ctrl-C. If you don't do this nearly immediately, unexpected behaviour will occur!

### Requirements
You will need to install pyautogui with pip if you haven't already.

In addition, this program has a vocal countdown that's narrated by the system voice but it is using os and the "say" command for MacOS. You may wish to remove that functionality completely (though I recommend leaving at least the time buffer) or change it to work with your operating system.

main.py does rely on isInt.py.
Feel absolutely free to use isInt.py in your own programs, I probably got it from someone else along the way and it's very useful.

---
I *highly* encourage anyone taking a look at this to fork the program and improve it. I did not spend a ton of time on this as it was mostly a Proof of Concept. It was written in 20-30 mins. It is **not** designed to be flawless and it most certainly isn't, just as most programs aren't.

Please note that I am not in any way associated with Jackbox Games.
