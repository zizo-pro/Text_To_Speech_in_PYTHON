from gtts import gTTS
from playsound import playsound

def english_lang(text):
	tts = gTTS(text,lang='en')
	tts.save(r"audio/en_audio.mp3")
	playsound(r"audio/en_audio.mp3")

def arabic_lang(text):
	tts = gTTS(text,lang='ar')
	tts.save("audio/ar_audio.mp3")

english_lang("i'm slim shady please")