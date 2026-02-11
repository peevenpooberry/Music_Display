#!/usr/bin/env python

# Imports
import seaborn as sns
import matplotlib.pyplot as plt
from pydantic import BaseModel
from modules.MusicBrainz_API_calls import get_artist_area, get_artist_gender
from rich.progress import Progress
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

    with open(filename, "r", encoding="utf-8") as input:
        row_count = sum(1 for _ in input) - 1

    with open(filename, "r", encoding="utf-8") as input, open("summarized_data.csv", "w", newline="") as output:
        fieldnames = list(Track.model_fields)
        reader = csv.DictReader(input)
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        with Progress() as p:
            t = p.add_task("Adding tracks...", total=row_count)
            for row in reader:
                track = create_track(row)
                writer.writerow(track.model_dump())
                p.update(t, advance=1)


# def into_playlists(tracks: list[Track])-> dict:
#     playlist_dict = {}
#     for track in tracks:
#         playlist = track["Playlist"]
#         if playlist not in playlist_dict.keys():
#             playlist_dict[playlist] = [track]
#         else:
#             playlist_dict[playlist].append(track)
#     return playlist_dict


# Code
def main():
    filename = r"playlist_files/all_data.csv"
    get_tracks_from_csv(filename)
    #write_to_csv(tracks)
    #by_playlist = into_playlists(tracks)
    

if __name__ == "__main__":
    main()