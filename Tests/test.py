class Test:
    def assertEqual(self, expected, actual, testName = 'test'):
        self.assertCondition(expected == actual, testName)

    def assertNone(self, element, testName = 'test'):
        self.assertCondition(element is None, testName)

    def assertCondition(self, condition, testName):
        message = testName + ' --- '
        message += 'OK' if condition else 'FAILED'
        print(message)
