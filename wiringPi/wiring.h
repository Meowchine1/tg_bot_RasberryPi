#include <wiringPi.h> // Include WiringPi library!

// ----------------------LEDS----------------------
#define LED1 0
#define LED2 2
#define LED3 3
#define RELE 4

uint8_t led1_state = 1;
uint8_t led2_state = 0;
uint8_t led3_state = 0;
uint8_t rele_state = 0;

const uint16_t BLINK_INTERVAL = 500;
unsigned long previousMillis = 0;

// ---------------------- SYGNAL --------------------
#define SYGNAL 5

// ----------------------MODE VARIABLES--------------------------------

typedef enum
{
    MODE1,  // штатный режим, при прерывании сигнала переход в режим отключенного реле
    MODE2,  // режим без прерывания реле при прекращении сигнала (ограниченное время)
    MODE3,  // режим без прерывания реле при прекращении сигнала (неограниченное время)
    RELEOFF // режим отключенного реле

} State;

State state = MODE1;

//  MODE2 TIMER
unsigned long mode2_start_time = 0;
const uint32_t MODE2_INTERVAL = 300000;

void set_mode1();
void set_mode2();
void set_mode3();
void set_releoff();
void turnoff_mode1();
void turnoff_mode2();
void turnoff_mode3();
void turnoff_releoff();