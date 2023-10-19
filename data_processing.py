import json
import csv

# Read the JSON dataset
with open('songs_dataset.json', 'r') as json_file:
    data = json.load(json_file)

# Create a CSV file for normalized data
with open('normalized_songs.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write header
    writer.writerow(["id", "title", "dance_ability", "energy", "acousticness",
                    "tempo", "duration_ms", "num_sections", "num_segments", "star_rating"])

    # Loop through the data and write rows
    for key in data["id"]:
        id = data["id"][key]
        title = data["title"][key]
        dance_ability = data["dance_ability"][key]
        energy = data["energy"][key]
        acousticness = data["acousticness"][key]
        tempo = data["tempo"][key]
        duration_ms = data["duration_ms"][key]
        num_sections = data["num_sections"][key]
        num_segments = data["num_segments"][key]
        star_rating = 0

        writer.writerow([id, title, dance_ability, energy, acousticness,
                        tempo, duration_ms, num_sections, num_segments, star_rating])
