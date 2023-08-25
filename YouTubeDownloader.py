from pytube import YouTube
from tqdm import tqdm
from time import sleep
def MP3():
    for i in tqdm(YouTube(url).streams.get_audio_only().download(path), unit= " mb", colour="#00ff00"):
        sleep(0.5)
def MP4():
    for i in tqdm(YouTube(url).streams.get_highest_resolution().download(path2), unit= " mb", colour="#00ff00"):
        sleep(0.5)
while True:
    try:
        path = "C:\music"
        path2 = "C:\ video"
        url = input("enter url: ")
        print("Select the format")
        m_or_v = input("mp3 or mp4: ")
        if m_or_v == "mp3":
            MP3()
            break
        elif m_or_v == "mp4":
            MP4()
            break
        else:
            print("Please enter mp3 or mp4 !!!")
            continue

    except:
        print("ERORR")
        break
