#!/usr/env/bin python

'Pre-assign Zoom breakout rooms based on a Canvas group set.'


import csv
import re
from urllib.parse import urlparse
from canvasapi import Canvas
from argparse import ArgumentParser

# Parse command line arguments
parser = ArgumentParser(description='Pre-assign Zoom breakout rooms based on a Canvas group set.')
parser.add_argument('-c', '--course', type=int,
                    help='Course ID')
parser.add_argument('-u', '--canvas-url', type=str,
                    help='Canvas URL, without https prefix (e.g. canvas.institution.edu')
parser.add_argument('-g', '--group-set', type=int,
                    help='Group set ID')
args = parser.parse_args()


# Locate API key
try:
    with open('API_TOKEN.txt', 'r') as f:
        apikey = f.readline()
except FileNotFoundError:
    print('API_TOKEN.txt not found. ', end='')
    apikey = input('Please enter your API key: ')


# Connect to Canvas
canvas_url = args.canvas_url
if canvas_url is None:
    canvas_url = input('Please enter Canvas url without https (e.g. canvas.college.edu): ')

try:
    canvas = Canvas('https://' + canvas_url, apikey)
except Exception as e:
    print('Error connecting to Canvas at {:s}'.format(canvas_url))
    raise e


# Select course
course_id = args.course
if course_id is None:

    # Display list of courses
    print('\n Your courses:')
    for c in canvas.get_courses():
        print('  ', c)

    # Prompt user to select course
    course_id = int(input('\nEnter the course ID: '))

course = canvas.get_course(course_id)


# Select group set
group_sets = {gs.id:gs for gs in course.get_group_categories()}

group_set_id = args.group_set
if group_set_id is None:

    # Display list of group sets
    print('\nYour group sets:')
    for gs_id in group_sets:
        print('  ', group_sets[gs_id].name, '({:d})'.format(gs_id))

    # Prompt user to select a group set
    group_set_id = int(input('\nEnter a group set ID: '))

group_set = group_sets[group_set_id]


# Write CSV file
out_fname = 'breakout_rooms_{:s}.csv'.format(re.sub('[^\w\-_\. ]', '_',
                                                    group_set.name))

with open(out_fname, 'w', newline='') as outfile:

    print('Writing CSV file...', end='')
    csvout = csv.writer(outfile, delimiter=',')
    
    csvout.writerow(['Pre-assign Room Name', 'Email Address'])
    for g in group_set.get_groups():
        for u in g.get_users(include=['email']):
            csvout.writerow([g.name, u.email])

    print(' Done')
