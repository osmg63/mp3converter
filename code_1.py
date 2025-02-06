import streamlit as st
import yt_dlp
import os

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_audio(youtube_url):
    """YouTube videosunun sesini indirir (WEBM formatında)."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",  # WEBM olarak kaydet
        'geo_bypass': True  # 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        filename = ydl.prepare_filename(info)  # Örn: downloads/video_title.webm

    return filename

# Streamlit UI
st.title("🎵 YouTube WEBM İndirici")
st.markdown("📌 **YouTube linkini gir ve WEBM olarak indir!**")

youtube_url = st.text_input("YouTube Video Linki:", "")

if st.button("İndir 🎶"):
    if youtube_url.strip():
        with st.spinner("İndirme işlemi devam ediyor..."):
            try:
                webm_file = download_audio(youtube_url)
                st.success(f"İndirme tamamlandı!")
                st.audio(webm_file, format="audio/webm", start_time=0)
                with open(webm_file, "rb") as file:
                    st.download_button("WEBM Dosyasını İndir", file, file_name=os.path.basename(webm_file), mime="audio/webm")
            except Exception as e:
                st.error(f"Hata oluştu: {e}")
    else:
        st.warning("Lütfen bir YouTube linki girin!")
