import RPi.GPIO as gpio
from time import sleep
from time import perf_counter_ns
from sys import exit
from xskey import XSKey

SDAT = 24
CTRL = 23

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(SDAT, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(CTRL, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.add_event_detect(CTRL, gpio.RISING)
    gpio.add_event_detect(SDAT, gpio.RISING)

    
def list_to_bin(byte: list, endian='big') -> int:
    byte_s = byte
    if endian == 'big':
        byte_s.reverse()
        return sum(b << i for i, b in enumerate(byte_s))
    elif endian == 'little':
        return sum(b << i for i, b in enumerate(byte_s))
    else:
        print(f'unknown endian scheme: \'{endian}\'')
        return 0

def recv(): 
    byte = [None] * 8
    try:   
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
        val = XSKey(B)
        print(f"{val.name:<20}", end=' ')
    except KeyboardInterrupt:
        print()
        return False
    except ValueError:
        print("read_data.py: not a predefined key in XSKey():", end=' ')

    print(f"{bin(B):>12} or {hex(B)} or {B}")
    return True

def main():
    setup()
    print('To end execution, press Ctrl+C (^C) and then a key on the remote')
    print('Press a key on the Kenwood RC-5030 remote control...')
    status = True
    while status is True:
        status = recv()

    gpio.cleanup() 


if __name__ == '__main__': 
    main()
