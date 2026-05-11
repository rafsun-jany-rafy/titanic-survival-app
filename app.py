import streamlit as st
import pandas as pd
import numpy as np
import pickle

#loading the trained model
@st.cache_resource
def load_model():
    with open('titanic_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

#Titel and Description
st.title('🚢 Titanic Survival Prediction App')
st.write('Enter passenger details to predict survival')

with st.sidebar:
    st.header('About')
    st.write('This app predicts Titanic passenger survival using a Random Forest model.')
    st.metric('Model Accuracy', '85%')  
    
if st.checkbox('Show Feature Importance'):
    importance = pd.DataFrame({
        'Feature': ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'],
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    st.bar_chart(importance.set_index('Feature'))

#Create input fields
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox('Passenger Class', [1,2,3],
                          help='1 = 1st Class, 2 = 2nd Class, 3 = 3rd Class')
    sex = st.selectbox('Sex',['Male','Female'])
    age = st.slider('Age', 0, 80, 29)
    sibsp = st.number_input('Number of Siblings/Spouses', 0,10,0)
    
with col2:
    parch = st.number_input('Number of Parents/Children',0,10,0)
    fare = st.number_input('Fare', 0.0, 500.00, 8.05)
    embarked = st.selectbox('Port of Embarkation',
                            ['S = Southampton','C = Cherbourg','Q = Queenstown'])

#Convert categorical inputs to numerical
sex_encoded = 1 if sex == 'Female' else 0
embarked_encoded =  {'S = Southampton':0,'C = Cherbourg':1,'Q = Queenstown':2}[embarked]
    
#Prediction Button
if st.button('Predict Survival', type='primary'):
    input_data = np.asarray([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])
    
    #make a prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)
    
    #Display result
    st.divider()
    if prediction[0] == 1:
        st.success('✅ Passenger would have SURVIVED!')
        st.metric('Survival Probability', f'{probability[0][1]*100:.2f}%')
    
    else: 
        st.error('❌ Passenger would NOT have survived')
        st.metric('Survival Probability', f'{probability[0][1]*100:.2f}%')
        
    
    #Show input summary
    with st.expander('See Input Details'):
        st.write(f'**Class:** {pclass}')
        st.write(f'**Sex:** {sex}')
        st.write(f'**Age:** {age}')
        st.write(f'**Siblings/Spouses:** {sibsp}')
        st.write(f'**Parents/Children:** {parch}')
        st.write(f'**Fare:** ${fare:.2f}')
        st.write(f'**Embarked:** {embarked}')