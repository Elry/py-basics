from pygame import mixer
from gtts import gTTS

def main():
   text = input('Type text to play: ')
   tts = gTTS(text)
   sound_path = 'output.mp3'
   tts.save(sound_path)

   mixer.init()
   mixer.music.load(sound_path)
   mixer.music.play()
   mixer.quit()
   
if __name__ == "__main__":
   main()