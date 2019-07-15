# Emotion-detection

## Introduction
  
This project aims to classify the emotion on a person's face into one of **seven categories**, using deep convolutional neural networks. This repository is an implementation of [this](https://github.com/atulapra/Emotion-detection/blob/master/ResearchPaper.pdf) research paper. The model is trained on the **FER-2013** dataset which was published on International Conference on Machine Learning (ICML). This dataset consists of 35887 grayscale, 48x48 sized face images with **seven emotions** - angry, disgusted, fearful, happy, neutral, sad and surprised.

## Dependencies

* Python 3.6, [OpenCV 3 or 4](https://opencv.org/), [Tensorflow](https://www.tensorflow.org/), [TFlearn](http://tflearn.org/), [Keras.](https://keras.io/)
* To install the required packages, run `pip install -r requirements.txt`.

## Usage
  
* First, clone the repository with `https://github.com/AndreaFrancis/happy-team-emotion-recognition` and enter the cloned folder: `cd Emotion-detection`.
* Download the **trained model** files from [here](https://drive.google.com/file/d/1rdgSdMcXIvfoPmf702UCtH6RNcvkKFu7/view?usp=sharing), extract it and copy the files into the current working directory.
* Modify config.ini file according to your configurations

```
[database]

Server = CBBRNDASORIA

Name = HappyTeam

User = andrea.soria

Psswd = 1234  

[process]

Captures = 20
```

 * For the fist time, run the database script TFLearn/db/sentiments.data.sql
 * Type `python main.py`

