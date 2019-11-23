# import sounddevice as sd
# from scipy.io.wavfile import write
# from playsound import playsound
#
# fs = 44100  # Sample rate
# seconds = 5  # Duration of recording
#
# print("Recording now")
#
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# print("Recording ended")
# write('output.wav', fs, myrecording)  # Save as WAV file
#
# playsound('output.wav')

import speech_recognition as sr


def listen(self):
    """Listens to response from microphone and converts to text"""
    self.userCommand = ""
    with sr.Microphone(device_index=self.mic, chunk_size=1024, sample_rate=48000) as source:
        print("\tThreshold: " + str(self.r.energy_threshold))
        print("\tWaiting for words...")
        try:
            audio = self.r.listen(source, timeout=5)
            # self.playSound("end.mp3")
            try:
                self.userCommand = self.r.recognize_google(audio)
                self.userCommand = self.userCommand.lower()
                if not self.processcommand(self.userCommand, source):
                    return False
                else:
                    return True
            except sr.UnknownValueError:
                print("\t...")
            except sr.RequestError as e:
                print("\tCould not request results from Google Speech Recognition service; {0}".format(e))
            except Exception as e:
                print(str(e))
        except Exception:
            print("\tNo audio heard")
            pass

def SpeechToText():
        r = sr.Recognizer()  # Speech recognition
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            message = r.recognize_google(audio)
            print("Check: " + message)
        try:
            print("User: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return message


print(SpeechToText())