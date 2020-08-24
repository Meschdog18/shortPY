import random, string

class Tools():
    def genID(self):
        return ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for _ in range(7))