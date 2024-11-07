import streamlit as st
st.title('수면의 질 예측 에이전트')

import joblib
model = joblib.load('logistic_regression_model.pkl') 

col1, col2,col3 = st.columns( 3 )      
with col1:
      st.subheader('수면 시간에 따른 수면의 질을 예측해주는 에이전트')
      st.write(' - 기계학습 알고리즘 :  ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/arsalanjamal002/student-sleep-patterns/data')
      st.write(' - 훈련    데이터 : 150건')
      st.write(' - 테스트 데이터 : 350건')
      st.write(' - 모델 정확도 : ')

with col2:
      st.subheader('데이터시각화1')
      st.image('____________' ) 
with col3:
      st.subheader('데이터시각화2')
      st.image('____________')

st.subheader('모델 활용')
st.write('**** 오늘의 수면 시간을 입력해주세요')

a = st.number_input(' 오늘의 수면 시간을 입력해주세요 ', value=0) 

if st.button('합불분류'):             
        input_data = [[ a ]]          
        p = model._______(input_data)      
        if p[0] == 1 :
              st.success('인공지능 분류 결과는 ___입니다')
        else:
              st.success('인공지능 분류 결과를 ____입니다')

              
