import random
characters = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pw_length = int(input("Masukkin panjang kata sandi yang antum mau :) :"))
generated_password = ""

for i in range(pw_length) :
    generated_password += random.choice(characters)

print("Kata sandi yang tergenerated :")