import requests


class ApiService():
    url = "http://192.168.50.99:4000/detect"

    def upladImage(self, path, yolotype):
        try:
            payload = {'detect': yolotype,
                       'token': 'test',
                       'yolodata': 'True'}
            files = [
                ('file', ('1.jpg', open(path, 'rb'), 'image/jpeg'))
            ]
            headers = {}
            response = requests.request(
                "POST", self.url, headers=headers, data=payload, files=files)

            # print(response.text)
            if response.status_code != 200:
                return ""
            return response.text
        except:
            return ""
