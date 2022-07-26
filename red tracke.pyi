from requests import get
import requests
class color:
	red = '\033[91m'
	green = '\033[92m'
	white = '\033[97m'
	blue = '\033[96m'
	yellow = '\033[93m'
	nock = '\033[94m'
print(f"""{color.green}
███████████     
██     ‌   
{color.white}██        ██▇─⫸   {color.blue}▊  {color.green}Name > | Red tracker{color.white}
██        ██▇─⫸   {color.blue}▊  {color.green}Extracting information from phone numbers
{color.red}██        
███████████      
{color.red}github > {color.white}https://github.com/Mr-Banana-2045
{color.yellow}
  [{color.red} 0 {color.yellow}] [ {color.green}Name of owner number {color.yellow} ]
  [{color.red} 1 {color.yellow}] [ {color.green}Target ip information {color.yellow}]
""")
num = float(input(f'{color.nock}enter number >{color.white}  '))
if num >= 0:
    if num == 0:
    	shshol = input(f"{color.nock}enter phone target > {color.white}")
    	moz = (get("https://numberbook.aryandev.ir/api.php" , json = {"number":shshol}).json()["data"])
    	print(f"{color.red}username > {color.yellow}[ {color.green}",moz,f"{color.yellow}]")
    else:
    	shshool = input(f"{color.nock}enter ip target > {color.white}")
    	x = requests.get(f'http://ip-api.com/json/{shshool}')
    	lolo = (x.text)
    	print(f"{color.red}file save | neme file > {color.green}phone.txt")
    	with open('phone.txt', 'w') as f:
    		f.write(lolo)
    		f.close()