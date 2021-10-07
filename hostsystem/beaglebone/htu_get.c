#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <linux/i2c-dev.h>


int fdev = open("/dev/i2c-1", O_RDWR); // open i2c bus

if (fdev < 0) {
    fprintf(stderr, "Failed to open I2C interface %s Error: %s\n", dev_path, strerror(errno));
    return -1;
}

unsigned char i2c_addr = 0x40;

// set slave device address 0x40
if (ioctl(fdev, I2C_SLAVE, i2c_addr) < 0) {
    fprintf(stderr, "Failed to select I2C slave device! Error: %s\n", strerror(errno));
    return -1;
}