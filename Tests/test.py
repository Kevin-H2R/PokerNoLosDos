import inspect

class Test:
    def assertEqual(self, expected, actual):
        self.assertCondition(expected == actual)

    def assertNone(self, element):
        self.assertCondition(element is None)

    def assertNotIn(self, element, array):
        self.assertCondition(element not in array)

    def assertCondition(self, condition):
        message = inspect.stack()[2][3] + ' --- '
        message += 'OK' if condition else 'FAILED'
        print(message)
