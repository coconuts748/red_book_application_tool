import hashlib
import json


def creat_txt(txt_content,file_name):
    with open(f'{file_name}.txt','a',encoding='utf-8') as f:
        f.write(txt_content)

def creat_json(json_content,file_name):
    with open(f'{file_name}.json','wb') as f:
        f.write(json.dumps(str(json_content)).encode('utf-8'))

def creat_json_for_build_param(json_content,file_name):
    with open(f'{file_name}.json','wb') as f:
        f.write(json.dumps(str(json_content)).encode('utf-8'))


def encryption_something(encrypt_content):
    result  = hashlib.sha256(encrypt_content.encode('utf-8')).hexdigest()
    return result



