# Canvas Breakout Rooms

Pre-assign Zoom breakout rooms based on a Canvas group set.

Trying to do active in your Zoom class? Breakout rooms are an effective way to quickly break students into small groups for discussions, worksheet activities, or lab group meetings. Zoom allows you to pre-assign students into breakout rooms by uploading a CSV file. If you use [Canvas LMS](https://www.instructure.com/canvas/), you can organize students into groups for group assignments. This script generates a Zoom breakout room assignment CSV file based on a group set defined in your Canvas course.

In my summer course (Mechanics of Engineering Materials at Cornell University), I had defined group sets for collaborative labs. I used the same lab groups for in-class activities.

## Installation

Download `canvas_breakout_rooms.py`. Make sure you have the [CanvasAPI](https://canvasapi.readthedocs.io) package installed.

## Usage

### Create a Group Set in Canvas

First, [create a Group Set in your Canvas course](https://community.canvaslms.com/docs/DOC-26335-how-do-i-add-a-group-set-in-a-course). You can either assign students manually, or allow students to self-select into their own groups.

### Create an API Token in Canvas

1. Log into Canvas
2. Click on your profile picture and click on "Settings."
3. Under "Approved Integrations," click "New Access Token.
4. Enter a short description under "Purpose."
5. Copy the API Token that is generated and save it in a plain text file "API_TOKEN.txt" in the same directory as `canvas_breakout_rooms.py`. You can also save it elsewhere, and just enter it when prompted by the script. Most importantly: __keep this file secret!__. It allows anyone to access and change your course and students' data.

### Generate the breakout room pre-assignment file

Run the script

```
python canvas_breakout_rooms.py
```

You can optionally specify the Canvas URL, course ID, and group set ID as command line arguments.

The script will create a new file called `breakout_rooms_<group set name>.csv`.

### Create pre-assigned breakout rooms in Zoom

1. Create a new Zoom meeting or edit your existing meeting. If you are using the Canvas/Zoom integration, go instead to <your institution>.zoom.us.
2. Click on "Breakout Room pre-assign" and then select "Import from CSV." Upload the file you created in the previous step.

## Get Help

```
python canvas_breakout_rooms.py -h
```
