import re

pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"

regex = re.compile(pattern)
digit_regex = re.compile(r"\d")
n = int(input())
for _ in range(n):
    barcode = input()
    
    if regex.match(barcode):
        digits = digit_regex.findall(barcode)
        if digits:
            product_group = "".join(digits)
        else:
            product_group = "00"
        
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
        