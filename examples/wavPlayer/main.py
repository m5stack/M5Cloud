from m5stack import lcd, buttonC
from machine import I2S
import os, wave


def wav_player(fname):
    os.mountsd()
    wav = wave.open(fname)
    params = wav.getparams()
    nchannels = params[0]
    sampwidth = params[1]
    framerate = params[2]
    nframes   = params[3]
    
    i2s = I2S(mode=I2S.MODE_IN_DAC)
    i2s.sample_rate(framerate)
    i2s.bits_per_sample(sampwidth*8)
    i2s.channel(nchannels)
    i2s.volume(90)
    
    while True:
        data = wav.readframes(1024)
        if len(data) > 0:
            i2s.stream_out(data)
            print('.', end='')
        else:
            break
        if buttonC.isPressed():
            break;

    i2s.deinit()


lcd.print("I2S DAC play wav test.")
wav_player('/sd/sample_1.wav')
