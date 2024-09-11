from gtts import gTTS
import os

def text_to_speech(text, output_audio_path="static/audio/"):     
    myobj = gTTS(text=text, lang='bn', slow=False)
    myobj.save(output_audio_path+"output.wav")
    os.system("mpg123 "+output_audio_path+"output.wav")

