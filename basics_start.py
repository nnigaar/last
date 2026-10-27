
print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)

print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# TODO: cell, rsrp, drops

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# TODO: type(...) və «mətn ≠ ədəd»

print("=== Kərpic 4 ===")   # Müqayisə → True / False
# TODO: rsrp < -105, ==

print("=== Kərpic 5 ===")   # Siyahı (list)
# TODO: rsrp_list, indeks, len, orta

print("=== Kərpic 6 ===")   # Lüğət (dict)
# TODO: row = {...}, row["region"]

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)


# age = int(input("Please enter your age: "))
# if age < 21:
#     print("Your age is more than 21")
# elif age == 21:
#     print("You are is exactly 21")

# else:
#     print("Your age is not more than 21")




rsrp_list = [-91.5,-108.1,-86.2,-103.3,110.4]

weak = 0
for v in rsrp_list:
    if v < -105:
        print(v, "zeif")
        weak = weak+1
    else:
        print(v, "normal")
print("Zeif siqnal sayi:", weak)

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
