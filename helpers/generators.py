import random
import string


def mail_generator(max_len: int = 15, dom: str = "gm.com"):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for _ in range(random.randrange(1, max_len))]) + "@" + dom


def password_generator(min_len=8, max_len=30):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    symbols = string.punctuation
    num = string.digits
    all = lower + upper + symbols + num
    password = "".join([random.choice(all) for _ in range(random.randrange(min_len, max_len))])
    return password


def gen_date_of_birth(number=1):
    def dob():
        for item in range(number):
            yield random.randrange(1900, 2006), random.randrange(1, 12), random.randrange(1, 31)

    for year, month, date in dob():
        m = list()
        year_ = str(year)
        month_ = str(month)
        date_ = str(date)
        m.append(year_)
        m.append(month_)
        m.append(date_)
    return m


print(gen_date_of_birth()[0])
print(gen_date_of_birth()[1])
print(gen_date_of_birth()[2])
