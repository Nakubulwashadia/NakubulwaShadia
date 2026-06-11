# Real world application using control structures
# Assignment 2: E-commerce platform with login system

# ============ USER DATABASE ============
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "cashier1": {"password": "cash123", "role": "Cashier"},
    "customer1": {"password": "cust123", "role": "Customer"},
}

# ============ LOGIN SYSTEM ============
print("==============================")
print("   Welcome to ShopEasy 🛒")
print("==============================")

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username]["password"] == password:
    role = users[username]["role"]
    print(f"\n✅ Login successful! Welcome {username}. You are logged in as {role}.\n")
else:
    print("\n❌ Invalid username or password. Access denied.")
    exit()

# ============ ACCESS LEVELS ============
if role == "Admin":
    print("🔑 ADMIN ACCESS — You can access all features.\n")

elif role == "Cashier":
    print("🧾 CASHIER ACCESS — You can process payments and view orders.\n")

elif role == "Customer":
    print("🛍️ CUSTOMER ACCESS — You can browse and purchase products.\n")

# ============ E-COMMERCE CALCULATOR ============
if role in ["Admin", "Cashier", "Customer"]:
    print("==============================")
    print("       Price Calculator")
    print("==============================")

    subtotal = float(input("Enter subtotal amount: $"))

    # ---- DISCOUNT BASED ON SUBTOTAL ----
    if subtotal >= 500:
        auto_discount = 20
        print("🎉 You qualify for a 20% discount (order over $500)!")
    elif subtotal >= 200:
        auto_discount = 10
        print("🎉 You qualify for a 10% discount (order over $200)!")
    elif subtotal >= 100:
        auto_discount = 5
        print("🎉 You qualify for a 5% discount (order over $100)!")
    else:
        auto_discount = 0

    # ---- COUPON CODE ----
    valid_coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "WELCOME": 15
    }

    coupon = input("Enter coupon code (or press Enter to skip): ").upper()

    if coupon == "":
        coupon_discount = 0
        print("No coupon applied.")
    elif coupon in valid_coupons:
        coupon_discount = valid_coupons[coupon]
        print(f"✅ Coupon '{coupon}' applied! {coupon_discount}% off.")
    else:
        coupon_discount = 0
        print("❌ Invalid coupon code.")

    # ---- TOTAL DISCOUNT ----
    total_discount_percent = auto_discount + coupon_discount
    discount_amount = subtotal * (total_discount_percent / 100)
    discounted_price = subtotal - discount_amount

    # ---- TAX BASED ON LOCATION ----
    print("\nSelect your location:")
    print("1) USA")
    print("2) Uganda")
    print("3) UK")
    print("4) Other")
    location = input("Enter choice (1-4): ")

    if location == "1":
        tax_rate = 8
        country = "USA"
    elif location == "2":
        tax_rate = 18
        country = "Uganda"
    elif location == "3":
        tax_rate = 20
        country = "UK"
    else:
        tax_rate = 5
        country = "Other"

    tax_amount = discounted_price * (tax_rate / 100)
    final_price = discounted_price + tax_amount

    # ---- RECEIPT ----
    print(f"""
==============================
         RECEIPT 🧾
==============================
Subtotal:            ${subtotal:.2f}
Auto Discount:       {auto_discount}%
Coupon Discount:     {coupon_discount}%
Discount Amount:    -${discount_amount:.2f}
Price After Discount: ${discounted_price:.2f}
Tax ({tax_rate}% - {country}):   ${tax_amount:.2f}
------------------------------
FINAL PRICE:         ${final_price:.2f}
==============================
""")

    # ---- ADMIN EXTRA FEATURE ----
    if role == "Admin":
        print("📊 ADMIN SUMMARY:")
        print(f"   Total discount given: ${discount_amount:.2f}")
        print(f"   Tax collected: ${tax_amount:.2f}")
        print(f"   Net revenue: ${final_price:.2f}")