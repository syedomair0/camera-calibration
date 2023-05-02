                            
                                                         ^
an attempt at solving the [https://github.com/commaai/calib_challenge](comma ai calibration challenge)

the problem is that when trying to detect the motion of travel from a dashcam the dashcam could not be installed perfectly
and may be at an angle. the goal of this project is to see how we can detect the angle at which the camera is at and calibrate it
so we have cleaner data which can be applied to autonomous driving systems.

there is data provided which are basically 5 labeled dashcam videos and 5 unlabeled videos available for testing and a script that checks
the error. 

possible attempts
    - train a neural network to detect the motion of travel ? 
    - use methods like optical flow, structure from motion, and SLAM algorithms. 

progress so far
    - used the opencv library to detect motion of travel but it seems to be buggy and I can't seem to extract the angle at which the camera
      is installed.



![car movement gif](./motion_direction.mov)

