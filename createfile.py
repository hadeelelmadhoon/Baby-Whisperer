import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound

fs = 44100  # Sample rate
seconds = 7  # Duration of recording

print("Recording now")

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print("Recording ended")
write('output.wav', fs, myrecording)  # Save as WAV file

playsound('output.wav')

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb+srv://someuser:abcd1234@productstutorial-78qhy.mongodb.net/hackwestern?retryWrites=true&w=majority")
db = client.hackwestern

collection = db.sample

entry = {
    "Task_ID": "4",
    "Task_Name": "Bellyache",
    "Resource": "ache",
    "Start_Date": datetime.now(),
    "End_Date": datetime.now(),
    "Duration": "null",
    "Percent_Complete": "100",
    "Dependencies": "null"
}

entry_id = collection.insert_one(entry)

print(entry_id)