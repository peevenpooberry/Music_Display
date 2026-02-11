#!/usr/bin/env python

import musicbrainzngs as mbz
from modules.global_map import countries_list


def start_connection():
    # Set the user agent: (app name, app version, contact info/email)
    mbz.set_useragent("Music_Display", "1.0", "sjengelbretson2005@gmail.com")
    # Set the rate of API requests (seconds, number of requests) maximum is 50 per second
    mbz.set_rate_limit(1.0, 40)
    

def get_first_artist(artist_names: str)-> str:
    artist_names_list = artist_names.split(";")
    return artist_names_list[0]


def get_artist_area(artist_names: str)-> str:
    try:
        start_connection()
        if ";" in artist_names:
            artist_names = get_first_artist(artist_names)
        
        results = mbz.search_artists(artist=artist_names, limit=1)
        if not results["artist-list"]:
            return "NA"
        
        artist = results["artist-list"][0]
        country = artist.get("country")
        if not country:
            return "NA"
        country = country.lower()
        if country not in countries_list:
            return "NA"
        return country
        
    except mbz.WebServiceError as e:
        print("MusicBrainz error:" )
        return "NA"
    

def get_artist_gender(artist_names: str)-> str:
    try:
        start_connection()
        if ";" in artist_names:
            artist_names = get_first_artist(artist_names)
        
        results = mbz.search_artists(artist=artist_names, limit=1)
        if not results["artist-list"]:
            return "NA"
        
        artist = results["artist-list"][0]
        gender = artist.get("gender", "NA")
        return gender
        
    except mbz.WebServiceError as e:
        print("MusicBrainz error:" )
        return "NA"
