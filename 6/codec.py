import librosa

def encode(a):
    # a = input audio
    sr = 44100
    a = librosa.resample(a.astype("float_"), sr, sr//2)
    return a.astype("int16")

def decode(a):
    sr = 44100
    a = librosa.resample(a.astype("float_"), sr//2, sr)
    return a.astype("int16")