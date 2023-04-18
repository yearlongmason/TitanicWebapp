import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

st.set_page_config(page_title='Titanic!')

col1, col2, col3 = st.columns(3)

fig, ax = plt.subplots(figsize=(7,5))
ax.bar(['1st', '2nd', '3rd'], [len(data[data['Pclass']==1]), len(data[data['Pclass']==2]), len(data[data['Pclass']==3])],       linewidth=1, edgecolor='Black')
ax.set_title('Passenger classes')
data

with col1:
    st.pyplot(fig)


fig, ax = plt.subplots(figsize=(7,5))
ax.hist(data['Age'], color='tab:purple', linewidth=1, edgecolor='Black')
ax.set_title('Passenger Age')

with col2:
    st.pyplot(fig)


fig, ax = plt.subplots(figsize=(7,5))
sns.violinplot(data=data, x='Pclass', y='Age', ax=ax)
ax.set_title('Passenger Age by class')

with col3:
    st.pyplot(fig)
