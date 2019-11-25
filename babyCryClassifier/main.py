from keras.models import model_from_json
from mfccSingle import mfccSingle
from pymongo import MongoClient
from datetime import datetime

import sounddevice as sd
from scipy.io.wavfile import write
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from playsound import playsound

fs = 44100  # Sample rate
seconds = 7  # Duration of recording

print("Recording now")

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print("Recording ended")
write('output.wav', fs, myrecording)  # Save as WAV file

# input('pause')

recordingArray = mfccSingle('data/tired/03ADDCFB-354E-416D-BF32-260CF47F7060-1433658024-1.1-f-04-ti.wav')

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.predict_proba(recordingArray)
print(score[0]*100)
arr = score.tolist()
print(arr)

type = arr[0].index(max(arr[0]))

reason = ''

if type == 0:
    reason = 'Bellyache'
elif type == 1:
    reason = 'Discomfort'
elif type == 2:
    reason = 'Burping'
elif type == 3:
    reason = 'Tired'
elif type == 4:
    reason = 'Hungry'

print(reason)

client = MongoClient("mongodb+srv://someuser:abcd1234@productstutorial-78qhy.mongodb.net/hackwestern?retryWrites=true&w=majority")
db = client.hackwestern

collection = db.sample

entry = {
    "Task_ID": "4",
    "Task_Name": reason,
    "Resource": reason,
    "Start_Date": datetime.now(),
    "End_Date": datetime.now(),
    "Duration": "null",
    "Percent_Complete": "100",
    "Dependencies": "null"
}

entry_id = collection.insert_one(entry)

print(entry_id)

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Your baby is crying! Reason: ' + reason,
         from_='',
         to=''
     )

print(message.sid)

