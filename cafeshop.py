import streamlit as st
st.title("🛒 แอปพลิเคชันคำนวณราคาน้ำรวม VAT 7%")

st.title("Menu")
menu = {
    1: {"name": "ชาไทยเย็น", "price": 35},
    2: {"name": "กาแฟเอสเพรสโซเย็น", "price": 45},
    3: {"name": "ชาเขียวมัทฉะ", "price": 50},
    4: {"name": "โกโก้เย็น", "price": 40},
    5: {"name": "นมสดคาราเมล", "price": 45},
    6: {"name": "ชามะนาว", "price": 35},
    7: {"name": "นมเผือก", "price": 35}


price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

vat = price * 0.07
net_price = price - vat

st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()
