import numpy as np
import cv2
import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import preprocessing
from PIL import Image
import tempfile

def app():  
  image = st.file_uploader("Upload Object Image", type=['png','jpeg', 'jpg'])
  #st.write(type(image))

  if image:
    img = Image.open(image)
    img = np.array(img)
    #st.write(type(img))
    
  # Create a button to get the prediction values on click
  if (st.button("Predict")):
    classNames=[]
    classFile = 'coco.names'
    with open(classFile,'rt') as f:
      classNames = f.read().rstrip('\n').split('\n')


    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'


    net = cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/ 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    classIds, confs, bbox = net.detect(img, confThreshold=0.4)

    for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
        cv2.rectangle(img,box,color=(0,255,0),thickness=2)
        c1 = 50.2, 12.4
        c2 = 88.8, 40.8
        # st.write(classId)
        # st.write(classNames)
        # st.write(classNames[classId-1].upper())
        # st.write((box[0]+10,box[1]+30))
        if(len(classNames)-1 < classId):
          st.error("Object not detected")
        else:
          cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
          cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
          cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
          cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


    st.image(img)