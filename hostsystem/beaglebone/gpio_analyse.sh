#!/bin/sh

## Dieses Skript analysiert die GPIO des BeagleBone Black

# Informationen über PINs in Verwendung
/sys/kernel/debug/pinctrl/44e10800.pinmux# cat pingroups

# Information über zugewiesene PINs in verwendung
sys/kernel/debug/pinctrl/44e10800.pinmux# cat pinmux-pins |more

# Liste alles PINs
/sys/kernel/debug/pinctrl/44e10800.pinmux# cat pins |more
