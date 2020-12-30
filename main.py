#!/usr/bin/python3

from nmigen import *
from nmigen_boards.icesugar import ICESugarPlatform
import shutil
import os

from blink import Blink


class Top(Elaboratable):
    def elaborate(self, platform):
        # Get the 3 LEDs
        led_r = platform.request('led_r')
        led_g = platform.request('led_g')
        led_b = platform.request('led_b')

        # Get the blink frequency for each LED
        blink_r = Blink(6000000)
        blink_g = Blink(12000000)
        blink_b = Blink(24000000)

        # Build the module
        m = Module()

        # Register the blink modules as submodules
        m.submodules += [blink_r, blink_g, blink_b]

        # Make sure that each LED is wired up to the `blink_x.led`
        m.d.comb += [
            led_r.eq(blink_r.state),
            led_g.eq(blink_g.state),
            led_b.eq(blink_b.state)
        ]

        return m


if __name__ == '__main__':
    print("Building platform... (Run with NMIGEN_verbose=\"True\" for debug information)")

    platform = ICESugarPlatform()
    platform.build(Top())
    print("Done!")

    FILE = "top.bin"
    ICELINK_DIR = "/media/" + os.getenv("USER") + "/iCELink/"

    if not os.path.exists(ICELINK_DIR):
        print("Could not find iCELink directory, checked these locations:")
        print("  " + ICELINK_DIR)
        print("Bitstream not uploaded")
    else:
        print("Uploading bitstream...")
        shutil.copyfile("build/" + FILE, ICELINK_DIR + FILE)
        print("Done!")
