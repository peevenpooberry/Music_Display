#!/usr/bin/env python

import musicbrainzngs as mbz
from modules.global_map import country_dict


def start_connection():
    # Set the user agent: (app name, app version, contact info/email)
    mbz.set_useragent("Music_Display", "1.0", "sjengelbretson2005@gmail.com")
    # Set the rate of API requests (seconds, number of requests) maximum is 50 per second
    mbz.set_rate_limit(1.0, 3)


def get_artist_id(artist_name:str)-> str:
    search_results = mbz.search_artists(artist=artist_name)
    if search_results["artist-list"]:
        first_artist = search_results["artist-list"][0]
        artist_id = first_artist["id"]
        return artist_id
    else:
        return "NA"
    

def get_first_artist(artist_names: str)-> str:
    artist_names_list = artist_names.split(";")
    return artist_names_list[0]


def get_artist_area(artist_names: str)-> str:
    try:
        start_connection()
        if ";" in artist_names:
            artist_name = get_first_artist(artist_names)
        artist_id = get_artist_id(artist_name)
        result = mbz.get_artist_by_id(artist_id)
        artist_data = result["artist"]
        country = artist_data["country"]
        if country in country_dict.keys():
            country_abr = country_dict[str(country)]
            return country_abr
        else:
            return "NA"
    except:
        return "NA"
    

def get_artist_gender(artist_names: str)-> str:
    try:
        start_connection()
        if ";" in artist_names:
            artist_name = get_first_artist(artist_names)
        artist_id = get_artist_id(artist_name)
        result = mbz.get_artist_by_id(artist_id)
        artist_data = result["artist"]
        gender = artist_data.get("gender")
        return str(gender)
    except:
        return "NA"
