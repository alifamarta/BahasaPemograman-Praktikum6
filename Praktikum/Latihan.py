telepon = {
    'Ari' : '081267888',
    'Dina' : '087677776'
}

print(telepon['Ari'])

telepon['Riko'] = '087654544'
telepon['Dina'] = '088999776'

print(telepon.keys)
print(telepon.values)

print("Nama\t| Nomor Telepon ")
print("======================")

for nama,nomor in telepon.items():
    print("%s \t| %s " % (nama,nomor))

print("\n")

del telepon['Dina']

print("Nama\t| Nomor Telepon")
print("======================")
for key,val in telepon.items():
    print("%s \t| %s " % (key,val))