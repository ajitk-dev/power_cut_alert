import time
import board 
import busio
from adafruit_ina219 import INA219


i2c = busio.I2C(board.SCL,board.SDA)
ina219=INA219(i2c)


BUZZER_PIN = 18



filename = "/home/Yelloskye/ina_219_power_cut/ina219_log.csv"

with open(filename,"w") as f:
    f.write("time(s),bus_voltage(V),shunt_voltage(V),current(mA),power(mW\n)")

    start = time.monotonic()
    power_cut_reported = False


    try:
        while True:
            bus_voltage=ina219.bus_voltage
            shunt_voltage = ina219.shunt_voltage
            current = ina219.current
            power = ina219.power


            elapsed = time.monotonic() - start
            line = f"{elapsed:.1f},{bus_voltage:.3f},{shunt_voltage:.5f},{current:.2f},{power:.2f}\n"
            f.write(line)
            f.flush()

            print(line,end="")


            if bus_voltage < 0.5:
                if not power_cut_reported:
                    print("power cut detected!")
                    'GPIO.output(BUZZER_PIN,GPIO.HIGH)'
                    power_cut_reported = True
                else:
                    if power_cut_reported:
                        print("Power restoed.Stopping buzzer.")
                    power_cut_reported = False
                time.sleep(5)
    except KeyboardInterrupt:
        print(f"\nLogging stopped.Data Saved in {filename}")            