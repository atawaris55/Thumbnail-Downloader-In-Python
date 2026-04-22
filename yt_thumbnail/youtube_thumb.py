import requests
import os

def extract_video_id(url):
    if "v=" in url:
        video_id=url.split("v=")[1].split("&")[0]
        return video_id
    elif "youtu.be/" in url:
        video_id=url.split("youtu.be/")[1].split("?")[0]
        return video_id
    else:
        return None
def download_thumb(video_url):
    video_id=extract_video_id(video_url)
    if not video_id:
        print("Invalid YouTube URL")
        return
    thumbnail_url=f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    try:
        response=requests.get(thumbnail_url)
        if response.status_code==200:
            file_name=f"{video_id}_thumbnail.jpg"
            with open(file_name,"wb") as f:
                f.write(response.content)
            print(f"Thumbnail downloaded successfully as {file_name}")

        else:
            print("High quality thumbnail ot found, trying fallback....")
            #fallback
            thumbnail_url=f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            response=requests.get(thumbnail_url)
            if response.status_code==200:
                file_name=f"{video_id}_thumbnail.jpg"
                with open(file_name,"wb") as f:
                    f.write(response.content)
                print(f"Thumbnail downloaded (HQ): {file_name}")
            else:
                print("Failed to download thumbnail")
    except Exception as e:
        print(f"An error occured as {e}")

if __name__=="__main__":
    url=input("Enter the YouTube video URL: ")
    download_thumb(url)