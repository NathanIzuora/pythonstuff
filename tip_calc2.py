bill = float(input("How much is the bill?"))
service = input("How was the service: GOOD, FAIR, BAD?").upper()
guests = int(input("How many people?"))

goodtip = float(.20 * bill)
fairtip = float(.15 * bill)
badtip = float(.10 * bill)
goodtotal = float(goodtip + bill)
fairtotal = float(fairtip + bill)
badtotal = float(badtip + bill)

if service == "GOOD":
    print("tip:" , goodtip)
    print("grandtotal" , goodtotal)
    print("pay per guest" , (goodtotal / guests)
if service == "FAIR":
    print("tip:" , fairtip)
    print("grandtotal:" , fairtotat)
    print("pay per guest" , (fairtotal / guests)
if service == "BAD":
    print("tip:" , badtip)
    print("grandtotal:" , badtotal)
    print("amount per guests" , (badtotal / guests)