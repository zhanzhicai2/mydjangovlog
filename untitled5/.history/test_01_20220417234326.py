class Test(object):
    """docstring for Test"""
    count = 1
    def __init__(self, age=None):
        super(Test, self).__init__()
        self.arg = age
    def say_hi(self):
        print(self.age)
        print("hello wrold")
    @staticmethod
    def say_bad():
        print("say bad")
    @classmethod
    def say_good(cls):
        # print(cls.arg)
        print("say good")
def main():
    test = Test(11)
    test.say_hi()
    Test.say_bad() 
    Test.say_good()
    print(Test.count)

if __name__ == '__main__':

    main()

    # magnet:?xt=urn:btih:c7c5d382606f01625b16fcc6ac168561b4ad3c3d