import os
import requests
import colorama
import threading

from colorama import Fore, init
from proxy_checker import ProxyChecker

proxies = []




def test():
    with open("proxies.txt", "r+") as extreme:
        os.system("title Proxy Checker by ExtremeDev")
        init()
        dev = extreme.readlines()
        for proxy in dev:
            checker = ProxyChecker()
            value = checker.check_proxy(proxy)
            if 'False' in str(value):
                print(Fore.RED + f"{proxy}" + Fore.WHITE)
                with open("bad.txt", "a+") as write:
                    write.write(f"{proxy}\n")
            else:
                print(Fore.GREEN + f"{proxy}" + Fore.WHITE)
                with open("good.txt", "a+") as write:
                    write.write(f"{proxy}\n")

test()