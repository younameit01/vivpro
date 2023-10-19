# Song Playlist Backend

This is the backend for a song playlist application. It provides REST APIs for managing and accessing song data in a normalized format. The backend is built using Flask, a Python web framework.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Server](#running-server)
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
   git clone https://github.com/younameit01/vivpro.git
   cd vivpro
2. Create a Python virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate
3. Install the required python packages
    ```bash
    pip install -r requirements.txt

### Running Server
1. Run the Flask application:
    ```bash
    flask run
    ```
    By default, ther server will run at http://127.0.0.1:5000. You can access the API at this URL.

### API Endpoints
1. Get All Songs
    ```
    URL: /songs
    Method: GET
    Description: Get all songs in the normalized data set. Supports pagination.
    ```
2. Get Song by Title
    ```
    URL: /songs/<title>
    Method: GET
    Description: Get song data by title. Performs a case-insensitive search.
    ```
3. Rate a Song
    ```
    URL: /songs/<song_id>/rate
    Method: POST
    Description: Rate a song using star ratings. Requires a JSON body with the star_rating field (1 to 5 stars).
    ```
