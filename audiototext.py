from pathlib import Path # for folder
import whisper #audio to text


folder_path = Path("folder") #location of the folder

# all the extentions of the audio and video file
extensions = [
    "*.mp3", "*.aac", "*.aif", "*.aiff", "*.aifc", "*.alac", "*.amr", "*.ape",
    "*.au", "*.cda", "*.flac", "*.gsm", "*.m4a", "*.m4b", "*.mid", "*.midi",
    "*.mpa", "*.mpc", "*.ogg", "*.oga", "*.mogg", "*.opus", "*.ra", "*.rm",
    "*.tta", "*.wav", "*.wma", "*.wv", "*.3g2", "*.3gp", "*.avi", "*.flv",
    "*.h264", "*.m4v", "*.mkv", "*.mov", "*.mp4", "*.mpg", "*.mpeg", "*.swf",
    "*.vob", "*.webm", "*.wmv"
]

model = whisper.load_model("tiny") # smallest available model





for ext in extensions:
    for file in folder_path.rglob(ext):
        audio_path = str(file)
        result = model.transcribe(audio_path)
        res = (result["text"])
 
    with open('converted text.txt', 'w') as output_file:
 
        output_file.write(res)


