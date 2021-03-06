# The MIT License (MIT)
# Copyright (c) 2017 Kionix Inc.
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
class register_base: pass
class registers(register_base):
	def __init__(self):
		self.KXG03_TEMP_OUT_L                                     = 0x00         
		self.KXG03_TEMP_OUT_H                                     = 0x01         
		self.KXG03_GYRO_XOUT_L                                    = 0x02         
		self.KXG03_GYRO_XOUT_H                                    = 0x03         
		self.KXG03_GYRO_YOUT_L                                    = 0x04         
		self.KXG03_GYRO_YOUT_H                                    = 0x05         
		self.KXG03_GYRO_ZOUT_L                                    = 0x06         
		self.KXG03_GYRO_ZOUT_H                                    = 0x07         
		self.KXG03_ACC_XOUT_L                                     = 0x08         
		self.KXG03_ACC_XOUT_H                                     = 0x09         
		self.KXG03_ACC_YOUT_L                                     = 0x0A         
		self.KXG03_ACC_YOUT_H                                     = 0x0B         
		self.KXG03_ACC_ZOUT_L                                     = 0x0C         
		self.KXG03_ACC_ZOUT_H                                     = 0x0D         
		self.KXG03_AUX1_OUT1                                      = 0x0E         # Auxiliary Sensor #1 output data bytes AUX1_OUT1 through AUX1_OUT6
		self.KXG03_AUX1_OUT2                                      = 0x0F         
		self.KXG03_AUX1_OUT3                                      = 0x10         
		self.KXG03_AUX1_OUT4                                      = 0x11         
		self.KXG03_AUX1_OUT5                                      = 0x12         
		self.KXG03_AUX1_OUT6                                      = 0x13         
		self.KXG03_AUX2_OUT1                                      = 0x14         # Auxiliary Sensor #2 output data bytes AUX2_OUT1 through AUX2_OUT6
		self.KXG03_AUX2_OUT2                                      = 0x15         
		self.KXG03_AUX2_OUT3                                      = 0x16         
		self.KXG03_AUX2_OUT4                                      = 0x17         
		self.KXG03_AUX2_OUT5                                      = 0x18         
		self.KXG03_AUX2_OUT6                                      = 0x19         
		self.KXG03_WAKE_CNT_L                                     = 0x1A         # Number of ODR cycles spent in wake state as measured in accelerometer ODRa_wake/ODRa_sleep periods. Data byte WAKE_CNT_L and WAKE_CNT_H.
		self.KXG03_WAKE_CNT_H                                     = 0x1B         
		self.KXG03_SLEEP_CNT_L                                    = 0x1C         # Number of ODR cycles spent in sleep state as measured in accelerometer ODRa_wake/ODRa_sleep periods. Data byte SLEEP_CNT_L and SLEEP_CNT_H.
		self.KXG03_SLEEP_CNT_H                                    = 0x1D         
		self.KXG03_BUF_SMPLEV_L                                   = 0x1E         # Reports the number of data packets (ODR cycles) currently stored in the buffer.
		self.KXG03_BUF_SMPLEV_H                                   = 0x1F         
		self.KXG03_BUF_PAST_L                                     = 0x20         # Reports the number of data packets lost since buffer has been filled.
		self.KXG03_BUF_PAST_H                                     = 0x21         
		self.KXG03_AUX_STATUS                                     = 0x22         # Reports the status of Auxiliary Sensors AUX1 and AUX2.
		self.KXG03_WHO_AM_I                                       = 0x30         # WHO_AM_I
		self.KXG03_SN1_MIR                                        = 0x31         # Individual Identification (serial number).
		self.KXG03_SN2_MIR                                        = 0x32         
		self.KXG03_SN3_MIR                                        = 0x33         
		self.KXG03_SN4_MIR                                        = 0x34         
		self.KXG03_STATUS1                                        = 0x36         
		self.KXG03_INT1_SRC1                                      = 0x37         
		self.KXG03_INT1_SRC2                                      = 0x38         
		self.KXG03_INT1_L                                         = 0x39         # Reading this register releases int1 source registers
		self.KXG03_STATUS2                                        = 0x3A         
		self.KXG03_INT2_SRC1                                      = 0x3B         
		self.KXG03_INT2_SRC2                                      = 0x3C         
		self.KXG03_INT2_L                                         = 0x3D         # Reading this register releases int2 source registers
		self.KXG03_ACCEL_ODR_WAKE                                 = 0x3E         # Accelerometer Wake Mode Control register.
		self.KXG03_ACCEL_ODR_SLEEP                                = 0x3F         
		self.KXG03_ACCEL_CTL                                      = 0x40         
		self.KXG03_GYRO_ODR_WAKE                                  = 0x41         # Gyroscope Wake Mode Control register.
		self.KXG03_GYRO_ODR_SLEEP                                 = 0x42         
		self.KXG03_STDBY                                          = 0x43         
		self.KXG03_CTL_REG_1                                      = 0x44         # Special control register 1
		self.KXG03_INT_PIN_CTL                                    = 0x45         
		self.KXG03_INT_PIN1_SEL                                   = 0x46         # Physical interrupt pin INT1 select register.
		self.KXG03_INT_PIN2_SEL                                   = 0x47         # Physical interrupt pin INT2 select register.
		self.KXG03_INT_MASK1                                      = 0x48         # Buffer Full Interrupt enable/mask bit.
		self.KXG03_INT_MASK2                                      = 0x49         # which axis and direction of detected motion can cause an interrupt.
		self.KXG03_FSYNC_CTL                                      = 0x4A         # External Synchronous control register.
		self.KXG03_WAKE_SLEEP_CTL1                                = 0x4B         
		self.KXG03_WAKE_SLEEP_CTL2                                = 0x4C         # WUF and BTS threshold mode.
		self.KXG03_WUF_TH                                         = 0x4D         
		self.KXG03_WUF_COUNTER                                    = 0x4E         
		self.KXG03_BTS_TH                                         = 0x4F         
		self.KXG03_BTS_COUNTER                                    = 0x50         
		self.KXG03_AUX_I2C_CTL_REG                                = 0x51         
		self.KXG03_AUX_I2C_SAD1                                   = 0x52         # Read/Write that should be used to store the SAD for auxiliary I2C device 1
		self.KXG03_AUX_I2C_REG1                                   = 0x53         # Read/Write that should be used to store the starting data register address for auxiliary I2C device 1
		self.KXG03_AUX_I2C_CTL1                                   = 0x54         # Register address for enable/disable control register for auxiliary I2C device
		self.KXG03_AUX_I2C_BIT1                                   = 0x55         # Defines bits to toggle in the control register for auxiliary I2C device 1
		self.KXG03_AUX_I2C_ODR1_W                                 = 0x56         # Defines register read controls for auxiliary I2C device 1
		self.KXG03_AUX_I2C_ODR1_S                                 = 0x57         # Defines register read controls for auxiliary I2C device 1
		self.KXG03_AUX_I2C_SAD2                                   = 0x58         
		self.KXG03_AUX_I2C_REG2                                   = 0x59         
		self.KXG03_AUX_I2C_CTL2                                   = 0x5A         
		self.KXG03_AUX_I2C_BIT2                                   = 0x5B         
		self.KXG03_AUX_I2C_ODR2_W                                 = 0x5C         
		self.KXG03_AUX_I2C_ODR1_S                                 = 0x57         # Defines register read controls for auxiliary I2C device 1
		self.KXG03_BUF_WMITH_L                                    = 0x75         # Buffer watermark threshold level L
		self.KXG03_BUF_WMITH_H                                    = 0x76         # Buffer watermark threshold level H
		self.KXG03_BUF_TRIGTH_L                                   = 0x77         # Buffer Trigger mode threshold L
		self.KXG03_BUF_TRIGTH_H                                   = 0x78         # Buffer Trigger mode threshold H
		self.KXG03_BUF_CTL2                                       = 0x79         # Read/write control register that controls sample buffer input in wake mode.
		self.KXG03_BUF_CTL3                                       = 0x7A         # Read/write control register that controls sample buffer input in sleep mode
		self.KXG03_BUF_CTL4                                       = 0x7B         # Read/write control register that controls aux1 and aux2 buffer input.
		self.KXG03_BUF_EN                                         = 0x7C         # Read/write control register that controls sample buffer operation.
		self.KXG03_BUF_STATUS                                     = 0x7D         # This register reports the status of the sample buffer trigger function.
		self.KXG03_BUF_CLEAR                                      = 0x7E         # Latched buffer status information and the entire sample buffer are cleared when any data is written to this register.
		self.KXG03_BUF_READ                                       = 0x7F         # Data from the buffer should be read using a single SAD+R command
