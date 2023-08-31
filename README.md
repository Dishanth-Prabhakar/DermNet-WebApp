# DermNet

## DermNet - Skin disease prediction


## Inspiration
"Turning a Negative Experience into Positive Change"

In the face of challenges, innovation can emerge that transforms negative experiences into powerful catalysts for positive change. The unfortunate incident of a person being falsely predicted and administered cancer drugs for years serves as a stark reminder of the critical responsibility that rests upon those venturing into the field of medical technology. While such an incident highlights the potential risks of inaccurate predictions, it also underscores the urgency to develop ethical and accurate solutions in skin disease prediction.
Hence building a skin disease prediction application can be a valuable contribution to the field of healthcare and dermatology. Such an application could help individuals identify potential skin issues early on and encourage them to seek professional medical advice. 


## What It Does
DermNet - A skin disease prediction application that takes dermoscopic and normal images as input and predicts the output for 32 different classes, which involves the use of advanced deep learning techniques and medical knowledge. Here's an overview of how this application works and the additional information it could provides.

**Functionality of the Application:**

• Input of dermoscopic image or normal image.

• Prediction: The application uses a trained convolutional neural network (CNN) model to predict

• Output: Provides the user with a prediction of the skin disease or condition.

• Gives the disease overview

• Provides available medical treatments

• Provides home remedies.


## How we built it
• Imported essential libraries

• Understand the data

• Train Test split

• Train the model using CNN to get better results and faster computation (Intel oneAPI Deep Neural Network (oneDNN))

• Model Fitting

• Attempt to gain maximum accuracy

• Save the model


## What we learned
**Intel oneDNN:** Intel oneDNN (Deep Neural Network Library), is used to efficiently preprocess the input images. This might involve tasks like resizing, normalization, and data augmentation to ensure consistent and meaningful input for the neural network.
We designed and trained a deep learning model using a framework like TensorFlow and Keras. These frameworks can leverage oneDNN's optimized operations for better performance during the training process. oneDNN provides a backend for many popular deep learning frameworks, allowing them to take advantage of hardware acceleration.

**Image Analysis:** Image is analyzed using Convolutional Neural Networks (CNNs) architecture which is the critical component in our skin disease prediction application. CNNs excel in extracting intricate patterns and features from images, making them well-suited for identifying subtle visual cues in skin lesions. 
