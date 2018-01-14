from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    Pin25 = GP.getPin25()
    Pin25.out()

    for x in range(0, 60):
        Pin25.high()
        Pin25.low()

finally:
    GP.cleanup()

