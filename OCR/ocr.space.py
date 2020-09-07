import json

import cv2
import numpy as np
import requests
import io

img = cv2.imread("chinese.png")
height, width, _ = (img.shape)
print(img)
# Cutting image
# roi = img[0: height, 0: width]
roi = img
# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)
result = requests.post(url_api, files={"text.png": file_bytes},
                       data={"apikey": '1f4f70193688957',
                             "language": "chs"})

result = result.content.decode()
result = json.loads(result)

text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)

cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
