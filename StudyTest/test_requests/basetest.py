"""
============================
Author:yuquanyong(yqy)
Time:2022/12/15
E-mail:yuqy1205@163.com
============================
"""
# import requests
# import json
# import time
# import hmac
# import uuid
# import base64
# from hashlib import sha256
#
# # 调用方生成的签名值，生成方式是X-Client-Id+X-Timestamp+X-Nonce组合字符，使用HmacSHA256算法计算并经Base64编码后的字符串，密钥为签名认证令牌密钥
# def getSignature(XClientId, X_Signature):
#     XClientId = XClientId.encode('utf-8')
#     X_Signature = X_Signature.encode('utf-8')
#     signature = base64.b64encode(hmac.new(XClientId, X_Signature, digestmod=sha256).digest())
#     signature = str(signature, 'utf-8')
#     return signature
# if __name__ == '__main__':
#     # 'Client ID' : '************'
#     # Client Secret: '************'
#     # AppKey '************'
#     timestramp = str(round(time.time() * 1000))
#     XClientId = '************'
#     X_Nonce = str(uuid.uuid1())
#     X_Signature = XClientId + timestramp + X_Nonce
#     signature = getSignature(XClientId,X_Signature)
#     print(signature)


# signature = base64.b64encode(hmac.new(XClientId.encode('utf-8'), X_Signature.encode('utf-8'), digestmod=sha256).digest())
# print(str(signature, 'utf-8')

from hashlib import sha256
import hmac, base64

def get_sha256(data, key):
    key = key.encode('utf-8')       # sha256加密的key
    message = data.encode('utf-8')  # 待sha256加密的内容
    sign = base64.b64encode(hmac.new(key, message, digestmod=sha256).digest()).decode()
    return sign

if __name__ == '__main__':
    key = 'HappyNewYear123456'
    data_str = '一段测试的字符串,祝你新年快乐哦!'
    sign = get_sha256(data_str, key)
    print(sign)

