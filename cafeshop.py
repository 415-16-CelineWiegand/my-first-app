import streamlit as st

st.title("Indy Cafe Menu")

st.header("Cafe Menu")
st.header("ชาไทยเย็น 35 ")
st.header("กาแฟเอสเพรสโซเย็น 45 บาท")
st.header("โกโก้เย็น 40 บาท")
st.header("นมสดคาราเมล 45 บาท")
st.header("ชามะนาว 35 บาท")
st.header("นมเผือก 35 บาท")

st.divider()


price = st.number_input("กรอกราคาเครื่องดื่ม (บาท):", value=0.0)
vat = price * 0.07
net_price = price - vat

st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()

st.write("Thank you for visiting Indy Cafe! ")
