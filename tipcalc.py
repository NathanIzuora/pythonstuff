bill = float(input("What's the bill? "))

servicelevel = input("How was the service? GOOD? BAD? FAIR? ").upper()

goodtip = float(0.20 * bill)
fairtip = float(0.15 * bill)
badtip = float(0.10 * bill)
goodtotal = float(goodtip + bill)
fairtotal = float(fairtip + bill)
badtotal = float(badtip + bill)

if servicelevel == "GOOD":
    print("Tip: " + "{:.2f}".format(goodtip))
    print("Grand Total: ", "{:.2f}".format(goodtotal))
if servicelevel == "FAIR":
    print("Tip: ", "{:.2f}".format(fairtip))
    print("Grand Total: ", "{:.2f}".format(fairtotal))
if servicelevel == "BAD":
    print("Tip: ", "{:.2f}".format(badtip))
    print("Grand Total: ", "{:.2f}".format(badtotal))