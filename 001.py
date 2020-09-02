import requests

class HTTP_Res:

    def http_res(self, url, data, method, cookies=None):

        if method.lower() == 'get':
            res = requests.get(url=url, data=data)
            res.encoding = res.apparent_encoding
            a = res.text.encode().decode("unicode_escape")
        else:
            res = requests.post(url=url, data=data)
            res.encoding = res.apparent_encoding
            a = res.text.encode().decode("unicode_escape")
        return a


url = 'http://localhost/action/login.php?action=login'
data = {'username': '138493948755',
        'password': '123456'}

a = HTTP_Res().http_res(url, data, 'post')
print(a, type(a))



