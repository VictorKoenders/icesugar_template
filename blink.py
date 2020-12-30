from nmigen import *
from nmigen.build import Platform

# Simple blink script. Call this with:
# ```python
# blink = Blink(12000000) # blink once a second, the icesugar runs at 12mhz
# led = platform.request('led_r')
#
# m = Module()
# m.submodules += blink
# m.d.comb += led.eq(blink.state)
# ```


class Blink(Elaboratable):
    def __init__(self, period, initial_state=1):
        self.period = Const(period)
        # The state of the led
        # On the icesugar, the LEDs are pull-up, so they'll be off when the state is 1
        self.state = Signal(initial_state)
        # Counter that counts down from `period` to 0
        self.counter = Signal(range(period+1))

    def elaborate(self, platform: Platform) -> Module:
        m = Module()
        with m.If(self.counter == 0):
            # If we're at 0, reset the `counter` and toggle the `state`
            m.d.sync += [
                self.counter.eq(self.period),
                self.state.eq(~self.state),
            ]
        with m.Else():
            # Else count down 1
            m.d.sync += [
                self.counter.eq(self.counter-1)
            ]
        return m
