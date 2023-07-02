LEN_NAME = 150
LEN_EMAIL = 254
LEN_PASSWORD = 150


def len_role(roles):
    words = [max(k, v, key=len) for k, v in roles]
    chars = [len(word) for word in words]
    return (max(chars))
