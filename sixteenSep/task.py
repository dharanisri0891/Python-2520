#actual_otp = 1234
#module random --> genertes random numbers
import random
actual_otp = random.randint(1000,9999)
print(actual_otp)

attempts = 3

while attempts:
    user_otps = int(input("Enter OTP"))
    if len(str(user_otps)) != 4:
        print("OTP must be 4 Digits Only")
    if user_otps == actual_otp:
        print("Transaction Success")
        break
    attempts = attempts - 1
else:
    print("Maximum attempts is reached")