class bits(register_base):
	def __init__(self):
		self.KXG03_AUX_STATUS_AUX2FAIL                            = (0x01 << 7)  # Aux2 command sequence failure flag
		self.KXG03_AUX_STATUS_AUX2ERR                             = (0x01 << 6)  # Aux2 data read error flag.
		self.KXG03_AUX_STATUS_AUX2ST_AUX2_DISABLED                = (0x00 << 4)  # Aux1 has not been enabled or ASIC has successfully sent disable cmd.
		self.KXG03_AUX_STATUS_AUX2ST_AUX2_WAITING_ENABLE          = (0x01 << 4)  # ASIC is attempting to enable aux sensor via enable sequence.
		self.KXG03_AUX_STATUS_AUX2ST_AUX2_WAITING_DISABLE         = (0x02 << 4)  # ASIC is attempting to disable aux sensor via disable sequence.
		self.KXG03_AUX_STATUS_AUX2ST_AUX2_RUNNING                 = (0x03 << 4)  # ASIC has successfully sent aux enable cmd.
		self.KXG03_AUX_STATUS_AUX1FAIL                            = (0x01 << 3)  # Aux1 command sequence failure flag
		self.KXG03_AUX_STATUS_AUX1ERR                             = (0x01 << 2)  # Aux1 data read error flag.
		self.KXG03_AUX_STATUS_AUX1ST_AUX1_DISABLED                = (0x00 << 0)  # Aux1 has not been enabled or ASIC has successfully sent disable cmd.
		self.KXG03_AUX_STATUS_AUX1ST_AUX1_WAITING_ENABLE          = (0x01 << 0)  # ASIC is attempting to enable aux sensor via enable sequence.
		self.KXG03_AUX_STATUS_AUX1ST_AUX1_WAITING_DISABLE         = (0x02 << 0)  # ASIC is attempting to disable aux sensor via disable sequence.
		self.KXG03_AUX_STATUS_AUX1ST_AUX1_RUNNING                 = (0x03 << 0)  # ASIC has successfully sent aux enable cmd.
		self.KXG03_WHO_AM_I_WIA_ID                                = (0x24 << 0)  # WHO_AM_I -value
		self.KXG03_STATUS1_INT1                                   = (0x01 << 7)  # Reports logical OR of non-masked interrupt sources sent to INT1
		self.KXG03_STATUS1_POR                                    = (0x01 << 6)  # Reset indicator.
		self.KXG03_STATUS1_AUX2_ACT                               = (0x01 << 5)  # Auxiliary sensor #2 active flag.
		self.KXG03_STATUS1_AUX1_ACT                               = (0x01 << 4)  # Auxiliary sensor #1 active flag.
		self.KXG03_STATUS1_AUX_ERR                                = (0x01 << 3)  
		self.KXG03_STATUS1_WAKE_SLEEP_SLEEP_MODE                  = (0x00 << 2)  # Sleep mode status
		self.KXG03_STATUS1_WAKE_SLEEP_WAKE_MODE                   = (0x01 << 2)  # Wake mode status
		self.KXG03_STATUS1_WAKE_SLEEP                             = (0x01 << 2)  
		self.KXG03_STATUS1_GYRO_RUN                               = (0x01 << 1)  # Gyro's run status
		self.KXG03_STATUS1_GYRO_START                             = (0x01 << 0)  # Gyro's start status
		self.KXG03_INT1_SRC1_INT1_BFI                             = (0x01 << 7)  # Buffer full interrupt.
		self.KXG03_INT1_SRC1_INT1_WMI                             = (0x01 << 6)  # Buffer water mark interrupt.
		self.KXG03_INT1_SRC1_INT1_WUFS                            = (0x01 << 5)  # Wake up function interrupt.
		self.KXG03_INT1_SRC1_INT1_BTS                             = (0x01 << 4)  # Back to sleep interrupt.
		self.KXG03_INT1_SRC1_INT1_DRDY_AUX2                       = (0x01 << 3)  # Aux2 data ready interrupt.
		self.KXG03_INT1_SRC1_INT1_DRDY_AUX1                       = (0x01 << 2)  # Aux1 data ready interrupt.
		self.KXG03_INT1_SRC1_INT1_DRDY_ACCTEMP                    = (0x01 << 1)  # Accelerometer / Temperature data ready interrupt.
		self.KXG03_INT1_SRC1_INT1_DRDY_GYRO                       = (0x01 << 0)  # Gyro data ready interrupt.
		self.KXG03_INT1_SRC2_INT1_XNWU                            = (0x01 << 5)  # Wake up event detected on x-axis, negative direction
		self.KXG03_INT1_SRC2_INT1_XPWU                            = (0x01 << 4)  # Wake up event detected on x-axis, positive direction.
		self.KXG03_INT1_SRC2_INT1_YNWU                            = (0x01 << 3)  # Wake up event detected on y-axis, negative direction
		self.KXG03_INT1_SRC2_INT1_YPWU                            = (0x01 << 2)  # Wake up event detected on y-axis, positive direction.
		self.KXG03_INT1_SRC2_INT1_ZNWU                            = (0x01 << 1)  # Wake up event detected on z-axis, negative direction.
		self.KXG03_INT1_SRC2_INT1_ZPWU                            = (0x01 << 0)  # Wake up event detected on z-axis, positive direction.
		self.KXG03_STATUS2_INT2                                   = (0x01 << 7)  # Reports logical OR of non-masked interrupt sources sent to INT2
		self.KXG03_STATUS2_POR                                    = (0x01 << 6)  # Reset indicator.
		self.KXG03_STATUS2_AUX2_ACT                               = (0x01 << 5)  # Auxiliary sensor #2 active flag.
		self.KXG03_STATUS2_AUX1_ACT                               = (0x01 << 4)  # Auxiliary sensor #1 active flag.
		self.KXG03_STATUS2_AUX_ERR                                = (0x01 << 3)  
		self.KXG03_STATUS2_WAKE_SLEEP_SLEEP_MODE                  = (0x00 << 2)  # Sleep mode status
		self.KXG03_STATUS2_WAKE_SLEEP_WAKE_MODE                   = (0x01 << 2)  # Wake mode status
		self.KXG03_STATUS2_WAKE_SLEEP                             = (0x01 << 2)  
		self.KXG03_STATUS2_GYRO_RUN                               = (0x01 << 1)  # Gyro's run status
		self.KXG03_STATUS2_GYRO_START                             = (0x01 << 0)  # Gyro's start status
		self.KXG03_INT2_SRC1_INT2_BFI                             = (0x01 << 7)  # Buffer full interrupt.
		self.KXG03_INT2_SRC1_INT2_WMI                             = (0x01 << 6)  # Buffer water mark interrupt.
		self.KXG03_INT2_SRC1_INT2_WUFS                            = (0x01 << 5)  # Wake up function interrupt.
		self.KXG03_INT2_SRC1_INT2_BTS                             = (0x01 << 4)  # Back to sleep interrupt.
		self.KXG03_INT2_SRC1_INT2_DRDY_AUX2                       = (0x01 << 3)  # Aux2 data ready interrupt.
		self.KXG03_INT2_SRC1_INT2_DRDY_AUX1                       = (0x01 << 2)  # Aux1 data ready interrupt.
		self.KXG03_INT2_SRC1_INT2_DRDY_ACCTEMP                    = (0x01 << 1)  # Accelerometer / Temperature data ready interrupt.
		self.KXG03_INT2_SRC1_INT2_DRDY_GYRO                       = (0x01 << 0)  # Gyro data ready interrupt.
		self.KXG03_INT2_SRC2_INT2_XNWU                            = (0x01 << 5)  # Wake up event detected on x-axis, negative direction
		self.KXG03_INT2_SRC2_INT2_XPWU                            = (0x01 << 4)  # Wake up event detected on x-axis, positive direction.
		self.KXG03_INT2_SRC2_INT2_YNWU                            = (0x01 << 3)  # Wake up event detected on y-axis, negative direction
		self.KXG03_INT2_SRC2_INT2_YPWU                            = (0x01 << 2)  # Wake up event detected on y-axis, positive direction.
		self.KXG03_INT2_SRC2_INT2_ZNWU                            = (0x01 << 1)  # Wake up event detected on z-axis, negative direction.
		self.KXG03_INT2_SRC2_INT2_ZPWU                            = (0x01 << 0)  # Wake up event detected on z-axis, positive direction.
		self.KXG03_ACCEL_ODR_WAKE_LPMODE_W_DISABLED               = (0x00 << 7)  # Accel low power mode is disabled in wake state. Accel operates at max sampling rate and navg_wake is ignored.
		self.KXG03_ACCEL_ODR_WAKE_LPMODE_W_ENABLED                = (0x01 << 7)  # Accel low power mode is enabled in wake state. Accel operates in duty cycle mode with number of samples set by navg_wake.
		self.KXG03_ACCEL_ODR_WAKE_LPMODE_W                        = (0x01 << 7)  
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_NO_AVG                   = (0x00 << 4)  # no average
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_2_SAMPLE_AVG             = (0x01 << 4)  
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_4_SAMPLE_AVG             = (0x02 << 4)  
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_8_SAMPLE_AVG             = (0x03 << 4)  
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_16_SAMPLE_AVG            = (0x04 << 4)  
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_32_SAMPLE_AVG            = (0x05 << 4)  
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_64_SAMPLE_AVG            = (0x06 << 4)  
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_128_SAMPLE_AVG           = (0x07 << 4)  
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_0P781                    = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_1P563                    = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_3P125                    = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_6P25                     = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_12P5                     = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_25                       = (0x05 << 0)  # odr 25Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_50                       = (0x06 << 0)  # odr 50Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_100                      = (0x07 << 0)  # odr 100Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_200                      = (0x08 << 0)  # odr 200Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_400                      = (0x09 << 0)  # odr 400Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_800                      = (0x0A << 0)  # odr 800Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_1600                     = (0x0B << 0)  # odr 1600Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_3200                     = (0x0C << 0)  # odr 3200Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_6400                     = (0x0D << 0)  # odr 6400Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_12800                    = (0x0E << 0)  # odr 12800Hz
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_51200                    = (0x0F << 0)  # odr 51200Hz
		self.KXG03_ACCEL_ODR_SLEEP_LPMODE_S_DISABLED              = (0x00 << 7)  
		self.KXG03_ACCEL_ODR_SLEEP_LPMODE_S_ENABLED               = (0x01 << 7)  
		self.KXG03_ACCEL_ODR_SLEEP_LPMODE_S                       = (0x01 << 7)  
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_NO_AVG                  = (0x00 << 4)  
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_2_SAMPLE_AVG            = (0x01 << 4)  
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_4_SAMPLE_AVG            = (0x02 << 4)  
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_8_SAMPLE_AVG            = (0x03 << 4)  
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_16_SAMPLE_AVG           = (0x04 << 4)  
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_32_SAMPLE_AVG           = (0x05 << 4)  
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_64_SAMPLE_AVG           = (0x06 << 4)  
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_128_SAMPLE_AVG          = (0x07 << 4)  
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_0P781                   = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_1P563                   = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_3P125                   = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_6P25                    = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_12P5                    = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_25                      = (0x05 << 0)  # odr 25Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_50                      = (0x06 << 0)  # odr 50Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_100                     = (0x07 << 0)  # odr 100Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_200                     = (0x08 << 0)  # odr 200Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_400                     = (0x09 << 0)  # odr 400Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_800                     = (0x0A << 0)  # odr 800Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_1600                    = (0x0B << 0)  # odr 1600Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_3200                    = (0x0C << 0)  # odr 3200Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_6400                    = (0x0D << 0)  # odr 6400Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_12800                   = (0x0E << 0)  # odr 12800Hz
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_51200                   = (0x0F << 0)  # odr 51200Hz
		self.KXG03_ACCEL_CTL_ACC_FS_S_2G                          = (0x00 << 6)  
		self.KXG03_ACCEL_CTL_ACC_FS_S_4G                          = (0x01 << 6)  
		self.KXG03_ACCEL_CTL_ACC_FS_S_8G                          = (0x02 << 6)  
		self.KXG03_ACCEL_CTL_ACC_FS_S_16G                         = (0x03 << 6)  
		self.KXG03_ACCEL_CTL_ACC_FS_W_2G                          = (0x00 << 2)  
		self.KXG03_ACCEL_CTL_ACC_FS_W_4G                          = (0x01 << 2)  
		self.KXG03_ACCEL_CTL_ACC_FS_W_8G                          = (0x02 << 2)  
		self.KXG03_ACCEL_CTL_ACC_FS_W_16G                         = (0x03 << 2)  
		self.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_256                    = (0x00 << 6)  # 256dps
		self.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_512                    = (0x01 << 6)  # 512dps
		self.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_1024                   = (0x02 << 6)  # 1024dps
		self.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_2048                   = (0x03 << 6)  # 2048dps
		self.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_10                     = (0x00 << 4)  # 10Hz
		self.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_20                     = (0x01 << 4)  # 20Hz
		self.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_40                     = (0x02 << 4)  # 40Hz
		self.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_160                    = (0x03 << 4)  # 160Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_0P781                     = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_1P563                     = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_3P125                     = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_6P25                      = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_12P5                      = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_25                        = (0x05 << 0)  # odr 25Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_50                        = (0x06 << 0)  # odr 50Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_100                       = (0x07 << 0)  # odr 100Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_200                       = (0x08 << 0)  # odr 200Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_400                       = (0x09 << 0)  # odr 400Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_800                       = (0x0A << 0)  # odr 800Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_1600                      = (0x0B << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_1600_2                    = (0x0C << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_1600_3                    = (0x0D << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_1600_4                    = (0x0E << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_1600_5                    = (0x0F << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_256                   = (0x00 << 6)  # 256dps
		self.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_512                   = (0x01 << 6)  # 512dps
		self.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_1024                  = (0x02 << 6)  # 1024dps
		self.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_2048                  = (0x03 << 6)  # 2048dps
		self.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_10                    = (0x00 << 4)  # 10Hz
		self.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_20                    = (0x01 << 4)  # 20Hz
		self.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_40                    = (0x02 << 4)  # 40Hz
		self.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_160                   = (0x03 << 4)  # 160Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_0P781                    = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_1P563                    = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_3P125                    = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_6P25                     = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_12P5                     = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_25                       = (0x05 << 0)  # odr 25Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_50                       = (0x06 << 0)  # odr 50Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_100                      = (0x07 << 0)  # odr 100Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_200                      = (0x08 << 0)  # odr 200Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_400                      = (0x09 << 0)  # odr 400Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_800                      = (0x0A << 0)  # odr 800Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600                     = (0x0B << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600_2                   = (0x0C << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600_3                   = (0x0D << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600_4                   = (0x0E << 0)  # odr 1600Hz
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600_5                   = (0x0F << 0)  # odr 1600Hz
		self.KXG03_STDBY_AUX2_STDBY_S_ENABLED                     = (0x00 << 7)  # Aux2 sensor is enabled in sleep state.
		self.KXG03_STDBY_AUX2_STDBY_S_DISABLED                    = (0x01 << 7)  # Aux2 sensor is disabled in sleep state.
		self.KXG03_STDBY_AUX2_STDBY_S                             = (0x01 << 7)  
		self.KXG03_STDBY_AUX1_STDBY_S_ENABLED                     = (0x00 << 6)  # Aux1 sensor is enabled in sleep state.
		self.KXG03_STDBY_AUX1_STDBY_S_DISABLED                    = (0x01 << 6)  # Aux1 sensor is disabled in sleep state.
		self.KXG03_STDBY_AUX1_STDBY_S                             = (0x01 << 6)  
		self.KXG03_STDBY_GYRO_STDBY_S_ENABLED                     = (0x00 << 5)  # Gyro sensor is enabled in sleep state.
		self.KXG03_STDBY_GYRO_STDBY_S_DISABLED                    = (0x01 << 5)  # Gyro sensor is disabled in sleep state.
		self.KXG03_STDBY_GYRO_STDBY_S                             = (0x01 << 5)  
		self.KXG03_STDBY_AUX2_STDBY_W_ENABLED                     = (0x00 << 3)  # Aux2 sensor is enabled in wake state.
		self.KXG03_STDBY_AUX2_STDBY_W_DISABLED                    = (0x01 << 3)  # Aux2 sensor is disabled in wake state.
		self.KXG03_STDBY_AUX2_STDBY_W                             = (0x01 << 3)  
		self.KXG03_STDBY_AUX1_STDBY_W_ENABLED                     = (0x00 << 2)  # Aux1 sensor is enabled in wake state.
		self.KXG03_STDBY_AUX1_STDBY_W_DISABLED                    = (0x01 << 2)  # Aux1 sensor is disabled in wake state.
		self.KXG03_STDBY_AUX1_STDBY_W                             = (0x01 << 2)  
		self.KXG03_STDBY_GYRO_STDBY_W_ENABLED                     = (0x00 << 1)  # Gyro sensor is enabled in wake state.
		self.KXG03_STDBY_GYRO_STDBY_W_DISABLED                    = (0x01 << 1)  # Gyro sensor is disabled in wake state.
		self.KXG03_STDBY_GYRO_STDBY_W                             = (0x01 << 1)  
		self.KXG03_STDBY_ACC_STDBY_ENABLED                        = (0x00 << 0)  # Accel sensor is enabled.
		self.KXG03_STDBY_ACC_STDBY_DISABLED                       = (0x01 << 0)  # Accel sensor is disabled.
		self.KXG03_STDBY_ACC_STDBY                                = (0x01 << 0)  
		self.KXG03_CTL_REG_1_RST                                  = (0x01 << 7)  # Active high soft reset.
		self.KXG03_CTL_REG_1_I2C_DIS_ENABLED                      = (0x00 << 5)  # I2C interface is not disabled
		self.KXG03_CTL_REG_1_I2C_DIS_DISABLED                     = (0x01 << 5)  # I2C interface is disabled
		self.KXG03_CTL_REG_1_I2C_DIS                              = (0x01 << 5)  # Active high I2C disable bit
		self.KXG03_CTL_REG_1_TEMP_STDBY_S_ENABLED                 = (0x00 << 4)  # Temperature output is enabled in sleep mode.
		self.KXG03_CTL_REG_1_TEMP_STDBY_S_DISABLED                = (0x01 << 4)  # Temperature output is disabled in sleep mode.
		self.KXG03_CTL_REG_1_TEMP_STDBY_S                         = (0x01 << 4)  
		self.KXG03_CTL_REG_1_TEMP_STDBY_W_ENABLED                 = (0x00 << 3)  # Temperature output is enabled in wake mode.
		self.KXG03_CTL_REG_1_TEMP_STDBY_W_DISABLED                = (0x01 << 3)  # Temperature output is disabled in wake mode.
		self.KXG03_CTL_REG_1_TEMP_STDBY_W                         = (0x01 << 3)  
		self.KXG03_CTL_REG_1_ACC_STPOL_NOT_INVERTED               = (0x00 << 1)  # Accel self-test polarity is not inverted..
		self.KXG03_CTL_REG_1_ACC_STPOL_INVERTED                   = (0x01 << 1)  # Accel self-test polarity is inverted..
		self.KXG03_CTL_REG_1_ACC_STPOL                            = (0x01 << 1)  
		self.KXG03_CTL_REG_1_ACC_ST                               = (0x01 << 0)  # Accel self-test is enabled.
		self.KXG03_INT_PIN_CTL_IEN2                               = (0x01 << 7)  # Active high enable for INT2 pin.
		self.KXG03_INT_PIN_CTL_IEA2_ACTIVE_LOW                    = (0x00 << 6)  
		self.KXG03_INT_PIN_CTL_IEA2_ACTIVE_HIGH                   = (0x01 << 6)  
		self.KXG03_INT_PIN_CTL_IEA2                               = (0x01 << 6)  # Interrupt polarity select for INT2 pin.
		self.KXG03_INT_PIN_CTL_IEL2_LATCHED                       = (0x00 << 4)  
		self.KXG03_INT_PIN_CTL_IEL2_PULSED_40US                   = (0x01 << 4)  
		self.KXG03_INT_PIN_CTL_IEL2_PULSED_160US                  = (0x02 << 4)  
		self.KXG03_INT_PIN_CTL_IEL2_REALTIME                      = (0x03 << 4)  
		self.KXG03_INT_PIN_CTL_IEN1                               = (0x01 << 3)  # Active high enable for INT1 pin.
		self.KXG03_INT_PIN_CTL_IEA1_ACTIVE_LOW                    = (0x00 << 2)  
		self.KXG03_INT_PIN_CTL_IEA1_ACTIVE_HIGH                   = (0x01 << 2)  
		self.KXG03_INT_PIN_CTL_IEA1                               = (0x01 << 2)  # Interrupt polarity select for INT1 pin.
		self.KXG03_INT_PIN_CTL_IEL1_LATCHED                       = (0x00 << 0)  
		self.KXG03_INT_PIN_CTL_IEL1_PULSED_40US                   = (0x01 << 0)  
		self.KXG03_INT_PIN_CTL_IEL1_PULSED_160US                  = (0x02 << 0)  
		self.KXG03_INT_PIN_CTL_IEL1_REALTIME                      = (0x03 << 0)  
		self.KXG03_INT_PIN1_SEL_BFI_P1                            = (0x01 << 7)  # Buffer Full Interrupt for INT1 pin.
		self.KXG03_INT_PIN1_SEL_WMI_P1                            = (0x01 << 6)  # Water Mark Interrupt for INT1 pin.
		self.KXG03_INT_PIN1_SEL_WUF_P1                            = (0x01 << 5)  # Wake Up Function Interrupt for INT1 pin.
		self.KXG03_INT_PIN1_SEL_BTS_P1                            = (0x01 << 4)  # Back To Sleep Function Interrupt for INT1 pin.
		self.KXG03_INT_PIN1_SEL_DRDY_AUX2_P1                      = (0x01 << 3)  # Data Ready Aux2 Interrupt for INT1 pin.
		self.KXG03_INT_PIN1_SEL_DRDY_AUX1_P1                      = (0x01 << 2)  # Data Ready AUX1 Interrupt for INT1 pin.
		self.KXG03_INT_PIN1_SEL_DRDY_ACCTEMP_P1                   = (0x01 << 1)  # Data Ready Accelerometer Interrupt for INT1 pin.
		self.KXG03_INT_PIN1_SEL_DRDY_GYRO_P1                      = (0x01 << 0)  # Data Ready Gyroscope Interrupt for INT1 pin.
		self.KXG03_INT_PIN2_SEL_BFI_P2                            = (0x01 << 7)  # Buffer Full Interrupt for INT2 pin.
		self.KXG03_INT_PIN2_SEL_WMI_P2                            = (0x01 << 6)  # Water Mark Interrupt for INT2 pin.
		self.KXG03_INT_PIN2_SEL_WUF_P2                            = (0x01 << 5)  # Wake Up Function Interrupt for INT2 pin.
		self.KXG03_INT_PIN2_SEL_BTS_P2                            = (0x01 << 4)  # Back To Sleep Function Interrupt for INT2 pin.
		self.KXG03_INT_PIN2_SEL_DRDY_AUX2_P2                      = (0x01 << 3)  # Data Ready Aux2 Interrupt for INT2 pin.
		self.KXG03_INT_PIN2_SEL_DRDY_AUX1_P2                      = (0x01 << 2)  # Data Ready AUX1 Interrupt for INT2 pin.
		self.KXG03_INT_PIN2_SEL_DRDY_ACCTEMP_P2                   = (0x01 << 1)  # Data Ready Accelerometer Interrupt for INT2 pin.
		self.KXG03_INT_PIN2_SEL_DRDY_GYRO_P2                      = (0x01 << 0)  # Data Ready Gyroscope Interrupt for INT2 pin.
		self.KXG03_INT_MASK1_BFIE                                 = (0x01 << 7)  # Buffer Full Interrupt enable/mask bit.
		self.KXG03_INT_MASK1_WMIE                                 = (0x01 << 6)  # Water Mark Interrupt enable/mask bit
		self.KXG03_INT_MASK1_WUFE                                 = (0x01 << 5)  # Wake-up Function Interrupt enable/mask bit.
		self.KXG03_INT_MASK1_BTSE                                 = (0x01 << 4)  # Back-to-sleep Function Interrupt enable/mask bit.
		self.KXG03_INT_MASK1_DRDY_AUX2                            = (0x01 << 3)  # Data Ready Aux2 Interrupt enable/mask bit.
		self.KXG03_INT_MASK1_DRDY_AUX1                            = (0x01 << 2)  # Data Ready AUX1 Interrupt enable/mask bit.
		self.KXG03_INT_MASK1_DRDY_ACCTEMP                         = (0x01 << 1)  # Data Ready Accelerometer / Temperature Interrupt enable/mask bit.
		self.KXG03_INT_MASK1_DRDY_GYRO                            = (0x01 << 0)  # Data Ready Gyroscope Interrupt enable/mask bit.
		self.KXG03_INT_MASK2_NXWUE                                = (0x01 << 5)  # x negative (x-) mask for WUF/BTS
		self.KXG03_INT_MASK2_PXWUE                                = (0x01 << 4)  # x positive (x+) mask for WUF/BTS
		self.KXG03_INT_MASK2_NYWUE                                = (0x01 << 3)  # y negative (y-) mask for WUF/BTS
		self.KXG03_INT_MASK2_PYWUE                                = (0x01 << 2)  # y positive (y+) mask for WUF/BTS
		self.KXG03_INT_MASK2_NZWUE                                = (0x01 << 1)  # z negative (z-) mask for WUF/BTS
		self.KXG03_INT_MASK2_PZWUE                                = (0x01 << 0)  # z positive (z+) mask for WUF/BTS
		self.KXG03_FSYNC_CTL_FSYNC_MODE_DISABLED                  = (0x00 << 4)  # FSYNC is disabled. SYNC pin is tri-stated.
		self.KXG03_FSYNC_CTL_FSYNC_MODE_INPUT_EXT                 = (0x01 << 4)  # FSYNC is enabled. Sync pin is onfigured as input pin. Buffer is updated in sync with external clock applied at SYNC pin.
		self.KXG03_FSYNC_CTL_FSYNC_MODE_INPUT                     = (0x02 << 4)  # FSYNC is enabled. Sync pin is configured as input pin.State of SYNC pin is stored in selected sensor's LSB bit.
		self.KXG03_FSYNC_CTL_FSYNC_MODE_OUTPUT                    = (0x03 << 4)  # FSYNC is disabled. SYNC pin is configured as output pin.
		self.KXG03_FSYNC_CTL_FSYNC_SEL_SEL000                     = (0x00 << 0)  # Definition according FSYNC_MODE selection
		self.KXG03_FSYNC_CTL_FSYNC_SEL_SEL001                     = (0x01 << 0)  # Definition according FSYNC_MODE selection
		self.KXG03_FSYNC_CTL_FSYNC_SEL_SEL010                     = (0x02 << 0)  # Definition according FSYNC_MODE selection
		self.KXG03_FSYNC_CTL_FSYNC_SEL_SEL011                     = (0x03 << 0)  # Definition according FSYNC_MODE selection
		self.KXG03_FSYNC_CTL_FSYNC_SEL_SEL100                     = (0x04 << 0)  # Definition according FSYNC_MODE selection
		self.KXG03_FSYNC_CTL_FSYNC_SEL_SEL101                     = (0x05 << 0)  # Definition according FSYNC_MODE selection
		self.KXG03_FSYNC_CTL_FSYNC_SEL_SEL110                     = (0x06 << 0)  # Definition according FSYNC_MODE selection
		self.KXG03_FSYNC_CTL_FSYNC_SEL_SEL111                     = (0x07 << 0)  # Definition according FSYNC_MODE selection
		self.KXG03_WAKE_SLEEP_CTL1_BTS_EN                         = (0x01 << 7)  # Active high back-to-sleep function enable
		self.KXG03_WAKE_SLEEP_CTL1_WUF_EN                         = (0x01 << 6)  # Active high wake-up function enable.
		self.KXG03_WAKE_SLEEP_CTL1_MAN_SLEEP                      = (0x01 << 5)  # Forces transition to sleep state.
		self.KXG03_WAKE_SLEEP_CTL1_MAN_WAKE                       = (0x01 << 4)  # Forces transition to wake state.
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_0P781                     = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_1P563                     = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_3P125                     = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_6P25                      = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_12P5                      = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_25                        = (0x05 << 0)  # odr 25Hz
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_50                        = (0x06 << 0)  # odr 50Hz
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_100                       = (0x07 << 0)  # odr 100Hz
		self.KXG03_WAKE_SLEEP_CTL2_TH_MODE_ABSOLUTE_THRESHOLD     = (0x00 << 1)  
		self.KXG03_WAKE_SLEEP_CTL2_TH_MODE_RELATIVE_THRESHOLD     = (0x01 << 1)  
		self.KXG03_WAKE_SLEEP_CTL2_TH_MODE                        = (0x01 << 1)  
		self.KXG03_WAKE_SLEEP_CTL2_C_MODE_COUNTER_CLEAR           = (0x00 << 0)  
		self.KXG03_WAKE_SLEEP_CTL2_C_MODE_COUNTER_DECREASE        = (0x01 << 0)  
		self.KXG03_WAKE_SLEEP_CTL2_C_MODE                         = (0x01 << 0)  # debounce counter clear mode.
		self.KXG03_AUX_I2C_CTL_REG_AUX_CTL_POL2                   = (0x01 << 5)  # Defines control bit polarity for aux2 enable/disable command sequences.
		self.KXG03_AUX_I2C_CTL_REG_AUX_CTL_POL1                   = (0x01 << 4)  # Defines control bit polarity for aux1 enable/disable command sequences.
		self.KXG03_AUX_I2C_CTL_REG_AUX_BUS_SPD_100HZ              = (0x00 << 3)  # FS speed
		self.KXG03_AUX_I2C_CTL_REG_AUX_BUS_SPD_400HZ              = (0x01 << 3)  # HS speed
		self.KXG03_AUX_I2C_CTL_REG_AUX_BUS_SPD                    = (0x01 << 3)  # Sets I2C bus speed.
		self.KXG03_AUX_I2C_CTL_REG_AUX_PULL_UP_DISABLED           = (0x00 << 2)  # Pull up disabled
		self.KXG03_AUX_I2C_CTL_REG_AUX_PULL_UP_ENABLED            = (0x01 << 2)  # Internal 1.5kohm pullup resistor enabled
		self.KXG03_AUX_I2C_CTL_REG_AUX_PULL_UP                    = (0x01 << 2)  # Active high pull up enable.
		self.KXG03_AUX_I2C_CTL_REG_AUX_BYPASS_BYPASSED            = (0x00 << 1)  # AUX I2C not bypassed
		self.KXG03_AUX_I2C_CTL_REG_AUX_BYPASS_NOT_BYPASSED        = (0x01 << 1)  # AUX I2C connected to main I2C pins. Pull up disabled
		self.KXG03_AUX_I2C_CTL_REG_AUX_BYPASS                     = (0x01 << 1)  # Active high bypass enable
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_NO_READ_BACK             = (0x00 << 4)  # No read back
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_1_READ_BACK              = (0x01 << 4)  # 1 read back
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_2_READ_BACK              = (0x02 << 4)  # 2 read back
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_3_READ_BACK              = (0x03 << 4)  # 3 read back
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_4_READ_BACK              = (0x04 << 4)  # 4 read back
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_5_READ_BACK              = (0x05 << 4)  # 5 read back
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_6_READ_BACK              = (0x06 << 4)  # 6 read back
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_DNE                      = (0x07 << 4)  # DNE
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_0P781                  = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1P563                  = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_3P125                  = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_6P25                   = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_12P5                   = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_25                     = (0x05 << 0)  # odr 25Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_50                     = (0x06 << 0)  # odr 50Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_100                    = (0x07 << 0)  # odr 100Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_200                    = (0x08 << 0)  # odr 200Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_400                    = (0x09 << 0)  # odr 400Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_800                    = (0x0A << 0)  # odr 800Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600                   = (0x0B << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600_2                 = (0x0C << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600_3                 = (0x0D << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600_4                 = (0x0E << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600_5                 = (0x0F << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_0P781                  = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1P563                  = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_3P125                  = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_6P25                   = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_12P5                   = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_25                     = (0x05 << 0)  # odr 25Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_50                     = (0x06 << 0)  # odr 50Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_100                    = (0x07 << 0)  # odr 100Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_200                    = (0x08 << 0)  # odr 200Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_400                    = (0x09 << 0)  # odr 400Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_800                    = (0x0A << 0)  # odr 800Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600                   = (0x0B << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600_2                 = (0x0C << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600_3                 = (0x0D << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600_4                 = (0x0E << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600_5                 = (0x0F << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_NO_READ_BACK             = (0x00 << 4)  # No read back
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_1_READ_BACK              = (0x01 << 4)  # 1 read back
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_2_READ_BACK              = (0x02 << 4)  # 2 read back
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_3_READ_BACK              = (0x03 << 4)  # 3 read back
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_4_READ_BACK              = (0x04 << 4)  # 4 read back
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_5_READ_BACK              = (0x05 << 4)  # 5 read back
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_6_READ_BACK              = (0x06 << 4)  # 6 read back
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_DNE                      = (0x07 << 4)  # DNE
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_0P781                  = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1P563                  = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_3P125                  = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_6P25                   = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_12P5                   = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_25                     = (0x05 << 0)  # odr 25Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_50                     = (0x06 << 0)  # odr 50Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_100                    = (0x07 << 0)  # odr 100Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_200                    = (0x08 << 0)  # odr 200Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_400                    = (0x09 << 0)  # odr 400Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_800                    = (0x0A << 0)  # odr 800Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600                   = (0x0B << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600_2                 = (0x0C << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600_3                 = (0x0D << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600_4                 = (0x0E << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600_5                 = (0x0F << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_0P781                  = (0x00 << 0)  # odr 0.781Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1P563                  = (0x01 << 0)  # odr 1.563Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_3P125                  = (0x02 << 0)  # odr 3.125Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_6P25                   = (0x03 << 0)  # odr 6.25Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_12P5                   = (0x04 << 0)  # odr 12.5Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_25                     = (0x05 << 0)  # odr 25Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_50                     = (0x06 << 0)  # odr 50Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_100                    = (0x07 << 0)  # odr 100Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_200                    = (0x08 << 0)  # odr 200Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_400                    = (0x09 << 0)  # odr 400Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_800                    = (0x0A << 0)  # odr 800Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600                   = (0x0B << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600_2                 = (0x0C << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600_3                 = (0x0D << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600_4                 = (0x0E << 0)  # odr 1600Hz
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600_5                 = (0x0F << 0)  # odr 1600Hz
		self.KXG03_BUF_CTL2_BUF_TEMP_W                            = (0x01 << 6)  # controls the Temperature input into the sample buffer
		self.KXG03_BUF_CTL2_BUF_ACC_W_X                           = (0x01 << 5)  # controls the Accelerometer axis input into the sample buffer
		self.KXG03_BUF_CTL2_BUF_ACC_W_Y                           = (0x01 << 4)  
		self.KXG03_BUF_CTL2_BUF_ACC_W_Z                           = (0x01 << 3)  
		self.KXG03_BUF_CTL2_BUF_GYR_W_X                           = (0x01 << 2)  # controls the Gyroscope axis input into the sample buffer.
		self.KXG03_BUF_CTL2_BUF_GYR_W_Y                           = (0x01 << 1)  
		self.KXG03_BUF_CTL2_BUF_GYR_W_Z                           = (0x01 << 0)  
		self.KXG03_BUF_CTL3_BUF_TEMP_S                            = (0x01 << 6)  # controls the Temperature input into the sample buffer.
		self.KXG03_BUF_CTL3_BUF_ACC_S_X                           = (0x01 << 5)  # controls the Accelerometer axis input into the sample buffer.
		self.KXG03_BUF_CTL3_BUF_ACC_S_Y                           = (0x01 << 4)  
		self.KXG03_BUF_CTL3_BUF_ACC_S_Z                           = (0x01 << 3)  
		self.KXG03_BUF_CTL3_BUF_GYR_S_X                           = (0x01 << 2)  # controls the Gyroscope axis input into the sample buffer.
		self.KXG03_BUF_CTL3_BUF_GYR_S_Y                           = (0x01 << 1)  
		self.KXG03_BUF_CTL3_BUF_GYR_S_Z                           = (0x01 << 0)  
		self.KXG03_BUF_CTL4_BUF_AUX2_S                            = (0x01 << 3)  # controls the aux2 input into the sample buffer in sleep mode.
		self.KXG03_BUF_CTL4_BUF_AUX1_S                            = (0x01 << 2)  # controls the aux1 axis input into the sample buffer in sleep mode
		self.KXG03_BUF_CTL4_BUF_AUX2_W                            = (0x01 << 1)  # controls the aux2 input into the sample buffer in wake mode.
		self.KXG03_BUF_CTL4_BUF_AUX1_W                            = (0x01 << 0)  
		self.KXG03_BUF_EN_BUFE                                    = (0x01 << 7)  
		self.KXG03_BUF_EN_BUF_SYM_SYMBOL_MODE_DISABLED            = (0x00 << 2)  
		self.KXG03_BUF_EN_BUF_SYM_SINGLE_SYMBOL_MODE_ENABLED      = (0x01 << 2)  
		self.KXG03_BUF_EN_BUF_SYM_DUAL_SYMBOL_TRANS_MODE_ENABLED  = (0x02 << 2)  
		self.KXG03_BUF_EN_BUF_SYM_DUAL_SYMBOL_FRAME_MODE_ENABLED  = (0x03 << 2)  
		self.KXG03_BUF_EN_BUF_M_FIFO                              = (0x00 << 0)  
		self.KXG03_BUF_EN_BUF_M_STREAM                            = (0x01 << 0)  
		self.KXG03_BUF_EN_BUF_M_TRIGGER                           = (0x02 << 0)  
		self.KXG03_BUF_EN_BUF_M_FILO                              = (0x03 << 0)  
		self.KXG03_BUF_STATUS_BUF_TRIG                            = (0x01 << 7)  
