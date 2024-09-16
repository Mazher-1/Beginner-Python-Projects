import speech_recognition

recognizer = speech_recognition.Recognizer()

sample_audio = speech_recognition.AudioFile('4.1 SampleAudioFile.wav')
with sample_audio as source :
    audio = recognizer.record(sample_audio)



print(recognizer.recognize_google(audio))
