EESchema Schematic File Version 2  date Saturday 01 October 2011 01:21:50 PM IST
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:ac
EELAYER 24  0
EELAYER END
$Descr A4 11700 8267
Sheet 1 1
Title ""
Date "26 sep 2011"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Connection ~ 5600 4200
Wire Wire Line
	5600 4300 5600 4200
Wire Wire Line
	6550 3350 6550 3150
Wire Wire Line
	6550 3150 5850 3150
Wire Wire Line
	4850 3300 4850 3150
Wire Wire Line
	4850 3150 5450 3150
Wire Wire Line
	4850 4200 6550 4200
Wire Wire Line
	6550 4200 6550 3850
$Comp
L GND #PWR01
U 1 1 4E800CCE
P 5600 4300
F 0 "#PWR01" H 5600 4300 30  0001 C CNN
F 1 "GND" H 5600 4230 30  0001 C CNN
	1    5600 4300
	1    0    0    -1  
$EndComp
$Comp
L V1 v1
U 1 1 4E800ACC
P 4850 3750
F 0 "v1" H 4650 3850 60  0000 C CNN
F 1 "AC" V 4500 3700 60  0000 C CNN
	1    4850 3750
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 4E8009EE
P 6550 3600
F 0 "R1" V 6630 3600 50  0000 C CNN
F 1 "1k" V 6550 3600 50  0000 C CNN
	1    6550 3600
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 4E8009E1
P 5650 3150
F 0 "C1" H 5700 3250 50  0000 L CNN
F 1 "3.3nf" H 5700 3050 50  0000 L CNN
	1    5650 3150
	0    1    1    0   
$EndComp
$EndSCHEMATC