_b=bits()
class enums(register_base):
	def __init__(self):
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D={
			'DNE':_b.KXG03_AUX_I2C_ODR2_W_AUX2_D_DNE,
			'5_READ_BACK':_b.KXG03_AUX_I2C_ODR2_W_AUX2_D_5_READ_BACK,
			'2_READ_BACK':_b.KXG03_AUX_I2C_ODR2_W_AUX2_D_2_READ_BACK,
			'3_READ_BACK':_b.KXG03_AUX_I2C_ODR2_W_AUX2_D_3_READ_BACK,
			'NO_READ_BACK':_b.KXG03_AUX_I2C_ODR2_W_AUX2_D_NO_READ_BACK,
			'4_READ_BACK':_b.KXG03_AUX_I2C_ODR2_W_AUX2_D_4_READ_BACK,
			'6_READ_BACK':_b.KXG03_AUX_I2C_ODR2_W_AUX2_D_6_READ_BACK,
			'1_READ_BACK':_b.KXG03_AUX_I2C_ODR2_W_AUX2_D_1_READ_BACK,
		}
		self.KXG03_GYRO_ODR_WAKE_GYRO_FS_W={
			'1024':_b.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_1024,
			'512':_b.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_512,
			'256':_b.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_256,
			'2048':_b.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_2048,
		}
		self.KXG03_STDBY_AUX1_STDBY_S={
			'DISABLED':_b.KXG03_STDBY_AUX1_STDBY_S_DISABLED,
			'ENABLED':_b.KXG03_STDBY_AUX1_STDBY_S_ENABLED,
		}
		self.KXG03_WAKE_SLEEP_CTL2_C_MODE={
			'COUNTER_CLEAR':_b.KXG03_WAKE_SLEEP_CTL2_C_MODE_COUNTER_CLEAR,
			'COUNTER_DECREASE':_b.KXG03_WAKE_SLEEP_CTL2_C_MODE_COUNTER_DECREASE,
		}
		self.KXG03_FSYNC_CTL_FSYNC_MODE={
			'DISABLED':_b.KXG03_FSYNC_CTL_FSYNC_MODE_DISABLED,
			'INPUT_EXT':_b.KXG03_FSYNC_CTL_FSYNC_MODE_INPUT_EXT,
			'INPUT':_b.KXG03_FSYNC_CTL_FSYNC_MODE_INPUT,
			'OUTPUT':_b.KXG03_FSYNC_CTL_FSYNC_MODE_OUTPUT,
		}
		self.KXG03_STDBY_ACC_STDBY={
			'DISABLED':_b.KXG03_STDBY_ACC_STDBY_DISABLED,
			'ENABLED':_b.KXG03_STDBY_ACC_STDBY_ENABLED,
		}
		self.KXG03_STDBY_AUX1_STDBY_W={
			'DISABLED':_b.KXG03_STDBY_AUX1_STDBY_W_DISABLED,
			'ENABLED':_b.KXG03_STDBY_AUX1_STDBY_W_ENABLED,
		}
		self.KXG03_AUX_STATUS_AUX1ST={
			'AUX1_RUNNING':_b.KXG03_AUX_STATUS_AUX1ST_AUX1_RUNNING,
			'AUX1_WAITING_ENABLE':_b.KXG03_AUX_STATUS_AUX1ST_AUX1_WAITING_ENABLE,
			'AUX1_WAITING_DISABLE':_b.KXG03_AUX_STATUS_AUX1ST_AUX1_WAITING_DISABLE,
			'AUX1_DISABLED':_b.KXG03_AUX_STATUS_AUX1ST_AUX1_DISABLED,
		}
		self.KXG03_STDBY_AUX2_STDBY_S={
			'DISABLED':_b.KXG03_STDBY_AUX2_STDBY_S_DISABLED,
			'ENABLED':_b.KXG03_STDBY_AUX2_STDBY_S_ENABLED,
		}
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D={
			'DNE':_b.KXG03_AUX_I2C_ODR1_W_AUX1_D_DNE,
			'5_READ_BACK':_b.KXG03_AUX_I2C_ODR1_W_AUX1_D_5_READ_BACK,
			'2_READ_BACK':_b.KXG03_AUX_I2C_ODR1_W_AUX1_D_2_READ_BACK,
			'3_READ_BACK':_b.KXG03_AUX_I2C_ODR1_W_AUX1_D_3_READ_BACK,
			'NO_READ_BACK':_b.KXG03_AUX_I2C_ODR1_W_AUX1_D_NO_READ_BACK,
			'4_READ_BACK':_b.KXG03_AUX_I2C_ODR1_W_AUX1_D_4_READ_BACK,
			'6_READ_BACK':_b.KXG03_AUX_I2C_ODR1_W_AUX1_D_6_READ_BACK,
			'1_READ_BACK':_b.KXG03_AUX_I2C_ODR1_W_AUX1_D_1_READ_BACK,
		}
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S={
			'25':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_25,
			'0P781':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_0P781,
			'200':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_200,
			'12P5':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_12P5,
			'1600':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600,
			'50':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_50,
			'6P25':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_6P25,
			'1P563':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_1P563,
			'1600_4':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600_4,
			'3P125':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_3P125,
			'400':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_400,
			'100':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_100,
			'1600_5':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600_5,
			'1600_2':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600_2,
			'1600_3':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_1600_3,
			'800':_b.KXG03_GYRO_ODR_SLEEP_ODRG_S_800,
		}
		self.KXG03_INT_PIN_CTL_IEL2={
			'PULSED_160US':_b.KXG03_INT_PIN_CTL_IEL2_PULSED_160US,
			'PULSED_40US':_b.KXG03_INT_PIN_CTL_IEL2_PULSED_40US,
			'LATCHED':_b.KXG03_INT_PIN_CTL_IEL2_LATCHED,
			'REALTIME':_b.KXG03_INT_PIN_CTL_IEL2_REALTIME,
		}
		self.KXG03_INT_PIN_CTL_IEL1={
			'PULSED_160US':_b.KXG03_INT_PIN_CTL_IEL1_PULSED_160US,
			'PULSED_40US':_b.KXG03_INT_PIN_CTL_IEL1_PULSED_40US,
			'LATCHED':_b.KXG03_INT_PIN_CTL_IEL1_LATCHED,
			'REALTIME':_b.KXG03_INT_PIN_CTL_IEL1_REALTIME,
		}
		self.KXG03_STDBY_GYRO_STDBY_S={
			'DISABLED':_b.KXG03_STDBY_GYRO_STDBY_S_DISABLED,
			'ENABLED':_b.KXG03_STDBY_GYRO_STDBY_S_ENABLED,
		}
		self.KXG03_STATUS2_WAKE_SLEEP={
			'SLEEP_MODE':_b.KXG03_STATUS2_WAKE_SLEEP_SLEEP_MODE,
			'WAKE_MODE':_b.KXG03_STATUS2_WAKE_SLEEP_WAKE_MODE,
		}
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW={
			'25':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_25,
			'0P781':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_0P781,
			'200':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_200,
			'12P5':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_12P5,
			'1600':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600,
			'50':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_50,
			'6P25':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_6P25,
			'1P563':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1P563,
			'1600_4':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600_4,
			'3P125':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_3P125,
			'400':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_400,
			'100':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_100,
			'1600_5':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600_5,
			'1600_2':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600_2,
			'1600_3':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_1600_3,
			'800':_b.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_800,
		}
		self.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S={
			'1024':_b.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_1024,
			'512':_b.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_512,
			'256':_b.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_256,
			'2048':_b.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_2048,
		}
		self.KXG03_BUF_EN_BUF_M={
			'TRIGGER':_b.KXG03_BUF_EN_BUF_M_TRIGGER,
			'FILO':_b.KXG03_BUF_EN_BUF_M_FILO,
			'FIFO':_b.KXG03_BUF_EN_BUF_M_FIFO,
			'STREAM':_b.KXG03_BUF_EN_BUF_M_STREAM,
		}
		self.KXG03_CTL_REG_1_ACC_STPOL={
			'NOT_INVERTED':_b.KXG03_CTL_REG_1_ACC_STPOL_NOT_INVERTED,
			'INVERTED':_b.KXG03_CTL_REG_1_ACC_STPOL_INVERTED,
		}
		self.KXG03_WAKE_SLEEP_CTL1_OWUF={
			'25':_b.KXG03_WAKE_SLEEP_CTL1_OWUF_25,
			'0P781':_b.KXG03_WAKE_SLEEP_CTL1_OWUF_0P781,
			'12P5':_b.KXG03_WAKE_SLEEP_CTL1_OWUF_12P5,
			'50':_b.KXG03_WAKE_SLEEP_CTL1_OWUF_50,
			'1P563':_b.KXG03_WAKE_SLEEP_CTL1_OWUF_1P563,
			'3P125':_b.KXG03_WAKE_SLEEP_CTL1_OWUF_3P125,
			'100':_b.KXG03_WAKE_SLEEP_CTL1_OWUF_100,
			'6P25':_b.KXG03_WAKE_SLEEP_CTL1_OWUF_6P25,
		}
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S={
			'200':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_200,
			'6400':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_6400,
			'0P781':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_0P781,
			'3200':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_3200,
			'12P5':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_12P5,
			'1600':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_1600,
			'50':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_50,
			'6P25':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_6P25,
			'1P563':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_1P563,
			'3P125':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_3P125,
			'25':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_25,
			'12800':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_12800,
			'400':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_400,
			'100':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_100,
			'800':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_800,
			'51200':_b.KXG03_ACCEL_ODR_SLEEP_ODRA_S_51200,
		}
		self.KXG03_INT_PIN_CTL_IEA1={
			'ACTIVE_HIGH':_b.KXG03_INT_PIN_CTL_IEA1_ACTIVE_HIGH,
			'ACTIVE_LOW':_b.KXG03_INT_PIN_CTL_IEA1_ACTIVE_LOW,
		}
		self.KXG03_INT_PIN_CTL_IEA2={
			'ACTIVE_HIGH':_b.KXG03_INT_PIN_CTL_IEA2_ACTIVE_HIGH,
			'ACTIVE_LOW':_b.KXG03_INT_PIN_CTL_IEA2_ACTIVE_LOW,
		}
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS={
			'25':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_25,
			'0P781':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_0P781,
			'200':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_200,
			'12P5':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_12P5,
			'1600':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600,
			'50':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_50,
			'6P25':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_6P25,
			'1P563':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1P563,
			'1600_4':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600_4,
			'3P125':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_3P125,
			'400':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_400,
			'100':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_100,
			'1600_5':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600_5,
			'1600_2':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600_2,
			'1600_3':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_1600_3,
			'800':_b.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_800,
		}
		self.KXG03_STDBY_GYRO_STDBY_W={
			'DISABLED':_b.KXG03_STDBY_GYRO_STDBY_W_DISABLED,
			'ENABLED':_b.KXG03_STDBY_GYRO_STDBY_W_ENABLED,
		}
		self.KXG03_GYRO_ODR_WAKE_ODRG_W={
			'25':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_25,
			'0P781':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_0P781,
			'200':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_200,
			'12P5':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_12P5,
			'1600':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_1600,
			'50':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_50,
			'6P25':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_6P25,
			'1P563':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_1P563,
			'1600_4':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_1600_4,
			'3P125':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_3P125,
			'400':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_400,
			'100':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_100,
			'1600_5':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_1600_5,
			'1600_2':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_1600_2,
			'1600_3':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_1600_3,
			'800':_b.KXG03_GYRO_ODR_WAKE_ODRG_W_800,
		}
		self.KXG03_CTL_REG_1_I2C_DIS={
			'DISABLED':_b.KXG03_CTL_REG_1_I2C_DIS_DISABLED,
			'ENABLED':_b.KXG03_CTL_REG_1_I2C_DIS_ENABLED,
		}
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W={
			'4_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_WAKE_NAVG_W_4_SAMPLE_AVG,
			'16_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_WAKE_NAVG_W_16_SAMPLE_AVG,
			'8_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_WAKE_NAVG_W_8_SAMPLE_AVG,
			'NO_AVG':_b.KXG03_ACCEL_ODR_WAKE_NAVG_W_NO_AVG,
			'128_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_WAKE_NAVG_W_128_SAMPLE_AVG,
			'2_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_WAKE_NAVG_W_2_SAMPLE_AVG,
			'64_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_WAKE_NAVG_W_64_SAMPLE_AVG,
			'32_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_WAKE_NAVG_W_32_SAMPLE_AVG,
		}
		self.KXG03_ACCEL_CTL_ACC_FS_S={
			'4G':_b.KXG03_ACCEL_CTL_ACC_FS_S_4G,
			'2G':_b.KXG03_ACCEL_CTL_ACC_FS_S_2G,
			'8G':_b.KXG03_ACCEL_CTL_ACC_FS_S_8G,
			'16G':_b.KXG03_ACCEL_CTL_ACC_FS_S_16G,
		}
		self.KXG03_AUX_I2C_CTL_REG_AUX_BUS_SPD={
			'400HZ':_b.KXG03_AUX_I2C_CTL_REG_AUX_BUS_SPD_400HZ,
			'100HZ':_b.KXG03_AUX_I2C_CTL_REG_AUX_BUS_SPD_100HZ,
		}
		self.KXG03_GYRO_ODR_WAKE_GYRO_BW_W={
			'10':_b.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_10,
			'160':_b.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_160,
			'40':_b.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_40,
			'20':_b.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_20,
		}
		self.KXG03_ACCEL_CTL_ACC_FS_W={
			'4G':_b.KXG03_ACCEL_CTL_ACC_FS_W_4G,
			'2G':_b.KXG03_ACCEL_CTL_ACC_FS_W_2G,
			'8G':_b.KXG03_ACCEL_CTL_ACC_FS_W_8G,
			'16G':_b.KXG03_ACCEL_CTL_ACC_FS_W_16G,
		}
		self.KXG03_STDBY_AUX2_STDBY_W={
			'DISABLED':_b.KXG03_STDBY_AUX2_STDBY_W_DISABLED,
			'ENABLED':_b.KXG03_STDBY_AUX2_STDBY_W_ENABLED,
		}
		self.KXG03_ACCEL_ODR_SLEEP_LPMODE_S={
			'DISABLED':_b.KXG03_ACCEL_ODR_SLEEP_LPMODE_S_DISABLED,
			'ENABLED':_b.KXG03_ACCEL_ODR_SLEEP_LPMODE_S_ENABLED,
		}
		self.KXG03_AUX_STATUS_AUX2ST={
			'AUX2_WAITING_DISABLE':_b.KXG03_AUX_STATUS_AUX2ST_AUX2_WAITING_DISABLE,
			'AUX2_RUNNING':_b.KXG03_AUX_STATUS_AUX2ST_AUX2_RUNNING,
			'AUX2_WAITING_ENABLE':_b.KXG03_AUX_STATUS_AUX2ST_AUX2_WAITING_ENABLE,
			'AUX2_DISABLED':_b.KXG03_AUX_STATUS_AUX2ST_AUX2_DISABLED,
		}
		self.KXG03_AUX_I2C_CTL_REG_AUX_PULL_UP={
			'DISABLED':_b.KXG03_AUX_I2C_CTL_REG_AUX_PULL_UP_DISABLED,
			'ENABLED':_b.KXG03_AUX_I2C_CTL_REG_AUX_PULL_UP_ENABLED,
		}
		self.KXG03_WAKE_SLEEP_CTL2_TH_MODE={
			'ABSOLUTE_THRESHOLD':_b.KXG03_WAKE_SLEEP_CTL2_TH_MODE_ABSOLUTE_THRESHOLD,
			'RELATIVE_THRESHOLD':_b.KXG03_WAKE_SLEEP_CTL2_TH_MODE_RELATIVE_THRESHOLD,
		}
		self.KXG03_AUX_I2C_CTL_REG_AUX_BYPASS={
			'NOT_BYPASSED':_b.KXG03_AUX_I2C_CTL_REG_AUX_BYPASS_NOT_BYPASSED,
			'BYPASSED':_b.KXG03_AUX_I2C_CTL_REG_AUX_BYPASS_BYPASSED,
		}
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W={
			'200':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_200,
			'6400':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_6400,
			'0P781':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_0P781,
			'3200':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_3200,
			'12P5':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_12P5,
			'1600':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_1600,
			'50':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_50,
			'6P25':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_6P25,
			'1P563':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_1P563,
			'3P125':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_3P125,
			'25':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_25,
			'12800':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_12800,
			'400':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_400,
			'100':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_100,
			'800':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_800,
			'51200':_b.KXG03_ACCEL_ODR_WAKE_ODRA_W_51200,
		}
		self.KXG03_CTL_REG_1_TEMP_STDBY_W={
			'DISABLED':_b.KXG03_CTL_REG_1_TEMP_STDBY_W_DISABLED,
			'ENABLED':_b.KXG03_CTL_REG_1_TEMP_STDBY_W_ENABLED,
		}
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS={
			'25':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_25,
			'0P781':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_0P781,
			'200':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_200,
			'12P5':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_12P5,
			'1600':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600,
			'50':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_50,
			'6P25':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_6P25,
			'1P563':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1P563,
			'1600_4':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600_4,
			'3P125':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_3P125,
			'400':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_400,
			'100':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_100,
			'1600_5':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600_5,
			'1600_2':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600_2,
			'1600_3':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_1600_3,
			'800':_b.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_800,
		}
		self.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S={
			'10':_b.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_10,
			'160':_b.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_160,
			'40':_b.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_40,
			'20':_b.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_20,
		}
		self.KXG03_CTL_REG_1_TEMP_STDBY_S={
			'DISABLED':_b.KXG03_CTL_REG_1_TEMP_STDBY_S_DISABLED,
			'ENABLED':_b.KXG03_CTL_REG_1_TEMP_STDBY_S_ENABLED,
		}
		self.KXG03_FSYNC_CTL_FSYNC_SEL={
			'SEL101':_b.KXG03_FSYNC_CTL_FSYNC_SEL_SEL101,
			'SEL100':_b.KXG03_FSYNC_CTL_FSYNC_SEL_SEL100,
			'SEL110':_b.KXG03_FSYNC_CTL_FSYNC_SEL_SEL110,
			'SEL111':_b.KXG03_FSYNC_CTL_FSYNC_SEL_SEL111,
			'SEL011':_b.KXG03_FSYNC_CTL_FSYNC_SEL_SEL011,
			'SEL010':_b.KXG03_FSYNC_CTL_FSYNC_SEL_SEL010,
			'SEL000':_b.KXG03_FSYNC_CTL_FSYNC_SEL_SEL000,
			'SEL001':_b.KXG03_FSYNC_CTL_FSYNC_SEL_SEL001,
		}
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW={
			'25':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_25,
			'0P781':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_0P781,
			'200':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_200,
			'12P5':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_12P5,
			'1600':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600,
			'50':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_50,
			'6P25':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_6P25,
			'1P563':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1P563,
			'1600_4':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600_4,
			'3P125':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_3P125,
			'400':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_400,
			'100':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_100,
			'1600_5':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600_5,
			'1600_2':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600_2,
			'1600_3':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_1600_3,
			'800':_b.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_800,
		}
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S={
			'4_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_SLEEP_NAVG_S_4_SAMPLE_AVG,
			'16_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_SLEEP_NAVG_S_16_SAMPLE_AVG,
			'8_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_SLEEP_NAVG_S_8_SAMPLE_AVG,
			'NO_AVG':_b.KXG03_ACCEL_ODR_SLEEP_NAVG_S_NO_AVG,
			'128_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_SLEEP_NAVG_S_128_SAMPLE_AVG,
			'2_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_SLEEP_NAVG_S_2_SAMPLE_AVG,
			'64_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_SLEEP_NAVG_S_64_SAMPLE_AVG,
			'32_SAMPLE_AVG':_b.KXG03_ACCEL_ODR_SLEEP_NAVG_S_32_SAMPLE_AVG,
		}
		self.KXG03_ACCEL_ODR_WAKE_LPMODE_W={
			'DISABLED':_b.KXG03_ACCEL_ODR_WAKE_LPMODE_W_DISABLED,
			'ENABLED':_b.KXG03_ACCEL_ODR_WAKE_LPMODE_W_ENABLED,
		}
		self.KXG03_STATUS1_WAKE_SLEEP={
			'SLEEP_MODE':_b.KXG03_STATUS1_WAKE_SLEEP_SLEEP_MODE,
			'WAKE_MODE':_b.KXG03_STATUS1_WAKE_SLEEP_WAKE_MODE,
		}
		self.KXG03_BUF_EN_BUF_SYM={
			'DUAL_SYMBOL_TRANS_MODE_ENABLED':_b.KXG03_BUF_EN_BUF_SYM_DUAL_SYMBOL_TRANS_MODE_ENABLED,
			'SINGLE_SYMBOL_MODE_ENABLED':_b.KXG03_BUF_EN_BUF_SYM_SINGLE_SYMBOL_MODE_ENABLED,
			'SYMBOL_MODE_DISABLED':_b.KXG03_BUF_EN_BUF_SYM_SYMBOL_MODE_DISABLED,
			'DUAL_SYMBOL_FRAME_MODE_ENABLED':_b.KXG03_BUF_EN_BUF_SYM_DUAL_SYMBOL_FRAME_MODE_ENABLED,
		}
