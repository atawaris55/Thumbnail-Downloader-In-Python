import streamlit as st
import requests

# --- Function to extract video ID ---
def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

# --- UI ---
st.title("📺 YouTube Thumbnail Downloader")
st.write("Paste your YouTube video link below 👇")

url = st.text_input("Enter YouTube URL")

# --- Button ---
if st.button("Download Thumbnail"):
    video_id = extract_video_id(url)

    if not video_id:
        st.error("❌ Invalid YouTube URL")
    else:
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

        response = requests.get(thumbnail_url)

        if response.status_code != 200:
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            response = requests.get(thumbnail_url)

        if response.status_code == 200:
            st.success("✅ Thumbnail Ready!")

            # Show image
            st.image(thumbnail_url, caption="Thumbnail Preview")

            # Download button
            st.download_button(
                label="📥 Download Thumbnail",
                data=response.content,
                file_name=f"{video_id}.jpg",
                mime="image/jpeg"
            )
        else:
            st.error("❌ Thumbnail not found")