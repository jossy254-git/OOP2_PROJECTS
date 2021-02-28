name = input("please enter your name:")
if len(name) >= 5:
    print(name.upper() + " "   +  "length is"   + " "  +  str(name))
else:
    print(name.lower() + " "  +  "length is"  + " "  +  str(name))