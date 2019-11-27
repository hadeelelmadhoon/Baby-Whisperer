# Baby Whisperer

The Baby Whisperer is a revamped baby monitor that uses voice enabled technology to identify variable crying patterns for infants. TensorFlow was used to process convolutional neural networks of the Mel Frequency Cepstral Coefficient of the infant cries audio files, and categorize them with a predictive reason of crying. The baby's cries can be recorded from a device that will associate the crying to a reason with the help of the neural network. The caregiver will also receive an SMS message with the reason at the time of recording. Additionally, a web browser is used to display the analytics of this data including most common reason as well as how many times a day the child has cried.

# Folder Descriptions

## BabyCryClassifier

Python files that listen to audio files, convert audio into MFCC, classify the audio using a Convolutional Neural Network, and send a text message notification about the crying baby along with the classification. Data folder contains sample baby cry audio.

## Testing

Full stack website using Node.js, express, MongoDB, and Google Charts to display analytics of the results from the BabyCryClassifier files.

# How to run

1) Download the zip file
2) Run BabyCryClassifier/main.py to record and classifier crying audio (python main.py in terminal)
3) Run Testing/server.js (node server.js) and open browser at http://localhost:8080/chart/ 
