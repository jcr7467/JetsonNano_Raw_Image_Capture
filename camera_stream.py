import io
import numpy as np
from subprocess import check_output
import cv2

cmd = "v4l2-ctl --device /dev/video0 --stream-mmap --stream-to=- --stream-count=1"

stream = io.BytesIO()
stream.write(check_output(cmd,shell=True))

data = stream.getvalue()

print('data type: ' + str(type(data)))
print('data length: ' + str(len(data)))

data = np.fromstring(data,dtype=np.uint16)

print('data np array shape: ' + str(data.shape))
print('number of nonzero pixels: ' + str(np.count_nonzero(data)))



cv2.imshow('testImage', np.reshape(data, [2464, 3264]))

cv2.waitKey(0)

np.save('raw_img_array.npy',data)
