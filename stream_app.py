from collections.abc import Mapping
import pickle
import streamlit as st
st.title("Bank Customer Churn Model")
# loading the trained model
pickle_in = open('model.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
def prediction(credit_score, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary, country):   
 
    # Pre-processing user input    
    if gender == "Male":
        gender = 0
    else:
        gender = 1
 
    if credit_card == "No":
        credit_card = 0
    else:
        credit_card = 1
 
    if active_member == "No":
        active_member = 0
    else:
        active_member = 1  

    if country == "Spain":
        country = 0


    if country == "Germany":
        country = 1
    
    
    if country == "France":
        country = 2
    

    # Making predictions 
    prediction = classifier.predict( 
        [[credit_score, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary, country]])
     
    if prediction == 1:
        pred = 'Stay!'
    else:
        pred = 'Leave!'
    return pred

def main():  
    # this is the main function in which we define our webpage  
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox("Customer's Gender",("Male","Female"))
    Age = st.number_input("Customer's Age")
    NumOfProducts = st.selectbox("Total Number of Bank Product The Customer Uses", ("1","2","3","4"))
    Tenure = st.selectbox("Number of Years The Customer Has Been a Client", ("0","1","2","3","4","5","6","7","8","9","10"))
    HasCrCard = st.selectbox('Does The Customer has a Credit Card?',("Yes","No"))
    IsActiveMember = st.selectbox('Is The Customer an Active Member?',("Yes","No"))
    EstimatedSalary = st.number_input("Estimated Salary of Customer") 
    Balance = st.number_input("Customer's Account Balance")
    CreditScore = st.number_input("Customer's Credit Score")
    country = st.selectbox('Is the Customer From France?',("Spain","Germany", "France"))
    
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(CreditScore, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, country) 
        st.success('The Customer will {}'.format(result))
        #print(LoanAmount)
     
if __name__=='__main__': 
    main()
