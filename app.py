import streamlit as st

import joblib
model = joblib.load('logistic_regression_model.pkl') 

st.title('수면의 질 예측 에이전트')
st.subheader(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/arsalanjamal002/student-sleep-patterns/data')
st.write(' - 훈련 데이터 : 150건')
st.write(' - 테스트 데이터 : 350건')
 st.write(' - 모델 정확도 : ')


col1, col2, col3, col4, col5, col6 = st.columns(6 )      
with col1:
      st.subheader('데이터시각화1')
      st.image('____________' ) 
with col2:
      st.subheader('데이터시각화2')
      st.image('____________')
with col3:
      st.subheader('데이터시각화3')
      st.image('____________')
with col4:
      st.subheader('데이터시각화4')
      st.image('____________')
with col5:
      st.subheader('데이터시각화5')
      st.image('____________')
with col6:
      st.subheader('데이터시각화5')
      st.image('____________')

st.subheader('모델 활용')
st.write('**** 오늘의 수면 시간을 입력해주세요')

a = st.number_input(' 오늘의 수면 시간을 입력해주세요 ', value=0) 
b = st.number_input(' 오늘의 수면 시간을 입력해주세요 ', value=0) 
c = st.number_input(' 오늘의 수면 시간을 입력해주세요 ', value=0) 
d = st.number_input(' 오늘의 수면 시간을 입력해주세요 ', value=0) 
e = st.number_input(' 오늘의 수면 시간을 입력해주세요 ', value=0) 
f = st.number_input(' 오늘의 수면 시간을 입력해주세요 ', value=0) 
if st.button('수면의질 예측'):             
        input_data = [[ a,b,c,d,e,f ]]          
        p = model.predict(input_data)      
        st.write('인공지능이 예측한 당신의 수면의 질은', p)

              
