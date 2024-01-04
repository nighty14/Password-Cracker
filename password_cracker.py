print ("This Tool was created by: h4xx04 d0xK")
print ("Be Aware to use this tool because the developer can trace you up")


print ("Good Luck!! :)")

import random
import string

def crack_password(password):
    attempts = 0
    while True:
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))
        attempts += 1
        if guess == password:
            return attempts






password = input("Enter the password to crack:")
print("Cracking password...")
attempts = crack_password(password)
print(f"The password was cracked in {attempts} attempts.")



print ("                              =======                                             ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                             =========                                            ")
print ("                    ======== ========= ======== ======= ======                    ")
print ("                    ======== ========= ======== ======= ======                    ")
print ("                    ======== ========= ======== ======= ======                    ")
print ("    =====           ======== ========= ======== ======= ======                    ")
print ("     ======         ======== ========= ======== ======= ======                    ")
print ("    ========        ======== ========= ======== ======= ======                    ")
print ("     ========       ======== ========= ======== ======= ======                    ")
print ("       ==========   ======== ========= ======== ======= ======                    ")
print ("        =========== ======== ======== ======== =======  ======                    ")
print ("          ================== ======== ======== =======  ======                    ")
print ("            ================ ======== ======== =======  ======                    ")
print ("                ============ ======== ======== =======  ======                    ")

