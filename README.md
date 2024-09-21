# red-awp-left 
This is VEX team 21919A's program for the autonomous win point on the left side of the red alliance side of the field. The location of this quadrant is highlighted below in the image with a picture of the field. Below that is a diagram of the autonomous path that we create in advance to display the locations our robot will be in due to our PID programming that we have implemented in our code.

## Organization of the Repository
You may notice that this repository is unlike most other VEX robotics Github repositories. Instead of multiple files being contained in one repository and a primary `main.py` file that contains all the code for running the robot along with the code for the autonomous routines. Most VEX repositories, including the default that VEX provides will contain something that looks similar to the following:

```python
def vexcode_auton_function():
   auton_task_0 = Thread(onauton_autonomous_0) # call main autonomous function
   while(competition.is_autonomous() and competition.is_enabled()):
       wait(10, MSEC) # wait for reset time period
   auton_task_0.stop()
```

Instead, our team employs more of a library-based approach, in which we create repositories that are created by using a template repository that has no autonomous code written into it, called high-stakes-manual. On Github, we can create this repository as a template and simply use the "create new from template" button to create a new repository that essentially makes a copy of the high-stakes-manual repository. The link to the repository is the following: https://github.com/hatatat-dev/high-stakes-manual. 

Inside of this template repository is a file called `preprocessed.py`, which is a file that contains all the code for our robot and is read-only, meaning the code can be run but never changed. In order to make any changes to the this file, they will have to be done in our other large github repository, telemetry, which is where all of our individual files are located, analogous to the files one might find in a typical VEX Github Repository. This allows our code to be more organized.

The only thing that we are now required to do now is create a few actual code functions for defining the autonomous functions, making everything much easier to manage and find. The first thing we need to create is `autonomous_function()`, which defines the code we will use for that autonomous function. The next thing we need to do is to simply add a `driver_function()` and a `competition` line statement. We do this will the following code segments:

```python

def driver_function():
    pass # nothing needed for the driver_function in this case
```

```python
# register the competition functions
competition = Competition(driver_function, autonomous_function)
```


## Location on Field
![redleft](https://github.com/user-attachments/assets/de5f090e-35a6-4e43-a173-d8779351d911)

## Autonomous Path
<img src=svgs/autonomous.svg width="300" height="300"/>
