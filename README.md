## For Ardupilot Customizable controller

### Usefull links

1) Main webpage for developer- https://ardupilot.org/dev/docs/building-setup-linux.html
2) To clean ardupilot github repository on Ubuntu ```./waf distclean```
3) Learning base code - https://ardupilot.org/dev/docs/learning-the-ardupilot-codebase.html
4) Ardupilot Libraries for sensors, controller - https://ardupilot.org/dev/docs/apmcopter-programming-libraries.html
5) Link to build the code - https://github.com/ArduPilot/ardupilot/blob/master/BUILD.md

### Getting started with Ardupilot code

1) To download Ardupilot repo\
    $ git clone --recursive https://github.com/ArduPilot/ardupilot.git
2) Go to ardupilot directory and type following code to build the fmv3 version. After successfully building it you will see fmv3 named folder in build directory. After that run following code to burn on Pixhawk\
    ```./waf configure --board fmuv3```\
    ```./waf copter```\
2.1) Go to ardupilot directory and type following code to build the fmv2 version. After successfully building it you will see pixhawk1 named folder in build directory. After that run following code to burn on Pixhawk\
    ```./waf configure --board pxhawk1```\
    ```./waf copter```
3) To upload the code on the Pixhawk use following code in ardupilot main directory\
    ```./waf --targets bin/arducopter --upload```
    or \
    ```./waf copter --upload```

4) If you got the error  ```Waf: Entering directory `/home/user/ardupilot/build/navio2'
Command ['/usr/bin/git', 'rev-parse', '--short=8', 'HEAD'] returned 128 ``` when you are working on git based ardupilot directory.

Go to Tools/ardupilotwaf/git_submodule.py and modified following method

```
def _git_head_hash(ctx, path, short=False):
    cmd = [ctx.env.get_flat('GIT'), 'rev-parse']
    if short:
        cmd.append('--short=8')
    cmd.append('HEAD')
    out = ctx.cmd_and_log(cmd, quiet=Context.BOTH, cwd=path)
    return out.strip()
```
    
to 

```
def _git_head_hash(ctx, path, short=False):
    return "deadc0de"
```
    
    

### UART Ports on Ardupilot https://ardupilot.org/dev/docs/learning-ardupilot-uarts-and-the-console.html

1) Followings are the UART ports on the Pixhawk
* uartA - the console (usually USB, runs MAVLink telemetry) (Serial 0)
* uartB - the first GPS  (Serial 3) [+5v], [TX], [RX], [CAN2 TX], [CAN2RX], [GND]
* uartC - primary telemetry (telem1 on most autopilots)  (Serial 1) [+5v], [TX], [RX], [CTS], [RTS], [GND]
* uartD - secondary telemetry (telem2 on most autopilots)  (Serial 2) [+5v], [TX], [RX], [CTS], [RTS], [GND]
* uartE - 2nd GPS (Serial 4/5)  (Serial 4 and 5) [5v], [TX4], [RX4], [TX5], [RX5], [GND]
* uartF - User Configurable  (Serial 0)
* uartG - User Configurable  (Serial 0)
* uartH - User Configurable  (Serial 0)

2) Some basic codes
* printf - formatted print
* printf_P - formatted print with progmem string (saves memory on AVR boards)
* println - print and line feed
* write - write a bunch of bytes
* read - read some bytes
* available - check if any bytes are waiting
* txspace - check how much outgoing buffer space is available
* get_flow_control - check if the UART has flow control capabilities

### For mission planner message - ```https://ardupilot.org/dev/docs/debug-with-send-text.html```

### Useful notes


1) The "_with_bl.hex": (it will be at build->name_of_board-> bin) file contains the bootloader and is used for flashing to Ardupilot from other firmware... 
2) The "..apj": (it will be at build->name_of_board-> bin) is used by mission planner to update firmware on existing Ardupilot installations as a local firmware file

### If functions in UserCode.cpp files are disabled/showing less brightened

1) Go to APM_Config.h file and uncomment the respective functions.


## For CAM device

1) Serial port configuration - https://docs.px4.io/master/en/peripherals/serial_configuration.html
2) Change the parameters [MAV_2_CONFIG] to TELEM 2, [MAV_2_RATE] to 38400 (considering 4 bits of data), 
3) Bit rate (B/s) = baud rate * the number of bit per baud - i.e., if buad rate = 9600,\\

    a) Bit rate – the number of binary ‘bits’, 1s or 0s to be transmitted per second\
    b) Baud rate – the number of line ‘symbols’ transmitted per second

4) Serial port mapping - (the location on the firmware is - PX4-Autopilot/boards/px4/fmu-v3/default.cmake)\
    SERIAL_PORTS\
	* GPS1:/dev/ttyS0\
	* TEL1:/dev/ttyS1\
	* TEL2:/dev/ttyS2\
	* TEL4:/dev/ttyS6\

5) Sample code - https://programmer.help/blogs/5e35463a2dbdb.html
