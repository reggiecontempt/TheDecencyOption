import hashlib, sys, os
def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(sha256(p), p)
