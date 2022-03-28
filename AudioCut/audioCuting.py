
##from scipy.io.wavfile import read, write
import math
#import numpy as np
import soundfile as sf
import wave
from pydub import AudioSegment

file_path = "testAudio.wav"

#cutAudio avec durée de chaque morceau en paramètre
#en fait ça marche pas comme ça les datas
#environ : 30s -> data[268237]
def cutAudioData(lengthPieces : int, audio_path : str,folder:str, prefix : str, nom : str):
    # Read and rewrite the file with soundfile
    data, samplerate = sf.read(audio_path)
    ret = []
    curser = 0
    nbPieces = len(data) // lengthPieces

    name = folder + "/"+prefix + "_" + nom + "_"
    print(audio_path)
    suffix ="." + audio_path.split(".")[1]  #.wav
    for i in range(nbPieces):  
        filename = name + str(i+1) + suffix
        ret.append(filename)
        sf.write(filename , data[curser:curser+lengthPieces], samplerate)
        curser += lengthPieces
    print("files created")
    return ret

#test

def getAudioLenght(filepath):
    data, samplerate = sf.read(filepath)
    return len(data)

def main() -> None:
    cutAudioData(10000, file_path, "test", "bonsoir", "tests")

if __name__ == "__main__":
    main()