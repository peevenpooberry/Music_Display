#!/usr/bin/env python

# Imports
import seaborn as sns
import matplotlib.pyplot as plt
from pydantic import BaseModel
from modules.MusicBrainz_API_calls import get_artist_area, get_artist_gender
import csv

# Classes
class Track(BaseModel):
    Track_Name: str
    Album_Name: str
    Artist_Names: str
    Artist_Gender: str
    Artist_Area: str
    Release_Date: str
    Duration_ms: int
    Genres: str
    Tempo: float
    Playlist: str


# Functions
def create_track(row: csv.row)-> Track:
    artist_names = row["Artist.Name.s."]

    entry = Track(Track_Name=row["Track.Name"],
                  Album_Name=row["Album.Name"],
                  Artist_Names=artist_names,
                  Artist_Gender=get_artist_gender(artist_names),
                  Artist_Area=get_artist_area(artist_names),
                  Release_Date=row["Release.Date"],
                  Duration_ms=row["Duration..ms."],
                  Genres=row["Genres"],
                  Tempo=row["Tempo"],
                  Playlist=row["Playlist"])
    return entry
    

def get_tracks_from_csv(filename: str)-> list[Track]:
    tracks = []
    with open(filename, "r", encoding="utf-8") as input:
        all_data = csv.DictReader(input)
        for row in all_data:
            track = create_track(row)
            tracks.append(track)
            break
    return tracks


def into_playlists(tracks: list[Track])-> dict:
    playlist_dict = {}
    for track in tracks:
        playlist = track["Playlist"]
        if playlist not in playlist_dict.keys():
            playlist_dict[playlist] = [track]
        else:
            playlist_dict[playlist].append(track)
    return playlist_dict


# def write_to_csv(tracks: list[Track], output_name="output.csv"):
#     fieldnames = Track.model_fields.keys()
#     data = [track.model_dump() for track in tracks]
#     with open(output_name, "w", newline="") as output:
#         writer = csv.DictWriterwriter(output, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)


# Code
def main():
    filename = r"playlist_files/all_data.csv"
    tracks = get_tracks_from_csv(filename)
    print(tracks[0])
    #by_playlist = into_playlists(tracks)
    

if __name__ == "__main__":
    main()