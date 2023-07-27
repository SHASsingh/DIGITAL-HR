from urllib.parse import urlencode
from urllib.request import urlopen,Request

user="BRIJESH"
key="066c862acdXX"
senderid="SOFTEC"
accusage="1"
def sendsms(mobile,message):
    values={
        'user':user,
        'key':key,
        'mobile':mobile,
        'message':message,
        'senderid':senderid,
        'accusage':accusage
    }
    url="https://smsbulkssms.com/submitsms.jsp"
    postdata=urlencode(values).encode("utf-8")
    req=Request(url,postdata)
    response=urlopen(req)
    response.read()