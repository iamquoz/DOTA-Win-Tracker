# Dota Win Tracker
Plots a win / loss graph in DOTA over a set number of games





Differences over the original build include improved UX and some more sorting settings.



Available settings are:

* Game Version

* Lobby Type (normal/ranked/battle cup)

* Played Hero

* Only X recent games



Build instructions: 

* Download Python 3.8 from [Python.org](https://www.python.org/downloads/)

* Make sure to install pip and add Python to PATH

* Open command prompt and type in `pip install matplotlib==3.2.2` (we're using ver 3.2.2 due to [this issue](https://github.com/pyinstaller/pyinstaller/issues/5004) with Pyinstaller)

* Without closing the command prompt, type in `pip install requests`

* At this point, you should be able to just double click the win_tracker.py file and use it, but if you want to build it into an .exe, go to the next step

* In the command prompt, type in `pip install pyinstaller`

* Build the app into a single .exe file using `pyinstaller --onefile win_tracker.py`
 
* The executable will be in the `dist` directory next to the original .py file

Same requirements apply to building on Linux: install dependencies and install pyinstaller if you'd want to build your own binary. 


