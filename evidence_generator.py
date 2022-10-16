from dotenv import load_dotenv
import os
import replicate
import numpy as np
import requests
import cv2
from dotenv import load_dotenv
import os
import base64

load_dotenv()

class EvidenceGenerator:

    def __init__(self):
        self.REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
    
    def acquire_evidence(self, theme):
        model = replicate.models.get("stability-ai/stable-diffusion")
        url = model.predict(prompt=theme)[0]
        # api call get image
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            data={
                'image_url': 'https://media.istockphoto.com/photos/close-up-young-smiling-man-in-casual-clothes-posing-isolated-on-blue-picture-id1270987867?k=20&m=1270987867&s=612x612&w=0&h=lX9Y1qUxtWOa0W0Mc-SvNta00UH0-sgJQItkxfwE4uU=',
                'size': 'auto'
            },
            headers={'X-Api-Key': 'rPdNmWA3gtAKbDXiTz5qEqjT'},
        )
        if response.status_code == requests.codes.ok:
            with open('nobg.png', 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)

        # read foreground image from api call
        img = cv2.resize(cv2.imread('nobg.png', cv2.IMREAD_UNCHANGED), (500, 500))

        resp = requests.get(url, stream=True).raw
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        back = cv2.resize(image, (500, 500))

        # read background image
        # back = cv2.resize(cv2.imread('background.png'), (500, 500))

        # get alpha channel
        alpha = img[:,:,3]
        alpha = cv2.merge([alpha,alpha,alpha])

        # extract bgr channels from foreground image
        front = img[:,:,0:3]

        # blend the two images using the alpha channel as controlling mask
        result = np.where(alpha==(0,0,0), back, front)

        _, buffer = cv2.imencode('.jpg', result)
        im_bytes = buffer.tobytes()

        jpg_as_text = base64.b64encode(im_bytes)
        
        return jpg_as_text
        # # save result
        # cv2.imwrite("front_back.png", result)

        # # show result
        # cv2.imshow("RESULT", result)
        # cv2.waitKey(0)



