import random

thuong = "abcdefghijklmnopqrstuvwxyz"
HOA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
so = "0123456789"
special = "!@$%&*"
tat_ca = thuong + HOA + so + special

do_dai = int(input("Độ Dài:"))

if do_dai < 8:
    print("Cần ít nhất 8 ký tự")
else:
    print("Độ dài hợp lệ, bắt đầu tạo mật khẩu...")
mk = [random.choice(thuong), random.choice(HOA), random.choice(so), random.choice(special)]

for i in range(do_dai - 4):
    mk.append(random.choice(tat_ca))
random.shuffle(mk)
print("".join(mk))



