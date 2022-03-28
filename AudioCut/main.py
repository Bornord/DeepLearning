import audioParsing
import os
from DataLoader import DataLoader



def main() -> None:
    print("main")
    """audio_path = "./audioParsing/audioTmp/tmp.wav"
    Fs,data = audioParsing.getAudioData(audio_path)
    audioParsing.plotAudio(data, Fs)
    spectogram_path = "./audioParsing/tmp2.png"
    audioParsing.getSpectogram(data, Fs,spectogram_path)
    #audioParsing.plotFrequency(data=data)"""
    
    #audioParsing.recordAudioToSpectogram()
    loader = DataLoader("akina")
    loader.convert("BELAMI_Enguerran.wav","train",100)
    
if __name__ == "__main__":
    main()