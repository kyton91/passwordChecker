import requests
import hashlib
import sys


def request_api_data(query_string):
    api = "https://api.pwnedpasswords.com/range/" + query_string
    res=requests.get(api)
    if res.status_code!=200:
        raise RuntimeError(f"Error:{res.status_code} check query and try again")
    return res


def check_password(password):
    hashed_string=hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5_char,tail=hashed_string[:5],hashed_string[5:]
    response=request_api_data(first_5_char)
    return get_passwords_leak_count(response.text,tail)


def get_passwords_leak_count(hashes, hash_to_check):
    hashes_list=(line.split(":") for line in hashes.splitlines())
    for hsh,count in hashes_list:
        if hsh==hash_to_check:
            return count
    return '0'


def main(args):
    for password in args:
        count=check_password(password)
        if int(count)>0:
            print(f"{password} has been leaked {count} times you should change it\n")
        else:
            print(f"{password} has not been leaked yet\n")
    return None


sys.exit(main(sys.argv[1:]))
