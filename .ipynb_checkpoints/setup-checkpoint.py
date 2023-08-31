import hmac
import hashlib

def hashdice(secret_key, message):
    hmac_sha512 = hmac.new(key=secret_key.encode(), msg=message.encode(), digestmod=hashlib.sha512).hexdigest()
    lucky = int(hmac_sha512[0:5], 16)
    return lucky % 100000

def main():
    x = open('hashdice.txt','w')

    for i in range(4000000):
        secret_key = '4671f003b18db91be8f1570c7f681ad9e97026c5f34d89a733f48ab81eb8d592'
        message = f'5533idsczGPRYacG5N15jfJ6nm5:{i}'
        result = hashdice(secret_key, message)
        rs = strs(result)
        _ = x.write(f'{rs + str(i%10000)}\n')


if __name__ == '__main__':
    main()