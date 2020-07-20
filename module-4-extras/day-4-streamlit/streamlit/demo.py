import streamlit as st
import numpy as np
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

st.title("Andy's super duper app is definitely cooler than Paige's")

password = st.text_input("What is the password?")

if True:
    degree = st.slider("What degree function?", 1, 10, 5)

    feelings = st.sidebar.radio('How do you feel today?',
                                ['Good', 'Bad', 'Ugly'])

    st.subheader(f"I'm feeling {feelings}")

    df = pd.read_csv('data/sample_data.csv')
    x_min, x_max = st.slider("what values of X?",
                             df.x.min(), df.x.max(), [df.x.min(), df.x.max()])

    @st.cache
    def calculate_regression(df, degree, x_min, x_max):

        new_df = df.loc[(df.x >= x_min) & (df.x <= x_max)]

        pf = PolynomialFeatures(degree=degree)

        X_pf = pf.fit_transform(new_df[['x']])

        lr = LinearRegression()
        lr.fit(X_pf, new_df['y'])

        new_df['pred'] = lr.predict(X_pf)
        return new_df

    df = calculate_regression(df, degree, x_min, x_max)
    st.line_chart(df.set_index('x'))