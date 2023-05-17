import random
import string
from reuseablefunctions.reporting import Reporting


class randomTextGenerator:

    def __init__(self):
        self.text = None

    objReporting = Reporting()

    def randomString(self,length):
        try:
            N = length
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            self.text=str(res)+"@gmail.com"
            return self.text
        except Exception as e:
            raise Exception(e)