class masks(register_base):
	def __init__(self):
		self.KXG03_AUX_STATUS_AUX2ST_MASK                         = 0x30         
		self.KXG03_AUX_STATUS_AUX1ST_MASK                         = 0x03         
		self.KXG03_WHO_AM_I_WIA_MASK                              = 0xFF         
		self.KXG03_STATUS1_WAKE_SLEEP_MASK                        = 0x04         
		self.KXG03_STATUS2_WAKE_SLEEP_MASK                        = 0x04         
		self.KXG03_ACCEL_ODR_WAKE_LPMODE_W_MASK                   = 0x80         
		self.KXG03_ACCEL_ODR_WAKE_NAVG_W_MASK                     = 0x70         # The max over sampling rate (or max number of samples averaged) varies with ODR
		self.KXG03_ACCEL_ODR_WAKE_ODRA_W_MASK                     = 0x0F         # accelerometer ODR in wake mode
		self.KXG03_ACCEL_ODR_SLEEP_LPMODE_S_MASK                  = 0x80         
		self.KXG03_ACCEL_ODR_SLEEP_NAVG_S_MASK                    = 0x70         
		self.KXG03_ACCEL_ODR_SLEEP_ODRA_S_MASK                    = 0x0F         
		self.KXG03_ACCEL_CTL_ACC_FS_S_MASK                        = 0xC0         # Accelerometer sleep mode full scale range select.
		self.KXG03_ACCEL_CTL_ACC_FS_W_MASK                        = 0x0C         # Accelerometer wake mode full scale range select.
		self.KXG03_GYRO_ODR_WAKE_GYRO_FS_W_MASK                   = 0xC0         # Gyroscope angular velocity range wake mode
		self.KXG03_GYRO_ODR_WAKE_GYRO_BW_W_MASK                   = 0x30         # Gyroscope bandwidth selection in wake mode.
		self.KXG03_GYRO_ODR_WAKE_ODRG_W_MASK                      = 0x0F         # gyroscope ODR in wake mode
		self.KXG03_GYRO_ODR_SLEEP_GYRO_FS_S_MASK                  = 0xC0         # Gyroscope angular velocity range sleep mode
		self.KXG03_GYRO_ODR_SLEEP_GYRO_BW_S_MASK                  = 0x30         # Gyroscope bandwidth selection in sleep mode.
		self.KXG03_GYRO_ODR_SLEEP_ODRG_S_MASK                     = 0x0F         # gyroscope ODR in sleep mode
		self.KXG03_STDBY_AUX2_STDBY_S_MASK                        = 0x80         
		self.KXG03_STDBY_AUX1_STDBY_S_MASK                        = 0x40         
		self.KXG03_STDBY_GYRO_STDBY_S_MASK                        = 0x20         
		self.KXG03_STDBY_AUX2_STDBY_W_MASK                        = 0x08         
		self.KXG03_STDBY_AUX1_STDBY_W_MASK                        = 0x04         
		self.KXG03_STDBY_GYRO_STDBY_W_MASK                        = 0x02         
		self.KXG03_STDBY_ACC_STDBY_MASK                           = 0x01         
		self.KXG03_CTL_REG_1_I2C_DIS_MASK                         = 0x20         # Active high I2C disable bit
		self.KXG03_CTL_REG_1_TEMP_STDBY_S_MASK                    = 0x10         
		self.KXG03_CTL_REG_1_TEMP_STDBY_W_MASK                    = 0x08         
		self.KXG03_CTL_REG_1_ACC_STPOL_MASK                       = 0x02         
		self.KXG03_INT_PIN_CTL_IEA2_MASK                          = 0x40         # Interrupt polarity select for INT2 pin.
		self.KXG03_INT_PIN_CTL_IEL2_MASK                          = 0x30         # Interrupt latch mode select for INT2 pin
		self.KXG03_INT_PIN_CTL_IEA1_MASK                          = 0x04         # Interrupt polarity select for INT1 pin.
		self.KXG03_INT_PIN_CTL_IEL1_MASK                          = 0x03         # Interrupt latch mode select for INT1 pin
		self.KXG03_FSYNC_CTL_FSYNC_MODE_MASK                      = 0x30         
		self.KXG03_FSYNC_CTL_FSYNC_SEL_MASK                       = 0x07         
		self.KXG03_WAKE_SLEEP_CTL1_OWUF_MASK                      = 0x07         # the Output Data Rate for the wake up (motion detection).
		self.KXG03_WAKE_SLEEP_CTL2_TH_MODE_MASK                   = 0x02         
		self.KXG03_WAKE_SLEEP_CTL2_C_MODE_MASK                    = 0x01         # debounce counter clear mode.
		self.KXG03_AUX_I2C_CTL_REG_AUX_BUS_SPD_MASK               = 0x08         # Sets I2C bus speed.
		self.KXG03_AUX_I2C_CTL_REG_AUX_PULL_UP_MASK               = 0x04         # Active high pull up enable.
		self.KXG03_AUX_I2C_CTL_REG_AUX_BYPASS_MASK                = 0x02         # Active high bypass enable
		self.KXG03_AUX_I2C_ODR1_W_AUX1_D_MASK                     = 0x70         # Number of bytes read back via Auxiliary I2C bus from device 1
		self.KXG03_AUX_I2C_ODR1_W_AUX1ODRW_MASK                   = 0x0F         # Determines rate at which aux1 output is polled by ASIC in aux1 wake state
		self.KXG03_AUX_I2C_ODR1_S_AUX1ODRS_MASK                   = 0x0F         # Determines rate at which aux1 output is polled by ASIC in aux1 sleep
		self.KXG03_AUX_I2C_ODR2_W_AUX2_D_MASK                     = 0x70         # Number of bytes read back via Auxiliary I2C bus from device 2
		self.KXG03_AUX_I2C_ODR2_W_AUX2ODRW_MASK                   = 0x0F         # Determines rate at which aux2 output is polled by ASIC in aux2 wake state
		self.KXG03_AUX_I2C_ODR1_S_AUX2ODRS_MASK                   = 0x0F         # Determines rate at which aux2 output is polled by ASIC in aux2 sleep
		self.KXG03_BUF_EN_BUF_SYM_MASK                            = 0x0C         # Symbol mode select.
		self.KXG03_BUF_EN_BUF_M_MASK                              = 0x03         # selects the operating mode of the sample buffer