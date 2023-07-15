
import os
import os.path
import sys
import struct
import argparse

from util import check_challenge

from crand import rand, srand
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad  # pkcs7 is standard


def byte_rand(numbytes):
    calls = (numbytes + 3) // 4
    randbytes = b''
    for i in range(calls):
        r = rand()
        randbytes += struct.pack('<I', r)

    return randbytes[:numbytes]


def enc_file(fname):
    iv = byte_rand(16)
    key = byte_rand(16)

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    f = open(fname, 'rb')
    ct = cipher.encrypt(pad(f.read(), 16))
    f.close()

    with open(fname + '.enc', 'wb') as f:
        f.write(iv)
        f.write(ct)

    with open(fname + '.key', 'wb') as f:
        f.write(key)


def dec_file(fname):
    with open(fname + '.key', 'rb') as f:
        key = f.read()

    with open(fname + '.enc', 'rb') as f:
        iv = f.read(16)
        ct = f.read()

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)

    try:
        pt = unpad(cipher.decrypt(ct), AES.block_size, style='pkcs7')
    except ValueError:
        print(fname + ': decryption failed, invalid padding')

    with open(fname, 'wb') as f:
        f.write(pt)


def solve_challenge(fname):
    with open(fname + '.enc', 'rb') as f:
        iv = f.read(16)
        ct = f.read()

    key = bytes(16)

    a=iv[12:16]
    b=struct.unpack('<I',a)
    c=[i for i in b]
    d=c[0]
    srand(d)
    key=byte_rand(16)
    #fname=fname+'_solution'


    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    try:
        pt = unpad(cipher.decrypt(ct), AES.block_size, style='pkcs7')
    except ValueError:
        print(fname + ': decryption failed, invalid padding')
        return

    with open(fname, 'wb') as f:
        f.write(pt)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', title='command')
    subparsers.required = True
    parser_e = subparsers.add_parser('e', help='encrypt')
    parser_e.add_argument('file', nargs='+')
    parser_d = subparsers.add_parser('d', help='decrypt')
    parser_d.add_argument('file', nargs='+')
    parser_c = subparsers.add_parser('c', help='challenge')
    parser_c.add_argument(
        'file',
        nargs='*',
        default=['challenge.enc'],
        help='default: challenge.enc')
    args = parser.parse_args()

    files = [
        t for t in args.file if (
            os.path.isfile(t) and not t.endswith('.key'))]

    rng_seed = struct.unpack('<I', os.urandom(4))[0]
    srand(rng_seed)

    if args.command == 'e':
        # we don't encrypt already encrypted files
        files = [t for t in files if not t.endswith('.enc')]
        if len(files) == 0:
            print('No valid files selected')
            return

        for f in files:
            enc_file(f)

        return

    if args.command == 'd':
        # we only want encrypted files
        files = [t[:-4] for t in files if t.endswith('.enc')]
        if len(files) == 0:
            print('No valid files selected')
            return

        for f in files:
            dec_file(f)

        return

    # challenge: decrypt without having the key
    if args.command == 'c':
        # we only want encrypted files
        files = [t[:-4] for t in files if t.endswith('.enc')]
        if len(files) == 0:
            print('No valid files selected')
            return

        for f in files:
            solve_challenge(f)
            check_challenge(f)

        return


if __name__ == "__main__":
    sys.exit(main())
