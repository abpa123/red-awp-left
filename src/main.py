#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from lib.log import *
from high_stakes.events import *

open_log("red-awp-left.csv")


def driver_function():
    pass


def autonomous_function():
    # Reset odometry to the starting autonomous position
    odometry.reset(PositionWithHeading(-1500, 600, -90))

    # Then try resetting it to GPS if GPS sensor is installed and reports high quality
    reset_odometry()

    intake_1st_stage.set_velocity(470, RPM)
    intake_2nd_stage.set_velocity(470, RPM)
    pid_driver.drive(-1000, True)
    clamp.set(True)
    pid_turner.turn(80, FRAME_HEADING_RELATIVE)

    reset_odometry()

    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)

    wait(1000, MSEC)
    reset_odometry()

    pid_driver.drive(550)
    pid_turner.turn(60, FRAME_HEADING_RELATIVE)
    pid_driver.drive(270)

    wait(1000, MSEC)
    reset_odometry()

    reset_odometry()

    pid_turner.turn(-80, FRAME_HEADING_RELATIVE)
    pid_driver.drive(-600, False)

    # pid_driver.drive(-150)
    # pid_turner.turn(120, FRAME_HEADING_RELATIVE)
    # intake_retract.set(True)
    # pid_driver.drive(1200)
    # intake_retract.set(False)

    # wait(1000, MSEC)
    # reset_odometry()

    # pid_driver.drive(-700)
    # pid_turner.turn(75, FRAME_HEADING_RELATIVE)
    # pid_driver.drive(-400)


init_event_handling()

# register the competition functions

competition = Competition(driver_function, autonomous_function)
