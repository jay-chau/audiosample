from pydub import AudioSegment
import os

def cut_sample(sample, clip, skip):
    if len(song) > clip + skip:
        return song[skip: skip + clip]
    else:
        return song[len(song) - clip:]

def fade_sample(sample, fade):
    return sample.fade_in(fade_time).fade_out(fade_time)

if __name__ == '__main__':
    ## Global
    clip_seconds = 20 ## Total length of sample (in seconds)
    skip_part = 40 ## Skip begining section of sample (in seconds)
    fade_time = 2 ## Amount of fade in and out (in seconds)
    
    folder_out = "./OutputSamples"
    folder_in = "./InputSamples"
    
    already_done = os.listdir(folder_out)

    for s in os.listdir(folder_in):
        try:
            if f"{s}" not in already_done:
                
                song = AudioSegment.from_mp3(f"{folder_in}\\{s}")
                
                clip = fade_sample(
                    cut_sample(song, clip_seconds * 1000, skip_part * 1000), 
                    fade_time * 1000)
                
                clip.export(f"{folder_out}\\{s}", format='mp3')
            
        except:
            print(f"failed at {s}")


