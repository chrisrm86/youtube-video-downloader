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
    2- Salir.\n""")

    choice = int(input("Ingrese una opción: "))
    if choice == 1:
        download_video()
    #elif choice == 2:
    #    download_audio()
    elif choice == 2:
        quit()
    else: 
        return menu()

run_program()

# VIDEO TEST: https://www.youtube.com/watch?v=aMsK3ZQg2KU&ab_channel=oscardaniel