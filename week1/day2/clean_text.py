import re

def clean(text: str) -> str:
    lower = text.lower()
    depunc = re.sub(pattern = "[^\w\d\s]", repl = "", string = lower)
    striped = re.sub(pattern = "\s+", repl = " ", string = depunc)
    return striped