from faker import Faker


def gen_address():
    fake = Faker()
    print(fake.address() + "\n")
    print(fake.text() + "\n")


def gen_name():
    """
    生成名字
    国家it_IT、en_US、ja_JP
    """
    fake = Faker(['it_IT', 'en_US', 'ja_JP'])
    print(fake.name() + "\n")
    print(fake.text() + "\n")


gen_address()

gen_name()
