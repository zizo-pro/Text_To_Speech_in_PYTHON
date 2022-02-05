from gtts import gTTS

def english_lang(text):
	tts = gTTS(text,lang='en')
	tts.save("en_audio.mp3")

def arabic_lang(text):
	tts = gTTS(text,lang='ar')
	tts.save("ar_audio.mp3")

arabic_lang("تجربة")