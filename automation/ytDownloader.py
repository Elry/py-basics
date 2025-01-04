from pytube import YouTube

video_url = input('Youtube Video URL: ')

youtube_object = YouTube(video_url)

video_stream = youtube_object.streams.get_highest_resolution()
audio_stream = youtube_object.streams.get_audio_only()

video_path = input('Where to save the video file: ')
audio_path = input('Where to save the audio file: ')

video_stream.download(output_path=video_path)
audio_stream.download(output_path=audio_path)

## Simple metadata handler
# video_title = youtube_object.title
# video_description = youtube_object.description

# print(f"Video Title: {video_title}")
# print(f"Video Description: {video_description}")