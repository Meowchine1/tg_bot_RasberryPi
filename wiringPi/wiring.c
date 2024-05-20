#include "wiring.h"

// ----------------------TURN ONN MODE--------------------------------
void set_mode1()
{
    state = MODE1;
    led1_state = 1;
    digitalWrite(LED1, led1_state);
}

void set_mode2()
{
    state = MODE2;
    rele_state = 1;
    led2_state = 1;
    digitalWrite(LED2, led2_state);
    mode2_start_time = millis();
}

void set_mode3()
{
    state = MODE3;
    rele_state = 1;
    led1_state = 1;
    led3_state = 1;
    digitalWrite(LED1, led1_state);
    digitalWrite(LED3, led3_state);
}

void set_releoff()
{
    state = RELEOFF;
    rele_state = 0;
    led3_state = 1;
    digitalWrite(LED3, led3_state);
}

// ----------------------TURN OFF MODE--------------------------------
void turnoff_mode1()
{
    led1_state = 0;
    digitalWrite(LED1, led1_state);
}

void turnoff_mode2()
{
    led2_state = 0;
    digitalWrite(LED2, led2_state);
}

void turnoff_mode3()
{
    led1_state = 0;
    led3_state = 0;
    digitalWrite(LED1, led1_state);
    digitalWrite(LED3, led3_state);
}

void turnoff_releoff()
{
    led3_state = 0;
    digitalWrite(LED3, led3_state);
}