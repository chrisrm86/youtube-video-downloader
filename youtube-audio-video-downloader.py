import os
import sys
import pytube

class Downloader():

    def __init__(self, *args, **kwargs):
        self.run_app =  run_program(self)

    def download_video(self):
        url = str(input("URL VIDEO: "))
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        print("Check if your download is ready")
        run_program()
        

    def download_audio(self):
        url = str(input("URL VIDEO: "))
        youtube = pytube.YouTube(url)
        audio = youtube.streams.get_audio_only()
        audio.download()
        print("Check if your download is ready")
        run_program()
    
    def quit(self):
        print("Press ENTER to exit")
        input()
        sys.exit(0)
    
    def run_program(self):
        print("""---------- MENÚ ---------- \n\n
        1- Descargar video
        2- Descargar audio.
        3- Salir.\n""")

        choice = int(input("Ingrese una opción: "))
        if choice == 1:
            self.download_video()
        elif choice == 2:
            self.download_audio()
        elif choice == 3:
            self.quit()
        else: 
            return run_program()


Downloader.run_app(self)            

# VIDEO TEST: https://www.youtube.com/watch?v=aMsK3ZQg2KU&ab_channel=oscardaniel