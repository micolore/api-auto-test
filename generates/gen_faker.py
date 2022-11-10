from faker import Faker


def gen_address():
    """
    生成地址
    国家it_IT、en_US、ja_JP
    """
    fake = Faker()
    return fake.address()


def gen_name():
    """
    生成名字
    国家it_IT、en_US、ja_JP
    """
    fake = Faker(['it_IT', 'en_US', 'ja_JP'])
    return fake.name()
