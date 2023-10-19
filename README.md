# Song Playlist Backend

This is the backend for a song playlist application. It provides REST APIs for managing and accessing song data in a normalized format. The backend is built using Flask, a Python web framework.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Get All Songs](#get-all-songs)
  - [Get Song by Title](#get-song-by-title)
  - [Rate a Song](#rate-a-song)

## Getting Started

### Prerequisites

To run the backend, you need to have the following software installed:

- Python 3.x
- Flask
- Pandas (for data processing)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/song-playlist-backend.git
Navigate to the project directory:

bash
Copy code
cd song-playlist-backend
Install the required Python packages using pip:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python app.py
The backend should now be running on http://localhost:5000.

API Endpoints
Get All Songs
URL: /songs
Method: GET
Description: Get all songs in the normalized data set. Supports pagination.
Get Song by Title
URL: /songs/<title>
Method: GET
Description: Get song data by title. Performs a case-insensitive search.
Rate a Song
URL: /songs/<song_id>/rate
Method: POST
Description: Rate a song using star ratings. Requires a JSON body with the star_rating field (1 to 5 stars).