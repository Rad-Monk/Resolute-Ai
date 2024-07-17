import streamlit as st # type: ignore
import pandas as pd # type: ignore
from mylib import get_summary

st.title('Resolute AI - Data Science Task')
st.header('Task 1: K-means Clustering')


# Task 1: Apply K-means clustering and display predicted clusters

train_data = pd.read_excel('data/task-1/train.xlsx')
st.subheader('Original Training Dataset')
st.write(train_data)

test_data = pd.read_csv('task-1/test_with_clusters.csv')
st.subheader('Dataset with Predicted Clusters')
st.write(test_data)


# Task 2: Train and test classification models

model_accuracy = pd.read_csv("task-2/accuracy_models.csv")
test_predictions= pd.read_csv("task-2/test_predictions.csv")

st.header('Task 2: Train and Test Classification Models')
st.subheader('Models Accuracy')
st.write(model_accuracy)
st.subheader('Model Predictions')
st.write(test_predictions)


# Task 3: Datewise analysis

processed_data = pd.read_csv('task-3/processed_data.csv')

st.header('Task 3: Datewise Analysis')
st.subheader('Analysis of the data')

st.write(processed_data)


# Task 6: Q/A with PDF

st.header('Task 5: PDF Summarizer')
st.write("first boot takes time as it install the model weights")
pdf = st.file_uploader("Upload your PDF File and Ask Questions", type="pdf")

if pdf is not None:
    summary = get_summary(pdf)
    st.write(summary)