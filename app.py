from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')


# Load the normalized data from the CSV file
df = pd.read_csv('normalized_songs.csv')


@app.route('/songs', methods=['GET', 'OPTIONS'])
def get_all_songs():
    # Get query parameters for pagination
    page = request.args.get('page', type=int, default=1)
    page_size = request.args.get('page_size', type=int, default=10)

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    # Slice the DataFrame based on the pagination parameters
    songs = df[start_idx:end_idx].to_dict(orient='records')

    # Calculate the total number of pages
    total_pages = (len(df) + page_size - 1) // page_size

    # Return a JSON response with pagination information
    response = {
        "songs": songs,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages
    }
    return jsonify(response)


@app.route('/songs/<title>', methods=['GET'])
def get_song_by_title(title):
    # Perform a case-insensitive loose search for songs
    matching_songs = df[df['title'].str.contains(title, case=False, na=False)]

    if matching_songs.empty:
        return jsonify({"error": "Song not found"}), 404

    # Convert the matching songs to a list of dictionaries
    songs_list = matching_songs.to_dict(orient='records')

    return jsonify(songs_list)


@app.route('/songs/<id>/rate', methods=['POST'])
def rate_song(id):
    rating = request.json.get('star_rating')

    if rating is None or not isinstance(rating, int) or rating < 1 or rating > 5:
        return jsonify({"error": "Invalid rating. Must be an integer between 1 and 5."}), 400

    # Find the song by title
    song = df[df['id'] == id]

    if song.empty:
        return jsonify({"error": "Song not found"}), 404

    # Update the 'star_rating' column with the new rating
    df.loc[song.index, 'star_rating'] = rating

    return jsonify({"message": f"Rating for '{id}' updated to {rating} stars."})


if __name__ == '__main__':
    app.run(debug=True)
