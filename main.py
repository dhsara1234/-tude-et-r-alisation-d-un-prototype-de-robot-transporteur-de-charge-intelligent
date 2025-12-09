import numpy as np
from keras.models import load_model

from Modules.MotorModule import Motor
import NeuralNetwork.RunMain as r
import Modules.WebcamModule as wM
import Modules.KeyboardModule as kp
import Modules.LaneDetectionModule as ld
import cv2

###################################
motor = Motor(2, 3, 4, 17, 22)
###################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
model = load_model('model.h5')
cap = cv2.VideoCapture(0)
kp.init()
frameCounter = 0


def main():
    global frameCounter
    # if kp.getKey('UP'):
    #     motor.move(0.6, 0, 0.1)
    # elif kp.getKey('DOWN'):
    #     motor.move(-0.6, 0, 0.1)
    # elif kp.getKey('LEFT'):
    #     motor.move(0.5, 0.3, 0.1)
    # elif kp.getKey('RIGHT'):
    #     motor.move(0.5, -0.3, 0.1)
    # else:
    #     motor.stop(0.1)
    #
    # if kp.getKey('z'):
    #     motor.move(0.6, 0, 0.1)
    # elif kp.getKey('socket'):
    #     motor.move(-0.6, 0, 0.1)
    # elif kp.getKey('q'):
    #     motor.move(0.5, 0.3, 0.1)
    # elif kp.getKey('d'):
    #     motor.move(0.5, -0.3, 0.1)
    # else:
    #     motor.stop(0.1)

    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0
    success, img = cap.read()
    img = cv2.resize(img, (480, 240))
    curve = ld.getLaneCurve(img, display=2)
    img = wM.getImg(True, size=[240, 120])
    img = np.asarray(img)
    img = r.preProcess(img)
    img = np.array([img])
    steering = float(model.predict(img))
    p = steering * steeringSen
    print(curve)

    if p < 0:
        motor.left(p)
    elif p > 0:
        motor.right(p)
    else:
        motor.forward(p)

    if curve > 0:
        motor.right(curve)
    elif curve < 0:
        motor.left(curve)
    else:
        motor.forward(curve)

    cv2.waitKey(1)


if __name__ == "__main__":
    while True:
        main()
