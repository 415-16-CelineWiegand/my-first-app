import streamlit as st

st.title("Indy Cafe Menu")

st.header("Cafe Menu")

coffee = st.number_input("Coffee - 50 Baht:", value=0)
cake = st.number_input("Cake - 60 Baht:", value=0)
sandwich = st.number_input("Sandwich - 70 Baht:", value=0)
tea = st.number_input("Tea - 40 Baht:", value=0)

price = st.number_input("กรอกราคาเครื่องเดิม (บาท):", value=0.0)

vat = price * 0.07
net_price = price - vat

st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()

st.header(" Bill")
st.write("Price:", price, "Baht")
st.write9("VAT 7%:", vat, "Baht")
st.write("Total Price:", total, "Baht")

st.divider()

st.write("Thank you for visiting Indy Cafe! ")
