
"""
import pytube

# set url in a variable
url ="https://www.youtube.com/watch?v=aMsK3ZQg2KU&ab_channel=oscardaniel"


# Load url in function youtube
youtube = pytube.YouTube(url)


# set stream resolution
video = youtube.streams.get_highest_resolution()


# Download video
video.download()        # in the same folder

# video.download('/Downloads')      in other folder

# get information of video
video.title
video.video_id
video.age_restricted

# streams format
video.streams.all()
stream = video.streams.all()
for i in stream:
    print(i)

"""
"""
import pytube

url = str(input('URL video: '))

youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download()


print("Download successfully")
input()
"""
import pytube
import os 
import sys

print("YOUTUBE VIDEO DOWNLOADER '\n'")


def download_video():
    url = str(input("URL VIDEO: "))
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()
    print("Check if your download is ready")
    

def download_audio():
    url = str(input("URL VIDEO: "))
    youtube = pytube.YouTube(url)
    audio = youtube.streams.get_audio_only()
    audio.download()
    print("Check if your download is ready")
    
    
def quit():
    print("Press ENTER to exit")
    input()
    sys.exit(0)
    

def run_program():
    print("""---------- MENÚ ---------- \n\n
    1- Descargar video
    2- Descargar audio.
    3- Salir.\n""")

    choice = int(input("Ingrese una opción: "))
    if choice == 1:
        download_video()
    elif choice == 2:
        download_audio()
    elif choice == 3:
        quit()
    else: 
        return menu()

run_program()

# VIDEO TEST: https://www.youtube.com/watch?v=aMsK3ZQg2KU&ab_channel=oscardaniel