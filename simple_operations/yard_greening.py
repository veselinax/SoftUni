sq_m_to_be_greened = float(input())
price = sq_m_to_be_greened * 7.61
discount = price * 0.18
final_price = price - discount
print(f"The final price is: {final_price:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")