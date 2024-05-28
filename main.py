import os
import re
import sys
from tqdm import tqdm
from pytube import Stream, YouTube, Playlist


def directoryName(actual_title):
    # Replace any character that is not a letter, number, space, or underscore with an underscore
    sanitized_title = re.sub(r'[^\w\s]', '_', actual_title)
    return sanitized_title


def playlistDownload(link):
    def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
        pbar.update(len(data_chunk))

    print(
        "\n--------------------------------------- Starting Playlist download ---------------------------------------")
    playlist = Playlist(link)
    print("Playlist Name : {}\nChannel Name  : {}\nTotal Videos  : {}\nTotal Views   : {}".format(playlist.title,
                                                                                                  playlist.owner,
                                                                                                  playlist.length,
                                                                                                  playlist.views))
    folderName = directoryName(playlist.title)
    os.mkdir(folderName)

    playlistVideos = playlist.video_urls

    try:
        pbar = None  # Initialize pbar to None outside the loop
        for link in playlistVideos:
            yt = YouTube(link, on_progress_callback=progress_callback)
            video = yt.streams.get_highest_resolution()
            pbar = tqdm(total=video.filesize, unit='B', unit_scale=True, colour='#008080')
            print(f"\nDownloading video to '{video.default_filename}'")
            video.download(folderName)
            pbar.close()
    except:
        print('Playlist link is not valid. Please try again !')
        sys.exit(0)

    print("--------------------------------------- Download complete ---------------------------------------")
    print(f"All videos are saved in {os.path.abspath(folderName)}")


def singleVideoDownload(url):
    def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
        pbar.update(len(data_chunk))

    print("\n--------------------------------------- Starting download ---------------------------------------")
    ytVideo = YouTube(url, on_progress_callback=progress_callback)

    folderName = directoryName(ytVideo.title)
    os.mkdir(folderName)

    video = ytVideo.streams.get_highest_resolution()

    try:
        print(f"Downloading video to '{video.default_filename}'")
        pbar = tqdm(total=video.filesize, unit='B', unit_scale=True, colour='#008080')
        path = video.download(folderName)
        pbar.close()
    except:
        print('Playlist link is not valid.')
        sys.exit(0)

    print("--------------------------------------- Download complete ---------------------------------------")
    print(f"All videos are saved in {os.path.abspath(folderName)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = input("Enter url of any YouTube video or playlist: ")

    if url.__contains__("playlist"):
        playlistDownload(url)
    else:
        singleVideoDownload(url)

