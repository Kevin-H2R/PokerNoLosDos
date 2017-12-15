import inspect

class Test:

    def __init__(self):
        hasFailed = False

    def assertEqual(self, expected, actual):
        return self.assertCondition(expected == actual)

    def assertNone(self, element):
        return self.assertCondition(element is None)

    def assertNotIn(self, element, array):
        return self.assertCondition(element not in array)

    def assertCondition(self, condition):
        message = inspect.stack()[2][3] + ' --- '
        hasFailed = False
        responseMessage = 'OK'
        if not (condition):
            responseMessage = 'FAILED'
            hasFailed = True

        message += responseMessage
        print(message)
        self.hasFailed = hasFailed
