# VS Code Pico Setup - Mac

This project is set up for editing in VS Code and deploying to the Yahboom Pico Robot with `mpremote`.

## One-time Mac setup

From this folder:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements-dev.txt
code .
```

In VS Code, install the Microsoft Python extension if it is not already installed. The workspace points Python at `.venv/bin/python`.

## Firmware

For a Raspberry Pi Pico 2, use the included `RPI_PICO2` UF2:

- `firmware/RPI_PICO2-20240809-v1.24.0-preview.201.g269a0e0e1.uf2`

Use this `RPI_PICO2` file for Pico 2.

To flash:

1. Unplug the Pico USB cable.
2. Hold `BOOTSEL`.
3. Plug USB into the Mac while still holding `BOOTSEL`.
4. Release `BOOTSEL` after the `RPI-RP2` drive appears.
5. Copy the Pico 2 UF2 onto that drive.
6. Wait for the Pico to reboot.

## VS Code Tasks

Open Command Palette -> `Tasks: Run Task`.

- `Pico: list serial devices` checks whether `mpremote` can see the Pico.
- `Pico: deploy support files only` copies support modules without installing `main.py` as the startup program.
- `Pico: smoke test sensors` imports the support modules, stops motors, and prints basic sensor values.
- `Pico: motor test sequence` pulses the motors at test power with stops between each step.
- `Pico: motor battery diagnostic` checks ADC battery readings while each motor is pulsed.
- `Pico: ultrasonic readout` streams ultrasonic distance readings over serial.
- `Pico: simple line follow` runs a timed black-tape line-following test.
- `Pico: line until obstacle` follows the line and stops after confirmed ultrasonic obstacle detection.
- `Pico: drive until obstacle` drives straight and stops after confirmed ultrasonic obstacle detection.
- `Pico: line sensor readout` streams the four tracking sensor values.
- `Pico: IR remote readout` prints raw Yahboom IR remote key values.
- `Pico: manual control test` maps YahboomRobot app or IR remote commands to motors for a timed test.
- `Pico: deploy files` copies `pico_car.py`, `main.py`, `states.py`, `sensors.py`, and `motors.py` to the Pico, then resets it.
- `Pico: run main from RAM` runs `main.py` without saving it to the Pico filesystem.
- `Pico: open REPL` opens the MicroPython serial console.
- `Pico: show device files` lists files currently on the Pico.

## First Test

1. Power the robot safely with wheels off the table or lifted.
2. Connect Pico USB to the Mac normally, without holding `BOOTSEL`.
3. Run `Pico: list serial devices`.
4. Run `Pico: deploy support files only`.
5. Run `Pico: smoke test sensors`.
6. Run `Pico: motor test sequence` with the wheels lifted.
7. Run `Pico: run main from RAM` when you are ready for course movement.
8. Run `Pico: deploy files` only when you want `main.py` to start automatically on Pico reset or battery power.

If no serial device appears, try another USB cable. Many micro-USB cables are charge-only.
