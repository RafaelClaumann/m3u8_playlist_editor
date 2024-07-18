![series_menu](https://github.com/user-attachments/assets/3049b80a-31c5-4fd7-9cae-ed00f7a6602e)# M3U8 Playlist Editor

A simple CLI to edit M3U8 playlists that allows you to manage and modify playlists.

## Features

- **Load Playlists**: Import M3U8 playlists for editing.
- **Modify Items**: Add, remove, or edit entries in the playlist.
- **Remove Low Quality Channels**: Option to filter out channels that contains H265, HD², SD² or SD in their names.
- **Remove Unwanted Groups**: Easily delete groups of channels that are not needed.
- **Change Group Title**: Modify the titles of groups to better organize your playlists.
- **List Channels Info**: Display detailed information about the channels in the playlist.
- **Save Changes**: Export the edited playlist to a new M3U8 file.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RafaelClaumann/m3u8_playlist_editor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd m3u8_playlist_editor
   ```

## Usage

1. Run the main script:
   ```bash
   cd app/
   python3 main.py
   ```

2. Select an option: You will see a menu with the following options:
   ```bash
   Choose an option to work with:
    1. Channels
    2. Movies/Vod
    3. Series
   -1. Exit
   Enter the number of the desired option:
   ```
  
## Demonstration

### channels menu
![channels_menu](https://github.com/user-attachments/assets/7866309b-2a1d-40ae-bbeb-6133ad8abd9b)

### movies menu
![movies_menu](https://github.com/user-attachments/assets/5c23e4be-10ac-4602-b859-788c7b783e43)

### series menu
![series_menu](https://github.com/user-attachments/assets/33b89978-150a-4dc0-ace5-9a37b872e0dc)



## Playlist Format
This is the file structure that this scripts can parse.
   ```txt
   #EXTINF:0 tvg-name="News 4K" tvg-id="news.com" tvg-logo="channel.png" tvg-group="NEWS" catchup="default" catchup-days="7",News 4K
   http://watch.com/news4k

   #EXTINF:0 tvg-name="News H265" tvg-id="news.com" tvg-logo="news.png" tvg-group="NEWS" catchup="default" catchup-days="7",News H265
   http://watch.com/newsh265

   #EXTINF:0 tvg-name="Sports FHD" tvg-id="" tvg-logo="sports.png" tvg-group="SPORTS",Sports FHD
   http://watch.com/sportsfhd

   #EXTINF:0 tvg-name="Sports HD" tvg-id="" tvg-logo="sports.png" tvg-group="SPORTS",Sports HD
   http://watch.com/sportshd
   
   #EXTINF:-1 tvg-name="Movie Title" tvg-logo="movie.png" tvg-group="Movies | Drama",Movie Title
   http://watch.com/movie/1231312.mp4

   #EXTINF:-1 tvg-name="Some Series S01E01" tvg-logo="series.png" tvg-group="Series | provider",Some Series S01E01
   http://watch.com/series/S01E01.mp4

   #EXTINF:-1 tvg-name="Some Series S01E02" tvg-logo="series.png" tvg-group="Series | provider",Some Series S01E02
   http://watch.com/series/S01E02.mp4
   ```
