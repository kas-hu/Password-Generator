import random

length = 10

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lowercase = uppercase.lower()

special_chars = '!"£$%^&*()_=+#[]{}~@:;><?/\|'

numbers = '0123456789'

mix = ''
while len(mix) <= length:
    mix += random.choice(uppercase) + random.choice(lowercase) + random.choice(special_chars) + random.choice(numbers)
password = mix

print(password)