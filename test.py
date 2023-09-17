import time
import waehrungUmrechner as waehrung

while True:
    crypto = waehrung.euro_cryptop()
    if crypto == -1:
        continue
    print("EURO => US Doller ", waehrung.convert('EUR','USD', 1))
    print("BITCOIN => EURO", crypto[0])
    print("DOGECOIN => EURO", crypto[1])
    print("ETHIRIUM => EURO", crypto[2])
    print("------------")
    time.sleep(5)