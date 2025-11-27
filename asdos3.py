password = "python123"

while True:
  password_input= (input("masukan password : "))
  if password_input == password:
    print("password benar!")
    break
  else:
    print("Password salah")
