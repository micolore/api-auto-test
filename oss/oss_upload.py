from itertools import islice

import oss2


def create_bucket():
    auth = oss2.Auth('', '')
    bucket = oss2.Bucket(auth, 'oss-cn-shanghai.aliyuncs.com', 'one-return')
    bucket.create_bucket(oss2.models.BUCKET_ACL_PRIVATE)


def list_files():
    auth = oss2.Auth('', '')
    bucket = oss2.Bucket(auth, 'oss-cn-shanghai.aliyuncs.com', '')
    for b in islice(oss2.ObjectIterator(bucket), 10):
        print(b.key)


list_files()
