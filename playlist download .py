#https://www.youtube.com/watch?v=mvZHDpCHphk&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs

from pytube import Playlist, YouTube

def download_selected_videos(playlist_url, start_video_number):
    """Downloads videos from the specified start video to the last video in a YouTube playlist.

    Args:
        playlist_url: The URL of the YouTube playlist.
        start_video_number: The 1-based index of the first video to download (e.g., 1 for the first video).
    """

    try:
        pl = Playlist(playlist_url)

        # Ensure start_video_number is within valid range
        if start_video_number < 1 or start_video_number > len(pl.videos):
            print("Invalid start video number. Please enter a number between 1 and", len(pl.videos))
            return

        # Get the total number of videos in the playlist
        total_videos = len(pl.videos)

        # Download videos from start_video_number to the last video
        for video_number in range(start_video_number - 1, total_videos):  # Use zero-based indexing
            video = pl.videos[video_number]
            video_url = video.watch_url

            yt = YouTube(video_url)
            video = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
            video.download()
            print(f"Downloaded video: {video.title}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    start_video_number = int(input("Enter the starting video number (1-based): "))
    download_selected_videos(playlist_url, start_video_number)
