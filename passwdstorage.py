#!/usr/bin/env python3

from base64 import b64encode
from os import urandom
from simplecrypt import encrypt, decrypt

import getpass
import os
import sys


HOME = os.path.expanduser("~")
PASSWD_FOLDER = HOME + '/.dot-files/.passwds/'


def generate_passwd(digit=8):
    random_bytes = urandom(digit)
    return b64encode(random_bytes).decode('utf-8')


def set_passwd(platform, pass_len=8, plaintext=None):
    if plaintext is None:
        token = generate_passwd(pass_len)
    else:
        token = plaintext

    platform = PASSWD_FOLDER + platform
    passwd = getpass.getpass('Password: ')
    re_passwd = getpass.getpass('Re password: ')
    if passwd != re_passwd:
        print('Wrong password!')
        return
    else:
        ciphertext = encrypt(passwd, token)

    if plaintext:
        plaintext = plaintext

    path = platform.split('/')
    root = '/'.join(path[:-1])
    if not os.path.isdir(root):
        os.makedirs(root)

    with open(platform, 'wb') as f:
        f.write(ciphertext)


def get_passwd(platform):
    platform = PASSWD_FOLDER + platform
    f = open(platform, 'rb')
    data = f.read()
    passwd = getpass.getpass('Passwd: ')
    plaintext = decrypt(passwd, data)
    plaintext = plaintext.decode('utf-8')

    if sys.platform == 'linux2':
        os.system("printf '%s' | xclip -sel clip" % plaintext)
    else:
        os.system("printf '%s' | pbcopy" % plaintext)


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1 or args[1] == 'help':
        print('Set password:')
        print(' python passwordstorage.py set new_password\n')
        print('Retrieve saved password:')
        print(' python passwordstorage.py new_password\n')
        print('Encrypt plain text:')
        print(' python passwordstorage.py set password_name')
        print(' Passwd: ')
        pass
    elif args[1] == 'set':
        pass_len = 12
        if len(args) > 3 and args[3].isdigit():
            pass_len = int(args[3])
        set_passwd(args[2], pass_len)
    elif args[1] == 'setpasswd':
        plaintext = getpass.getpass('Text: ')
        set_passwd(args[2], plaintext=plaintext)
    else:
        get_passwd(args[1])
