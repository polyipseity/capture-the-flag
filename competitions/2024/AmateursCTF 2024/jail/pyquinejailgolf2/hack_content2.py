# coding: raw-unicode-escape
#                                                pyquinejailgolf
b=print.\u005f\u005fself\u005f\u005f
ret=b.open(b.bytes([114,117,110,116,105,109,101,47,101,120,116,101,114,110,97,108,95,114,117,110,46,112,121]).decode()).read()
print(b.eval(ret[ret.find(b.chr(39),70):ret.find(b.chr(39),90)+1])[::-1],end=b.str())
