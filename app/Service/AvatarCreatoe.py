import random


def AvatarCreator():
    number = random.randint(1,25)
    return f'/assets/images/avatars/avatar_{number}.jpg'


