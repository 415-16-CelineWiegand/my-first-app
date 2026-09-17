import streamlit as st

st.title("Indy Cafe Menu")

st.header("Cafe Menu")

coffee = st.number_input("Coffee - 50 Baht:", value=0)
cake = st.number_input("Cake - 60 Baht:", value=0)
sandwich = st.number_input("Sandwich - 70 Baht:", value=0)
tea = st.number_input("Tea - 40 Baht:", value=0)

price = coffee  50 + cake  60 + sandwich  70 + tea  40

vat = price * 0.07
total = price + vat

st.divider()

st.header(" Bill")
st.write("Price:", price, "Baht")
st.write9"VAT 7%:", vat, "Baht")
st.write("Total Price:", total, "Baht")

st.divider()

st.write("Thank you for visiting Indy Cafe! ")
