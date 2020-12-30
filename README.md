# Icesugar FPGA quickstart project

## How to program

Simply run `./main.py`.
This will automatically build and upload the bitstream.

For more information, see this readme, `main.py` and `blink.py`.
If you still have questions, please open an issue so we can update the documentation.

## External links

- Learning nmigen: [nMigen tutorial](https://github.com/RobertBaruch/nmigen-tutorial/)
- Icesugar README: [Icesugar README](https://github.com/wuxx/icesugar/blob/master/README_en.md)

## Configuration

For more information, see the [nMigen tutorial, part 9](https://github.com/RobertBaruch/nmigen-tutorial/blob/b03a0eb449275ec4100d4d5dac551568a42601af/9_synthesis.md#class-properties)

### Resources

- clk12
- led_b (pin 39)
- led_g (pin 41)
- led_r (pin 40)
- uart (rx: 4, tx: 6)
- spi flash (cs: 16, clk: 15, copi: 14, cipo: 17, wp: 12, hold: 13)
- DIP switch / button
  - but 1: pin 21
  - but 2: pin 20
  - but 3: pin 19
  - but 4: pin 18

### Connectors

- pmod 1 (pin 10, 6, 3, 48, 9, 4, 2, 47)
- pmod 2 (pin 46, 44, 42, 37, 45, 43, 38, 36)
- pmod 3 (pin 34, 31, 27, 25, 32, 28, 26, 23)
- pmod 4 (pin 21, 20, 19, 18)
  - Hooked up to DIP switch / buttons

## Set up environment

**note:** You only have to set up this toolchain once on every system

Run `setup/setup.sh`, or you can do it manually by running the commands below:

Sources:
- [http://www.clifford.at/icestorm/](http://www.clifford.at/icestorm/)
- [https://nmigen.info/nmigen/latest/install.html#editable-development-snapshot](https://nmigen.info/nmigen/latest/install.html#editable-development-snapshot)

### icestorm

```bash
git clone https://github.com/YosysHQ/icestorm.git icestorm
cd icestorm
make -j$(nproc)
sudo make install
```

### nextpnr

```bash
git clone https://github.com/YosysHQ/nextpnr nextpnr
cd nextpnr
cmake -DARCH=ice40 -DCMAKE_INSTALL_PREFIX=/usr/local .
make -j$(nproc)
sudo make install
```

### yosys

```bash
git clone https://github.com/YosysHQ/yosys.git yosys
cd yosys
make -j$(nproc)
sudo make install
```

### nmigen

```bash
git clone https://github.com/nmigen/nmigen
cd nmigen
pip3 install --editable .[builtin-yosys]
```

### nmigen-boards

```bash
git clone https://github.com/nmigen/nmigen-boards
cd nmigen-boards

# Make sure to copy icesugar.py!
cp ../setup/icesugar.py nmigen_boards/

pip3 install --editable .[builtin-yosys]
```