from fastapi import FastAPI
from engine import BypassEngine
from resolvers import *

app = FastAPI(title="Bypass API")

engine = BypassEngine()
engine.register(ParamsResolver())
engine.register(CommonShortenerResolver())
engine.register(LinkvertiseResolver())
engine.register(RekoniseResolver())
engine.register(SubUnlockResolver())
engine.register(AdFocUsResolver())
engine.register(RedirectResolver())

@app.get("/bypass")
def bypass(url: str):
    return {
        "input": url,
        "output": engine.resolve(url)
    }
