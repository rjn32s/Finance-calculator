import streamlit as st
from res.design import *
from utilities.function import *
import locale
import numpy as np
#from num2words import num2words
locale.setlocale(locale.LC_ALL, 'en_IN')
display_animation()
st.write("Calculators")
tab1, tab2, tab3 = st.tabs(["LumpSum", "SIP", "Time Duration"])

with tab1:
   st.header("LumpSum amount calculator.")
   st.image("./img/lum-sum-calculator.png",width=200)
   invested_amount = st.number_input("Invested Amount", min_value=0.0, step=1.0)
   rate_of_return = st.number_input("Rate of Return (in percentage)", min_value=0.0)
   tenure = int(st.number_input("Tenure (in years)", min_value=0.0, step=1.0))

# Calculate future value
   future_values = lumpsum_calculator(invested_amount, rate_of_return, tenure)
   future_val = locale.currency(future_values[-1], grouping=True)

# Display the result
   st.write("Future Value: ", future_val)
   # Plot the future values
   years = range(1, int(tenure+1))
   if future_values:
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(1, tenure+1), future_values, color='#FF6F61', linewidth=2, marker='o', markersize=6, markerfacecolor='white')
    plt.fill_between(np.arange(1, tenure+1), future_values, color='#FF9F51', alpha=0.3)
    plt.xlabel('Years', fontsize=12)
    plt.ylabel('Investment Value', fontsize=12)
    plt.title('Lumpsum Investment Growth', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(color='#EEEEEE')
    plt.tight_layout()


    # Convert the plot to a Streamlit figure and display it
    st.pyplot(plt)
    #    number_string = future_value.replace("₹", "").replace(",", "")

# # Convert the number string to float
#    number = float(number_string)

# # Convert the number to words
#    number_words = num2words(number, to="ordinal")

# # Display the converted number
#    st.write(number_words)

with tab2:
   st.header("SIP Calculator")

   # Calculating the future value
   target_wealth = st.number_input("Target wealth", min_value=0.0, step=1.0)
   rate_of_return = st.number_input("Rate of Return", min_value=0.0, step=1.0)
   rate_of_return = st.number_input("Tenure", min_value=0, step=1)/100
   adjust_inflation = st.checkbox('Adjust Inflation')
   st.write(adjust_inflation)
   future_val =calculate_sip(target_wealth, rate_of_return, tenure, adjust_inflation=False)
   st.write(future_val)



with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)