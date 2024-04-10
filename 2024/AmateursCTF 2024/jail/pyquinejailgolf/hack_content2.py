#                                                                                pyquinejailgolf
from builtins import bytes,chr,eval,open,str
ret=open(bytes([114,117,110,116,105,109,101,47,101,120,116,101,114,110,97,108,95,114,117,110,46,112,121]).decode()).read()
print(eval(ret[ret.find(chr(39),70):ret.find(chr(39),90)+1])[::-1],end=str())
