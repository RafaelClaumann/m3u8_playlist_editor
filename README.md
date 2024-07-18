# M3U8 Playlist Editor

A simple CLI to edit M3U8 playlists that allows you to manage and modify playlists.

## Demonstration

### channels menu
![channels_menu](https://github.com/user-attachments/assets/1cd18ec7-177f-49a9-aef1-3e1f749b4c7d)

### movies menu
![movies_menu](https://github.com/user-attachments/assets/8769a4e3-9173-4459-9a12-8d0f8b02e77f)

### series menu
![series_menu](https://github.com/user-attachments/assets/141179c2-32d0-47d1-a838-4d76e7256aed)


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
    Choose an option:
      1. Remove low quality channels
      2. Remove unwanted groups
      3. Change group title
      4. List channels info
      5. Exit
    Enter the number of the desired option: 
   ```
  
3. Removing low quality channels, option 1:
   ```bash
    Choose an option:
      1. Remove low quality channels
      2. Remove unwanted groups
      3. Change group title
      4. List channels info
      5. Exit
    Enter the number of the desired option: 1
    
    This will remove channels that contains H265, HD², SD² or SD in their names.
    Do you want to proceed? (y/n): y
   
    Total channels removed [ 180 ].
   ```
  
4. Removing unwanted groups, option 2:
   ```bash
    Choose an option:
      1. Remove low quality channels
      2. Remove unwanted groups
      3. Change group title
      4. List channels info
      5. Exit
    Enter the number of the desired option: 2
    
    Groups found in the channel list: 
    
    [0] - 4K CHANNELS
    [1] - SPORTS
    [2] - MOVIES
    [3] - DOCUMENTARY
    [4] - NEWS
    
    Choose one or more groups to be removed, use the number displayed at left of the group title.
    Type numbers separated by comma: 4, 2
    Do you want to proceed? (y/n): y
   
    Removing channels from group [ group-title="NEWS" ].
    Total channels removed [ 18 ].
    Channels from group [ group-title="NEWS" ] removed.
    Removing channels from group [ group-title="MOVIES" ].
    Total channels removed [ 5 ].
    Channels from group [ group-title="MOVIES" ] removed.
   ```

## Demonstration
![editando_canais](https://github.com/user-attachments/assets/3d20e054-4f46-4413-b6c9-24f4d944afe5)


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
