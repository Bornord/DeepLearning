from this import d
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io.wavfile import read, write
import sounddevice as sd
from PIL import Image


def getAudioData(audio_path:str):
    Fs ,data = read(audio_path)
    data = data[:,0]
    return Fs,data

def saveAudioData(audio_path:str,Fs:int,data:np.ndarray)->None:
    write(audio_path,Fs,data)

def recordAudio(seconds:int=5,Fs:int=44100,audio_path:str="./audioParsing/output.wav"):
    print("start recording")
    recording = sd.rec(int(seconds * Fs), samplerate=Fs, channels=2)
    sd.wait()  
    print("end of recording")
    write(audio_path, Fs, recording)
    

def plotAudio(data:np.ndarray,Fs:int)->None:
    plt.figure()
    time = len(data)*(1/Fs)
    plt.plot(data)
    plt.ylabel("Amplitude")
    plt.xlabel(f"Sample index ({time}s)")
    plt.show()

def getFrequency(data):
    freq = np.fft.fft(data)
    return freq

def plotFrequency(data):
    freq = np.fft.fft(data)
    plt.plot(freq)
    plt.ylabel("Amplitude")
    plt.show()

def getSpectogram(data:np.ndarray,Fs:int,spectogram_path:str="./audioParsing/tmp.png"):
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    fig.frameon = False
    ax.set_axis_off()
    ax.specgram(data,NFFT=128,Fs=Fs,noverlap=120,cmap="jet_r")
    #plt.colorbar()
    #plt.show()
    fig.savefig(spectogram_path,bbox_inches='tight')
    plt.close(fig)
    image = Image.open(spectogram_path)
    bbox = image.getbbox()
    image = image.crop(bbox)
    (width, height) = image.size
    cropped_image = Image.new("RGBA", (width, height), (0,0,0,0))
    cropped_image.paste(image, (0, 0))
    image.save(spectogram_path)

def getSpectromFromFile(filepath:str,output_folder:str):
    Fs,data = getAudioData(filepath)
    output_file = output_folder+"/" + clearExtension(getFileName(filepath))+".png"
    getSpectogram(data,Fs,output_file)
    return output_file

def getFileName(filepath):
    return filepath.split("/")[-1]
def clearExtension(filepath):
    return filepath.split(".")[0]

def recordAudioToSpectogram(seconds:int=5,Fs:int=44100,audio_path:str="audioParsing/audioTmp/tmp.wav"):
    recordAudio(seconds=seconds,Fs=Fs,audio_path=audio_path)
    Fs,data = getAudioData(audio_path=audio_path)
    getSpectogram(data, Fs)
