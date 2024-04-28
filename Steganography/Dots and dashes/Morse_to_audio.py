#!/usr/bin/python 
# based on : www.daniweb.com/code/snippet263775.html
import math
import wave
import struct

# Audio will contain a long list of samples (i.e. floating point numbers describing the
# waveform).  If you were working with a very long sound you'd want to stream this to
# disk instead of buffering it all in memory list this.  But most sounds will fit in 
# memory.
audio = []
sample_rate = 44100.0


def append_silence(duration_milliseconds=300):
    """
    Adding silence is easy - we add zeros to the end of our array
    """
    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)): 
        audio.append(0.0)

    return


def append_sinewave(
        freq=500.0,
        duration_milliseconds=100,
        volume=1.0):
    """
    The sine wave generated here is the standard beep.  If you want something
    more aggresive you could try a square or saw tooth waveform.   Though there
    are some rather complicated issues with making high quality square and
    sawtooth waves... which we won't address here :) 
    """ 

    global audio # using global variables isn't cool.

    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))

    return


def save_wav(file_name):
    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1

    sampwidth = 2

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The stanard for low quality
    # is 8000 or 8kHz.
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    # WAV files here are using short, 16 bit, signed integers for the 
    # sample size.  So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer.  NOTE: It is theortically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

    return

unit = 50
text = "..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--...- ..-..... ..--..-- ..--.... ..-..... ..--..-- ..--.... ..-..... ..--..-. ..--...."
for char in text:
    if char == '.':
        append_sinewave(duration_milliseconds=unit)
    elif char == '-':
        append_sinewave(duration_milliseconds=3*unit)
    elif char == ' ':
        append_silence(duration_milliseconds=unit*7)
    append_silence(duration_milliseconds=unit)
#save_wav("output.wav")


def generate_block_wave_string(file_path, threshold=0, block_duration=0.05):
    with wave.open(file_path, 'rb') as wav_file:
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()

        # Read audio data
        audio_data = wav_file.readframes(num_frames)

        # Convert audio data to a list of integers
        audio_samples = [int.from_bytes(audio_data[i:i + sample_width], byteorder='little', signed=True)
                         for i in range(0, len(audio_data), sample_width)]

        # Determine sound and silence intervals
        intervals = []
        in_sound = False
        buffer = 0
        start_time = 0

        for idx, sample in enumerate(audio_samples):
            amplitude = abs(sample)
            if amplitude > threshold:
                if not in_sound:
                    in_sound = True
                    start_time = int((idx / frame_rate) * 1000)
                    buffer = 0
            else:
                if in_sound and buffer > (frame_rate * 0.0005):
                    in_sound = False
                    end_time = int((idx / frame_rate) * 1000)
                    intervals.append((start_time, end_time))
                buffer += 1
        print(intervals)
        # Generate block wave string
        decode_string = ''

        prev_end = 0
        for start, end in intervals:
            time = end - start

            if start - prev_end >= 50*7:
                decode_string += ' '

            if time == 50:
                decode_string += '.'
            elif time == 150:
                decode_string += '-'
            else:
                pass
                #print(f"THE TIME DID NOT MAKE ANY SENSE HELP (time = {time})")



            prev_end = end
    return decode_string

# Example usage:
file_path = 'challenge.wav'  # Replace 'example.wav' with the path to your WAV file
block_wave_string = generate_block_wave_string(file_path)
print("decoded:", block_wave_string)
print(block_wave_string == text)
