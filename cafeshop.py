# 1. นิยามเมนูสินค้าและราคา
menu = {
    1: {"name": "ชาไทยเย็น", "price": 35},
    2: {"name": "กาแฟเอสเพรสโซเย็น", "price": 45},
    3: {"name": "ชาเขียวมัทฉะ", "price": 50},
    4: {"name": "โกโก้เย็น", "price": 40},
    5: {"name": "นมสดคาราเมล", "price": 45},
    6: {"name": "ชามะนาว", "price": 35},
    7: {"name": "นมเผือก", "price": 35}
}

print("=== เมนูเครื่องดื่มประจำร้าน ===")
for key, item in menu.items():
    print(f"{key}. {item['name']} - {item['price']} บาท")

total_price = 0

# 2. รับข้อมูลการสั่งซื้อ
print("\n--- กรอกจำนวนที่ต้องการสั่ง (หากไม่รับให้ใส่ 0) ---")
for key, item in menu.items():
    qty = int(input(f"รับ {item['name']} จำนวนกี่แก้ว: "))
    total_price += qty * item['price']

print(f"\nราคารวมทั้งหมด: {total_price} บาท")

# 3. คำนวณส่วนลดตามเงื่อนไข (If-Else)
discount = 0

# เงื่อนไขที่ 1: ยอดซื้อครบ 300 บาท ลด 10%
if total_price >= 300:
    discount += total_price * 0.10
    print("-> คุณได้รับส่วนลดยอดซื้อครบ 300 บาท (ลด 10%)")

# เงื่อนไขที่ 2: ส่วนลดบัตรสมาชิก
is_member = input("มีบัตรสมาชิกหรือไม่? (y/n): ").lower()
if is_member == 'y':
    discount += 50
    print("-> คุณได้รับส่วนลดบัตรสมาชิก ลดเพิ่ม 50 บาท")

final_price = total_price - discount
print(f"ส่วนลดรวมทั้งหมด: {discount} บาท")
print(f"ยอดเงินที่ต้องจ่ายจริง: {final_price} บาท")

# 4. รับเงินและคำนวณเงินทอน
cash = float(input("\nรับเงินจากลูกค้า (บาท): "))

if cash >= final_price:
    change = cash - final_price
    print(f"เงินทอน: {change} บาท")
    print("=== ขอบคุณที่ใช้บริการ ===")
else:
    print("จำนวนเงินไม่พอชำระ!")
