#!/usr/bin/env python

import time
import musicbrainzngs as mbz
from global_map import countries


def start_connection():
    # Set the user agent: (app name, app version, contact info/email)
    mbz.set_useragent("Your_App_Name", "1.0", "your_email@example.com")
    mbz.rate()


def get_artist_area(artist_names: str)-> str:
    start_connection()
    pass
    # try:
    # except:
    # if artist_area in countries:
        # return artist_area
    # else:
        # return "NA"


def get_artist_gender(artist_names: str)-> str:
    start_connection()
    pass
    # try:
    # except:
    # if artist_gender in [male, female, neither]
        # return artist_gender
    # else:
        # return "NA"
