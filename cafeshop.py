import streamlit as st
st.title("🛒 แอปพลิเคชันคำนวณราคาน้ำรวม VAT 7%")

st.title("Menu")
print("=== ร้าน Panda Cafe ===")
print("1. ชาไทยเย็น (35 บาท)")
print("2. กาแฟเอสเพรสโซเย็น (45 บาท)")
print("3. ชาเขียวมัทฉะ (50 บาท)")
print("4. โกโก้เย็น (40 บาท)")
print("5. นมสดคาราเมล (45 บาท)")
print("6. ชามะนาว (35 บาท)")
print("7. นมเผือก (35 บาท)")
print("-----------------------------------")

price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

vat = price * 0.07
net_price = price - vat

st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()
