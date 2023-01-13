import streamlit as st
import src.model as model # import the model.py file to predict and access the model and graphs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# add images of the prediction graph and the loss function graphs (put them in static/images folder)
# connect to model in src/model.py and run the predict function when the user submits their values to predict on
# add fields in the streamlit app to ask the user to submit values

# Explanation of the app
st.title("Hurricane Prediction")
st.markdown(
    """
        Predicting the windspeed of a hurricane from its latitude, 
        longitude, maximum sustained wind, and its central pressure.

        In the following code, we train an LSTM model to predict future hurricanes, 
        and then test it on the test dataset. The learning rate was
        decided after some experimentation, where we chose the learning rate 
        that gave accurate results. The number of epochs we use is 20, by which 
        it would have converged and thus would suffice for the purposes of this 
        notebook. After that, we visualize three different graphs: the 
        comparison between the real hurricane data and the ones given by the 
        model; and the evolution of test loss and training loss by epoch.
    """
)

# Section 2 shows graphs of the loss function and the prediction graph
size = model.size
df_out = model.df_out

chart_data = pd.DataFrame(
    df_out,
    columns = ["Model forecast", "tmrw windspeed"]
)

st.line_chart(chart_data)

st.title("")

# Section 3 is where the user can make predictions

# **** FOR REFERENCE ****
# ? GH LINK: https://github.com/cloudera/CML_AMP_Intelligent_Writing_Assistance
# ? Streamlit Docs: https://docs.streamlit.io/en/stable/