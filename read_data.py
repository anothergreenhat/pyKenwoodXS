import RPi.GPIO as gpio
from time import sleep
from time import perf_counter_ns
from sys import exit

SDAT = 24
CTRL = 23

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(SDAT, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(CTRL, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.add_event_detect(CTRL, gpio.RISING)
    gpio.add_event_detect(SDAT, gpio.RISING)

    
def list_to_bin(byte, endian='big'):
    byte_s = byte
    if endian == 'big':
        byte_s.reverse()
        return sum(b << i for i, b in enumerate(byte_s))
    elif endian == 'little':
        return sum(b << i for i, b in enumerate(byte_s))
    else:
        print(f'unknown endian scheme: \'{endian}\'')
        return 0

def main():
    setup()
    print('To end execution, press Ctrl+C (^C) and then a key on the remote')
    print('Press a key on the Kenwood RC-5030 remote control...')
    try:
        while True:
            byte = [None] * 8
            
            # start bit
            gpio.wait_for_edge(SDAT, gpio.RISING)
            gpio.wait_for_edge(SDAT, gpio.FALLING)
            # end start bit
            
            
            # begin data bit receive
            for i in range(8):
                start = perf_counter_ns()
                gpio.wait_for_edge(SDAT, gpio.RISING)
                end = perf_counter_ns()
                byte[i] = 1 if ((end - start) < 9e6) else 0
                gpio.wait_for_edge(SDAT, gpio.FALLING)
                
            # ctrl goes low which means tranmission has ended
            gpio.wait_for_edge(CTRL, gpio.FALLING)
            B = list_to_bin(byte)
            print(bin(B), 'or', hex(B), 'or', B)
    except KeyboardInterrupt:
        print()
        exit(0)
    finally:
        gpio.cleanup()
   
   
    
main()
