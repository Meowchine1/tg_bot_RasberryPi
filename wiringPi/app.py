from wiringPi.state import *
import queue
# import multiprocessing as mp
# from multiprocessing.managers import NamespaceProxy, BaseManager

class App:
    def __init__(self):
        self.led1_state = 1
        self.led2_state = 0
        self.led3_state = 0
        self.rele_state = 0
        self.mode2_start_time = 0
        self.previousMillis = 0
        self.state = State.MODE1
        self.message_q = queue.Queue()

    def get_led1_state(self):
        return self.led1_state
    

    def get_led2_state(self):
        return self.led1_state
    
    def get_led3_state(self):
        return self.led1_state
    
    def get_rele_state(self):
        return self.led1_state
    
    def get_mode2_start_time(self):
        return self.led1_state
    
    def get_previousMillis(self):
        return self.led1_state
    
    def get_state(self):
        return self.led1_state
    
    def get_message_q(self):
        return self.led1_state
    

    def set_led1_state(self, led_st):
        self.led1_state = led_st
    

    def set_led2_state(self, led_st):
        self.led1_state = led_st
    
    def set_led3_state(self, led_st):
        self.led1_state = led_st
    
    def set_rele_state(self, led_st):
        self.led1_state = led_st
    
    def set_mode2_start_time(self, led_st):
        self.led1_state = led_st
    
    def set_previousMillis(self, led_st):
        self.led1_state = led_st
    
    def set_state(self, led_st):
        self.led1_state = led_st
    
    def set_message_q(self, led_st):
        self.led1_state = led_st
    
    
# class AppManager(BaseManager):
#     pass

# class AppProxy(NamespaceProxy):
#     _exposed_ = ('exposed_func' )


#     pass

# AppManager.register('AppClassRegistred', App, AppProxy)

# if __name__ == '__main__':
#     M = AppManager()
#     M.start()
#     MAC = M.AppClassRegistred()
#     p = mp.Process(target = changer, args=(MAC,))
#     p.start()
#     p.join()
#     print('Here I am: ', MAC.x)