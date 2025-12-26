import sys
from engine import BypassEngine
from resolvers import *

engine = BypassEngine()
engine.register(ParamsResolver())
engine.register(CommonShortenerResolver())
engine.register(LinkvertiseResolver())
engine.register(RekoniseResolver())
engine.register(SubUnlockResolver())
engine.register(AdFocUsResolver())
engine.register(RedirectResolver())

def run():
    if len(sys.argv) > 1:
        for url in sys.argv[1:]:
            print(f"[+] {url}")
            print(" ->", engine.resolve(url))
    else:
        while True:
            url = input("Short link > ")
            print("Final:", engine.resolve(url))

run()
