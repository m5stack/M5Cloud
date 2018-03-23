from m5stack import lcd, buttonC
from machine import I2S
import os, wave


i2s = I2S(  mode = I2S.MODE_MASTER | I2S.MODE_TX | I2S.MODE_DAC_BUILT_IN,
            rate = 16000,
            bits = 16,
            channel_format = I2S.CHANNEL_ONLY_RIGHT,
            data_format = I2S.FORMAT_I2S_MSB)


def wav_player(fname):
    wav = wave.open(fname)
    i2s.set_dac_mode(I2S.DAC_RIGHT_EN)
    i2s.sample_rate(wav.getframerate())
    i2s.bits(wav.getsampwidth() * 8)
    i2s.nchannels(wav.getnchannels()) 
    i2s.volume(100)

    while True:
        data = wav.readframes(1024)
        if len(data) > 0:
            i2s.write(data)
            print('.', end='')
        else:
            wav.close()
            break
        if buttonC.isPressed():
            wav.close()
            break;
    

lcd.print("I2S DAC play wav testing...")
os.mountsd()

# Playing WAV audio file
wav_player('/sd/sample_1.wav')
i2s.stop()
