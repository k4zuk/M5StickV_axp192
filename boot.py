import lcd
import pmu
import time

eval_commands = [
    "getUSBVoltage()",
    "getUSBInputCurrent()",
#    "getConnextVoltage()",
#    "getConnextInputCurrent()",
    "getVbatVoltage()",
    "getBatteryChargeCurrent()",
    "getBatteryDischargeCurrent()",
#    "getBatteryInstantWatts()",
    "getTemperature()"
]

lcd.init()
lcd.rotation(2) #Rotate the lcd 180deg

axp = pmu.axp192()
axp.enableADCs(True)

n = min(len(eval_commands), 8)
while 1:
    for i in range(n):
        cmd = eval_commands[i]
        ret = eval("axp." + cmd)
        s = str(ret) + " #" + cmd
        lcd.draw_string(0, i*16, s, lcd.GREEN, lcd.BLACK)

    time.sleep(1)
