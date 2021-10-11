# Use GPIO with Swarm
https://stackoverflow.com/questions/30059784/docker-access-to-raspberry-pi-gpio-pins
## use with swarm
https://blog.alexellis.io/gpio-on-swarm/

    devices:
      - /dev/
      - /dev/mem
      - /dev/gpiomem

      - /dev/i2c-1
      - /dev/i2c-0
      - /dev/i2c/1
      - /dev/i2c/0

      - /dev/gpio
