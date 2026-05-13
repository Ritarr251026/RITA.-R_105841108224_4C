import hashlib

print("=== REGISTRASI USER ===")

# Input registrasi
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

# Mengubah password menjadi hash SHA-256
hash_password = hashlib.sha256(password.encode()).hexdigest()

# Menampilkan hash password
print("\n=== DATA TERSIMPAN ===")
print("Username :", username)
print("Hash Password :", hash_password)

print("\n=== LOGIN USER ===")

# Input login
login_password = input("Masukkan Password Login: ")

# Hash password login
hash_login = hashlib.sha256(login_password.encode()).hexdigest()

# Verifikasi login
if hash_login == hash_password:
    print("Status Login : Berhasil")
else:
    print("Status Login : Gagal")