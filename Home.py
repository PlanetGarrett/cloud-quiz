import streamlit as st
import pandas as pd

ss = st.session_state
if 'counter' not in ss:
    st.session_state['counter'] = 0

container = st.container()

qDf = pd.read_csv('assets/questions.csv')

def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

def increment_ss():
    st.session_state['counter'] += 1

def decrement_ss():
    ss.counter = ss.counter - 1

def check_ans(selected_ans, question_num, ans_key):
    if selected_ans == qDf.iat[question_num, 1]:
        container.subheader(':green[Correct!]')

    else:
        container.subheader(':red[Try again!]')
        ss.a = False
        ss.b = False
        ss.c = False
        ss.d = False

if ss.counter == 0:
    with container.container():
        st.header('🌧️ Welcome to the Cloud Quiz')
        st.subheader('See how well you know the ten most common types of clouds with a short 10 question quiz.')
        nl(1)
        if st.button('Start', on_click=increment_ss):
            container = st.empty()
        nl(4)
        st.write(' This applet is open-source for educational purposes. Email contact@planetgarrett.com for inquiries or to report bugs')
        
if ss.counter != 0 and ss.counter < 11:
    question_num = ss.counter
    q = question_num - 1
    photo_dir = qDf.iat[q,0]
    ans1 = qDf.iat[q,2]
    ans2 = qDf.iat[q,3]
    ans3 = qDf.iat[q,4]
    ans4 = qDf.iat[q,5]
    explanation = qDf.iat[q,6]
    with container.container():
        st.subheader(str(question_num) + '. What type of cloud is shown in the image?')
        st.image(photo_dir)
        st.checkbox(ans1, key='a', on_change=check_ans, args=[ans1, q, 'a'])
        st.checkbox(ans2, key='b', on_change=check_ans, args=[ans2, q, 'b'])
        st.checkbox(ans3, key='c', on_change=check_ans, args=[ans3, q, 'c'])
        st.checkbox(ans4, key='d', on_change=check_ans, args=[ans4, q, 'd'])

        col1, col2 = st.columns(2)
        col1.button('Previous', on_click=decrement_ss)
        col2.button('Next', on_click=increment_ss)

if ss.counter == 11:
    with container.container():
        st.subheader('Congratulations, you have completed the quiz.')
        st.write(' This applet is open-source for educational purposes. Email contact@planetgarrett.com for inquiries or to report bugs')