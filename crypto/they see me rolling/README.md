# Challenge

They see me rolling [Medium]

## Description

I've intersepted the codes that open the gate to the building (;; separated). However the traffic is encrypted, if we can break the encryption we could get more information about the codes that they send. 

## Solutions

The ecnryption done by xoring the FLAG with a random number. The xor is done bitwise that means that Fi ^ Xi. Xi is very limited in values 0-9 if we xor the number again we get the number of the flag, "Fi_p = Fi ^ Xi ^ Xi_guess" Fi_p gives us a possible value of letter i from the flag. We have 25 intercepted messages, The correct value has to come out everytime. The other possible values will not always come out. 

My solution gives two possibilities per letter. Words are _ separated and the first value should be ctf, this leaves the competitors with possible words they have to guess. 


```Python
from vernamcipher.cryptographic import Cryptographic


def encrypt(data, key):
    return Cryptographic.exclusive_operations(data, key)

f = open("intercepted.txt", "r")
values = f.read().split(';;')[:-1]
print(values)
real_values = ['TBWH\x7fUiPL]BA]Z^iDQ\x05nVWuKICl^[_m^WME', 'RBUMqZn_CVDAYYWjF_\x03mT\\zEKAfP_YoYQIO', 'UD_Ix_fSARGDX[Ql@X\x00lT^qFHAf^_[lRTLJ', 'VLQJzZmQMQCGX\\VhGX\x02hW_rKJAb\\_XkXS@J', 'ZMSJ~TiVG]@JZXPoD\\\x02jQ^vGMHb^YVk]SMO', '[LUC\x7f]mQAVJF\\\\SkFQ\x04gWVwCICf]]WfXWJJ', 'WL_CzYj^D]AJ\\\\TnC\\\x03nVY{EIEmXYWnY]JO', 'VCWBpZmVM\\GJ^ZPjC\\\x0biVZsE@FeZX\\i]QMJ', 'PEWH|_jSCS@D\\X_oEP\x04iV_uJLHfZ]]l]WKK', 'VMQLq\\kTGPFDXWSiD_\x05iP^uJ@EeY_^l]TND', 'TB_NxUgWGV@DZZThEP\x05mUVv@MAa\\W\\oSPKM', 'TC_Bx^gWEQDDQ\\^hA[\ngWZtJOGlXV]j^UHE', 'QLRM\x7fYfQDQDC[]RiD_\x04g]ZsDNBa^Z_g\\SMN', 'T@WIz\\l^APJG^VToL_\x00g]WqGNDaX^ZfZTKL', 'QDTJqZgUEUJBYW^lL[\x05hUYz@OClQYYk]VNJ', 'QDSJ\x7f^iUDPKD]_RjD^\x04nPZwBHBe^_WhYWAN', '[F^Jy]jQMPGJ[Z_oG\\\x01gRZtKJ@bY\\Xm\\PKE', '[MRK}\\nPE]KBYXRmFY\nnQ\\uJNIeYV[jY]HD', 'QFPIqXiSDTBBP_UjMZ\nmQ_p@OBa[[Wn]]HK', 'UETI|]oPDQJBQWTkAY\x01gQYtJOBlQ_^g]]KL', 'TD_N{UmT@SACP[QfGP\x01nQ]zCLEc^[^m[VON', '[BWHyUgW@]FE\\^TjEX\x07g]WvBN@dQ\\Zi_\\OM', 'RFUB}XnTAWK@]\\UnMX\x05oVVrCHDfX^]m[SNN', 'WMQBz]fQGPEB]__oL\\\x07h]\\tKJEeYVWn]SNO', 'RF^By_g^DUAFXZVgA\\\x03lUWsAIHf_Z]o]RMK']

number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
possibilities = {}
print((len(values)))
for i in range(len(real_values)):
    value = values[i]
    print(value == real_values[i])
    print(f"{value} =? {real_values[i]}")
    for i in range(1, len(value) + 1):
        v = value[:i]
        if i not in possibilities:
            possibilities[i] = {}
        for n in number:
            result = encrypt(v, str(n) * i)
            c = result[i - 1]
            if c not in possibilities[i]:
                possibilities[i][c] = 1
                #print(f"{i}:{n} --> {c}")
            elif c in possibilities[i]:
                possibilities[i][c] += 1

filtered = {}
for i in possibilities:
    filtered[i] = []
    highest = list(possibilities[i].keys())[0]
    for l in possibilities[i]:
        if possibilities[i][l] == len(values):
            filtered[i].append(l)
        if possibilities[i][highest] < possibilities[i][l]:
            highest = l

    if highest not in filtered[i]:
        filtered[i].append(highest)


print(filtered)

strings = []
flag = "ctf{"

words = []
word_counter = 0
letter_counter = 0
for i in range(1, len(filtered)):
    if len(words) == i -1:
        words.append({})
    skip = False
    for letter in filtered[i]:
        if not letter.isalpha() and not letter.isdigit():
            word_counter += 1
            letter_counter = 0
            skip = True
            break
    if not skip:
        print(f"word {word_counter} - letter {letter_counter}: {filtered[i]}")
        words[word_counter][letter_counter] = filtered[i]
        letter_counter += 1


print(words)
```

## flag 
ctf{they_see_me_rolling_over_the_encryption_key}
