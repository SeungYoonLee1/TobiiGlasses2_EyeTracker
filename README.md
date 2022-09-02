## TobiiGlasses2_EyeTracker
## Getting started

#### This repository was created based on the code I made myself when I was in college.

https://github.com/ddetommaso/TobiiGlassesPyController

#### If you wish to use the code written here to use 'Tobii Glasses', please download the required module from the GitHub page above and add this code to the required part.

#### I would like to express my sincere gratitude to the GitHub page manager above for providing this module and solving my questions.

## Code Execution Results
### 1. get_video_text.py 
#### The code that records the video with the eye tracker and receives the gp(gaze_point) as a text file
![Untitled](https://user-images.githubusercontent.com/69844293/182260090-94dcd6a4-f62a-4ca3-b833-25d53785a750.png)

### 2. load_text_print_gp.py
#### The code that load the text file (that is obtained by running get_video_text.py) and print gaze point on video

https://user-images.githubusercontent.com/69844293/182446405-b08ef437-518e-46ed-84e2-a10b28530b6f.mp4

### 3. live_scene_gaze_point.py
#### Code that displays the image in real time and outputs a normalized gaze point

[live_scene_gaze_point.webm](https://user-images.githubusercontent.com/69844293/182646109-4c17720c-c278-4a22-9740-8b9920fb20dd.webm)

### 4. save_frame_per_second.py
#### Save the frame every second while displaying the gp on the screen in real time.

[save_frame_per_second.webm](https://user-images.githubusercontent.com/69844293/183244315-0daf7af2-a094-4b15-98d3-ea8966049e22.webm)

# Using ROS, Data Publish & Subscribe

### 5. ROS_publish.py
#### Publish EyeTracker's data

https://user-images.githubusercontent.com/69844293/188066687-61a34fb4-6489-4618-8247-92f92b1de024.mp4

### 6. ROS_subscribe.py
#### Subscribe EyeTracker's data
![173D3D9D-23CB-4318-9731-CBDA90D52455](https://user-images.githubusercontent.com/69844293/188066699-812528a8-bb58-4fd3-b3e7-31ee23db6dcf.jpeg)

# Converting between ROS images and OpenCV images (Python, cvbridge)

### 7. cvbridge1_CV_to_ROS.py

https://user-images.githubusercontent.com/69844293/188067770-a2fe208f-7c38-41a1-899e-3513ee1a2a08.mp4


### 8. cvbridge2_CV_to_ROS.py
#### image processing(resize, threshold, grayscale..)
![cvbridge](https://user-images.githubusercontent.com/69844293/188067922-b8ae626b-9193-4b23-a8e1-b23ff48d025c.png)

### 9. tobii_talker.py 
### 10. tobii_listener.py

#### Frame and Tobii data are transmitted using the ROS environment EyeTracker-Tobii Glasses2.

![tobii_final](https://user-images.githubusercontent.com/69844293/188068612-01672dbc-3696-40aa-9f3b-fd9145f4559c.png)


[tobii_final.webm](https://user-images.githubusercontent.com/69844293/188068618-0aaa264b-95b3-411e-865e-de51f8f71c94.webm)


## Reference
```
@inproceedings{DeTommaso:2019:TOS:3314111.3319828,
 author = {De Tommaso, Davide and Wykowska, Agnieszka},
 title = {TobiiGlassesPySuite: An Open-source Suite for Using the Tobii Pro Glasses 2 in Eye-tracking Studies},
 booktitle = {Proceedings of the 11th ACM Symposium on Eye Tracking Research \& Applications},
 series = {ETRA '19},
 year = {2019},
 isbn = {978-1-4503-6709-7},
 location = {Denver, Colorado},
 pages = {46:1--46:5},
 articleno = {46},
 numpages = {5},
 url = {http://doi.acm.org/10.1145/3314111.3319828},
 doi = {10.1145/3314111.3319828},
 acmid = {3319828},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {Tobii Pro Glasses 2, eye-tracking, human-computer interaction, open-source, wearable computing, wearable eye-tracker},
}
```
