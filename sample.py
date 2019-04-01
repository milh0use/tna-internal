from tnadiscovery import Discovery

disco = Discovery()

result = disco.search("WO 95")
ia = disco.get_ia("C12345")
description = ia.get_description()
print(description)