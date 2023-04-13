import os
from pytube import YouTube

def download_song(link, save_path=None):
    #link je str arg, koji predstavlja  
    if save_path is None:
        save_path = os.path.join(os.path.expanduser("~"), "Downloads")

    #kreiramo instancu YouTuba, u koji ubacujemo link 
    yt = YouTube(link)

    # unutar varijable uzimamo samo zvuk iz videa
    audio_stream = yt.streams.filter(only_audio=True).first()

    # preuzimamo audio datoteku
    downloaded_file = audio_stream.download(save_path, filename=yt.title)

    # kreiramo novi file sa .mp3 ekstenzijom
    new_filename = os.path.splitext(downloaded_file)[0] + '.mp3'

    # funkcija koja preimenuje file 
    os.rename(downloaded_file, new_filename)

    # izbacujemo ispis da je pjesma preuzeta
    print(f"{yt.title} has been successfully downloaded as an mp3 file.")
    #funkcija vraća string sa imenom pjesme
    return os.path.abspath(new_filename)
