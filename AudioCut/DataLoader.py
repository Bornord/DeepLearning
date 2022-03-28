import audioCuting
import audioParsing
import os, os.path
import errno

class DataLoader:
    def __init__(self,name) -> None:
        self.name = name

    def load(self):
        pass
    def convert(self,filepath:str,prefix:str,nb_images : int = 100):
        audio_folder = "akina-audio-files"
        mkdir_p(audio_folder)
        self.audio_files = audioCuting.cutAudioData((int) (audioCuting.getAudioLenght(filepath)/nb_images), filepath,audio_folder, prefix, self.name)
        img_folder = "akina-image-files"
        mkdir_p(img_folder)
        self.img_files = []
        for file in self.audio_files:
            nfile = audioParsing.getSpectromFromFile(file,img_folder)
            self.img_files.append(nfile)
        


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def main() -> None:
    loader = DataLoader("willem")
    loader.convert("testAudio.wav","train")

if __name__ == "__main__":
    main()