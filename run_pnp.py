#!/usr/bin/env python

from tasks.pnp_sim import PickAndPlace
import baxter_interface
import signal
import sys


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    rs = baxter_interface.RobotEnable(baxter_interface.CHECK_VERSION)
    if rs.state().enabled:
        print("Disabling Baxter.")
        rs.disable()

    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C')

    pnp = PickAndPlace(
        #place_position=[0.7, -0.5, -0.2],
        place_position=[0.6, 0.6, 0.05],
    )
    pnp.run()
