class Test(object):
    """docstring for Test"""
    def __init__(self, arg=None):
        super(Test, self).__init__()
        self.arg = arg
    def say_hi(self):
        print("hello wrold")
    @staticmethod
    def say_bad(sls):
        print("say bad")
    @classmethod
    def say_good(cls):
        print("say good")
def main():
    # test = Test()
    # test.say_hi()
    Test.say_bad() 
    Test.say_good()

if __name__ == '__main__':

    main()