from model import EMR
from singleface import runDetection
import sys 
import configparser

if __name__ == "__main__":
  print("\n------------Emotion Detection Program------------\n")
  network = EMR()
 
  config = configparser.ConfigParser()
  config.read('config.ini')
  captures = int(config['process']['Captures'])

  print(captures)
  runDetection(captures)