class Test(object):
    """docstring for Test"""
    count = 1
    def __init__(self, age=100):
        super(Test, self).__init__()
        self.age = age
    def say_hi(self):
        # print(self.age)
        self.age=self.age+1
        print(self.age)
        print("hello wrold")
    @staticmethod
    def say_bad():
        print(Test.count)
        print("say bad")
    @classmethod
    def say_good(cls,count):
        cls.count =count
        print(cls.count)
        print("say good")
    @classmethod
    def get_count(cls,age):
        return Test.age
def main():
    test = Test(11)
    test.say_hi()
    test.say_bad()
    Test.say_good(13)
    print(Test.count)
    # get_count =Test.get_count(100)
    print(Test.get_count(100))

if __name__ == '__main__':

    main()

# magnet:?xt=urn:btih:c7c5d382606f01625b16fcc6ac168561b4ad3c3d