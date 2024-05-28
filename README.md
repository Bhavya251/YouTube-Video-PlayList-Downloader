# YouTube Video/PlayList Downloader

This Python script allows users to download YouTube videos or entire playlists to their local machine.

## Features

  - Download individual YouTube videos in the highest available resolution.
  - Download all videos from a YouTube playlist.
  - Progress bar display during downloads.

## Requirements

  - Python 3.x
  - Libraries: `os`, `re`, `sys`, `tqdm`, `pytube`

## Installation

  1. Ensure Python 3.x is installed on your system.
  2. Install required Python libraries:
       ```bash
       pip install tqdm pytube

## Usage
  Run the script using Python and follow the on-screen prompts:
  ```bash
  python main.py
  ```
  Enter the URL of the YouTube video or playlist when prompted. If the URL contains "playlist", the script will automatically switch to playlist download mode.

## Example
  Enter url of any YouTube video or playlist: https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID

## Error Handling
  The script checks if the provided URL is a valid YouTube video or playlist.
  If an invalid link is provided, the script will terminate and prompt the user to try again.

## Directory Structure
  Downloads are saved in a directory named after the video or playlist title, sanitized to remove any non-alphanumeric characters.

## Notes
  The script uses the pytube library to interact with YouTube content. Ensure compliance with YouTube's terms of service when using this tool.

## License
  This project is open-sourced under the MIT license.
