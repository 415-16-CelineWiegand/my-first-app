import streamlit as st

st.title("Indy Cafe Menu")

st.header("Cafe Menu")

price = st.number_input("กรอกราคาเครื่องดื่ม (บาท):", value=0.0)
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
