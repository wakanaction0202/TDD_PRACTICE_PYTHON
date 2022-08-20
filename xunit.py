class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result

class TestResult:
    def __init__(self):
        self.runCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def summary(self):
        return "%d run, 0 failed" % self.runCount

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "
    def testMethod(self):
        self.log = self.log + "testMethod "
    def tearDown(self):
        self.log = self.log + "tearDown "

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testTemplateMethod(self):
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()


# [x]テストメソッドを呼び出す
# [x]setUpを最初に呼び出す
# [ ]tearDownを後で呼び出す
# [ ]テストメソッドが失敗したとしてもtearDown()を呼び出す
# [ ]複数のテストを走らせる
# [ ]収集してテスト結果を出力する
# [x]wasRunでは文字列をログに記録する