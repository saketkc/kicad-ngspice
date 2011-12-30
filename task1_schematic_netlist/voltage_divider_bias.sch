EESchema Schematic File Version 2  date Monday 21 November 2011 02:10:57 AM IST
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
LIBS:voltage_divider_bias-cache
EELAYER 24  0
EELAYER END
$Descr A4 11700 8267
Sheet 1 1
Title "noname.sch"
Date "20 nov 2011"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	6450 3450 6450 3200
Wire Wire Line
	5850 3600 6050 3600
Wire Wire Line
	6050 3600 6050 3850
Connection ~ 4900 3850
Connection ~ 4900 4850
Wire Wire Line
	4900 4550 4900 4850
Wire Wire Line
	3900 3350 3900 1950
Wire Wire Line
	3900 1950 6450 1950
Wire Wire Line
	6450 4850 3900 4850
Wire Wire Line
	3900 4850 3900 3950
Wire Wire Line
	4700 5000 4700 4850
Connection ~ 4700 4850
Wire Wire Line
	4900 1950 4900 2700
Connection ~ 4900 1950
Wire Wire Line
	4900 4050 4900 3200
Wire Wire Line
	4900 3850 5050 3850
Wire Wire Line
	5050 3850 5050 3600
Wire Wire Line
	5050 3600 5250 3600
Wire Wire Line
	6450 2550 6450 2700
Wire Wire Line
	6450 4300 6450 4350
$Comp
L BATTERY v4
U 1 1 4EBCEEBC
P 5550 3600
F 0 "v4" H 5550 3800 50  0000 C CNN
F 1 "0" H 5550 3410 50  0000 C CNN
	1    5550 3600
	1    0    0    -1  
$EndComp
$Comp
L R R4
U 1 1 4EBCE764
P 4900 4300
F 0 "R4" V 4980 4300 50  0000 C CNN
F 1 "3.9k" V 4900 4300 50  0000 C CNN
	1    4900 4300
	1    0    0    -1  
$EndComp
$Comp
L TR U1
U 1 1 4EB1340B
P 6350 3850
F 0 "U1" H 6350 3850 60  0000 C CNN
F 1 "TR" H 6350 3750 60  0000 C CNN
	1    6350 3850
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 4EB9165C
P 6450 4600
F 0 "R3" V 6530 4600 50  0000 C CNN
F 1 "1.5k" V 6450 4600 50  0000 C CNN
	1    6450 4600
	1    0    0    -1  
$EndComp
$Comp
L BATTERY v3
U 1 1 4EB1216A
P 6450 2250
F 0 "v3" H 6450 2450 50  0000 C CNN
F 1 "0" H 6450 2060 50  0000 C CNN
	1    6450 2250
	0    1    1    0   
$EndComp
$Comp
L GND #PWR01
U 1 1 4EB0E9F4
P 4700 5000
F 0 "#PWR01" H 4700 5000 30  0001 C CNN
F 1 "GND" H 4700 4930 30  0001 C CNN
	1    4700 5000
	1    0    0    -1  
$EndComp
$Comp
L BATTERY v1
U 1 1 4EB0E9CA
P 3900 3650
F 0 "v1" H 3900 3850 50  0000 C CNN
F 1 "22" H 3900 3460 50  0000 C CNN
	1    3900 3650
	0    1    1    0   
$EndComp
$Comp
L R R1
U 1 1 4EB0E9BE
P 4900 2950
F 0 "R1" V 4980 2950 50  0000 C CNN
F 1 "39k" V 4900 2950 50  0000 C CNN
	1    4900 2950
	1    0    0    -1  
$EndComp
$Comp
L R R2
U 1 1 4EB0E9B3
P 6450 2950
F 0 "R2" V 6530 2950 50  0000 C CNN
F 1 "10k" V 6450 2950 50  0000 C CNN
	1    6450 2950
	1    0    0    -1  
$EndComp
$EndSCHEMATC
