from keras.models import model_from_json
from mfccSingle import mfccSingle
from pymongo import MongoClient
from datetime import datetime

recordingArray = mfccSingle('data/burping/10A40438-09AA-4A21-83B4-8119F03F7A11-1430925142-1.0-f-26-dc.wav')

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
    "Resource": "ache",
    "Start_Date": datetime.now(),
    "End_Date": datetime.now(),
    "Duration": "null",
    "Percent_Complete": "100",
    "Dependencies": "null"
}

entry_id = collection.insert_one(entry)

print(entry_id)