import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

df = pd.read_csv("bank.csv")

st.set_page_config(
    page_title="Real Time Science Dashboard",
    page_icon=":cameroon:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Real Time Analysis Dashboard")

# Filter sur jop
job_filter = st.selectbox("Select a job",pd.unique(df['job']))
# Espace dédié pour le sélecteur
df = df[df["job"]==job_filter]

# Creation des indicareurs
avg_age = np.mean(df['age'])
count_married = int(df[(df['marital'] == 'married')]['marital'].count())
balance = np.mean(df['balance'])

kpi1,kpi2,kpi3 = st.columns(3)

kpi1.metric(label="age :calendar:" , value= round(avg_age) , delta=round(avg_age))
kpi2.metric(label="Married count 💍" , value=int(count_married), delta=round(count_married))
kpi3.metric(label="Balance $" , value=f"$ {round(balance,2)}" , delta=round(balance/count_married))

# Graphiques

col1, col2, col3 = st.columns(3)
with col1:
    fig1 = plt.figure()
    sns.boxplot(x="age", y="marital", data=df,palette='muted')
    st.pyplot(fig1)
with col2:
    fig2 = plt.figure()
    sns.histplot(x="age",  data=df)
    st.pyplot(fig2)
st.markdown("### Detailed data view")
st.dataframe(df)
time.sleep()
