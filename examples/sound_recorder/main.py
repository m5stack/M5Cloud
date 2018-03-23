from m5stack import *
from machine import I2S
import os, wave, time


i2s = I2S(  mode = I2S.MODE_MASTER | I2S.MODE_TX | I2S.MODE_RX | I2S.MODE_DAC_BUILT_IN | I2S.MODE_ADC_BUILT_IN,
            rate = 16000,
            bits = 16,
            channel_format = I2S.CHANNEL_ONLY_RIGHT,
            data_format = I2S.FORMAT_I2S_MSB)


def record_sound(fname, duration=None):
    audio = wave.open(fname, 'wb')
    # audio.setnchannels(1)
    # audio.setsampwidth(2)
    # audio.setframerate(16000)
    audio.setparams([1, 2, 16000, 0, 'NONE', 'not compressed'])

    i2s.sample_rate(16000)
    i2s.nchannels(1)
    i2s.set_adc_pin(34) # Set the ADC Pin 34
    i2s.adc_enable(True)
    data = bytes(0)
    if duration:
        duration_time = (time.ticks_ms() + duration*1000) if duration else 0
        
    while True:
        data = i2s.read(8000)
        audio.writeframes(data)
        print('.', end='')

        if duration:
            if time.ticks_ms() > duration_time:
                break
        if buttonC.wasReleased():
            break;
    i2s.adc_enable(False)
    audio.close()
                 
    
def wav_player(fname):
    wav = wave.open(fname)
    i2s.set_dac_mode(I2S.DAC_RIGHT_EN)
    i2s.sample_rate(wav.getframerate())
    i2s.bits(wav.getsampwidth()*8)
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


lcd.print('Sound recorder testing..\n')
os.mountsd()
print('Record...')
file_name = '/sd/record/' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.wav'
record_sound(file_name, 5)

print('\nPlaying: '+file_name)
lcd.println('Playing: '+file_name)
wav_player(file_name)
i2s.stop()
