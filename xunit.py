from time import thread_time_ns


class TestCase:
    def __init__(self, name) :
        self.name = name
    def run(self) :
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name) :
        self.wasRun = None
        super().__init__(name)

    def testMethod(self) :
        self.wasRun = 1

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

TestCaseTest("testRunning").run()

# [x]テストメソッドを呼び出す
# [ ]setUpを最初に呼び出す
# [ ]tearDownを後で呼び出す
# [ ]テストメソッドが失敗したとしてもtearDown()を呼び出す
# [ ]複数のテストを走らせる
# [ ]収集してテスト結果を出力する