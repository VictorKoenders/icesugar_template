import os
import subprocess

from nmigen.build import *
from nmigen.vendor.lattice_ice40 import *
from .resources import *


__all__ = ["ICESugarPlatform"]


class ICESugarPlatform(LatticeICE40Platform):
    device = "iCE40UP5K"
    package = "SG48"
    default_clk = "clk12"
    resources = [
        Resource("clk12", 0, Pins("35", dir="i"),
                 Clock(12e6), Attrs(GLOBAL=True, IO_STANDARD="SB_LVCMOS")),

        *LEDResources(pins="39 40 41", invert=True,
                      attrs=Attrs(IO_STANDARD="SB_LVCMOS")),
        # Semantic aliases
        Resource("led_b", 0, PinsN("39", dir="o"),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("led_g", 0, PinsN("41", dir="o"),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("led_r", 0, PinsN("40", dir="o"),
                 Attrs(IO_STANDARD="SB_LVCMOS")),

        UARTResource(0,
                     rx="4", tx="6",
                     attrs=Attrs(IO_STANDARD="SB_LVTTL", PULLUP=1)
                     ),

        *SPIFlashResources(0,
                           cs_n="16", clk="15", copi="14", cipo="17", wp_n="12", hold_n="13",
                           attrs=Attrs(IO_STANDARD="SB_LVCMOS")
                           ),


    ]

    connectors = [
        Connector("pmod", 0, "10  6  3 48 - -  9  4  2 47 - -"),  # PMOD1
        Connector("pmod", 1, "46 44 42 37 - - 45 43 38 36 - -"),  # PMOD2
        Connector("pmod", 2, "34 31 27 25 - - 32 28 26 23 - -"),  # PMOD3
        Connector("pmod", 3, "21 20 19 18 - -"),  # PMOD4
    ]

    dip_switch_pmod = [
        Resource("but", 0, Pins("21", dir="o", conn=("pmod", 3)),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("but", 1, Pins("20", dir="o", conn=("pmod", 3)),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("but", 2, Pins("19", dir="o", conn=("pmod", 3)),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
        Resource("but", 3, Pins("18", dir="o", conn=("pmod", 3)),
                 Attrs(IO_STANDARD="SB_LVCMOS")),
    ]

    def toolchain_program(self, products, name):
        iceprog = os.environ.get("ICEPROG", "iceprog")
        with products.extract("{}.bin".format(name)) as bitstream_filename:
            subprocess.check_call([iceprog, bitstream_filename])
