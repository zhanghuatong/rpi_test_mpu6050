import lib_mpu6050 as lib
import time

if __name__ == "__main__":
    mpu = lib.mpu6050(0x68)
    time.sleep(0.5)
    #print(mpu.get_temp())
    while True:
        data=mpu.get_accel_data(True)
        print("ACCEL X=%7.2f , Y=%7.2f , Z=%7.2f" %(data['x'],data['y'],data['z']), end="\r")
        time.sleep(0.02)
"""
    accel_data = mpu.get_accel_data()
    print(accel_data['x'])
    print(accel_data['y'])
    print(accel_data['z'])
    gyro_data = mpu.get_gyro_data()
    print(gyro_data['x'])
    print(gyro_data['y'])
    print(gyro_data['z'])
"""