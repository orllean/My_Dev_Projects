import urllib
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:  # Exception as err:
    print('deu ruim')
else:
    print('deu bom')
