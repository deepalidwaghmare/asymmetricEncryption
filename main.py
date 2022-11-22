p = 0
q = 0
cipher = "!#@ abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
secret_key = 0
public_key = 0
plain_text = ""
encrypted_text = ""
word = ""
key_number = 1
run = True

while run:
    p, q = input("Please enter numbers separated by column it should be prime no:\n#>").split(" ")
    p = int(p)
    q = int(q)
    n = p * q
    z = (p-1)*(q-1)

    for i in range(1, 1000):
        if 0 != z % i:
            public_key = round(i)
            break

    for j in range(0, 10000):
        d = 1 + (j * z)
        d2 = d/public_key
        if 0 == d % public_key:
            secret_key = round(d2)
            break

    start = True
    while start:
        print("p=", p)
        print("q=", q)
        print("modulo=", n)
        print("publick key", public_key)
        print("secret key", secret_key)
        print("Commands")
        print("-en")
        print("-de")
        print("exit")
        word = input("#>")

        if "-exit" in word:
            start = False

        if "-en" in word:
            plain_text = input("Enter your plain Text: ")
            encrypted_text =""
            for k in plain_text:
                m = 0
                for l in cipher:
                    if k == l:
                        if m < 10:
                            m = m + 00
                        encrypted_text = encrypted_text + (str((m ** public_key)% n))  + " "
                        break
                    m += 1
            print("encrypted Text: " , encrypted_text)
            input("press enter")

        if "-de" in word:
            encrypted_text = input("Enter En Text: ")
            plain_text = ""
            for s in encrypted_text.split(" "):
                for k in cipher:
                    m = 0
                    for l in cipher:
                        if k == l:
                            if s == (str((m ** public_key) % n)):
                                plain_text = plain_text + l
                            break
                        m += 1
            print("PT: " ,plain_text)
            input("Press Enter")

        if "-exit" in word:
            run = False
