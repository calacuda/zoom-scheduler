# Zoom-Scheduler
This program runs in the background and will open zoom to specified links at specified times.


### Disclaimer
this program is not yet complete. is still has functionality that needs adding. see the
"TODO's" below for a list.


### Security/Privacy
it is HIGHLY recomended that you set up zoom to automatically mute you mic and not connect video
upon joining a call. this way no one can see or hear you untill you ready to be seen or heard.


### Compatibility
linux (Deffinatly), mac (Probably), window (Hopefully). I can not verify if it works on either
mac or windows becasue i don't have access to a mac or windows machine.


### First Setup/ Make New Schedule
run the "write_schedule.py" file with python3 by opening a terminal/comand prompt in this
programs directory and typing "python3 write_schedule.py". Answer the on schreen question but
remember the times need to be in [hh:mm] 24/hr format. so, if you had a meeting at 2:30pm you 
would answer "14:30" for the time.


### Updateing an Old Schedule
not implemented yet


### Running a Schedule
open a terminal/command prompt in this directory, and run the "run_schedule.py" file with
python3 the same way you did when setting up the schedule. Then LEAVE THE TERMINAL OR COMAND
PROMT OPEN. If it close the program will stop runnin. there are ways to avoid this, setting
up a system services on linux, but I don't know how to do the equivalent mac or windows.
that part would be up to you, the user.


### TODO's
1. write the run_schedule.py script.
2. implement teh ability to update an old schedule without manually editing the json
3. write a linux systemctl compatable system service to make life easier