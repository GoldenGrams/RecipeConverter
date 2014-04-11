import unittest

class unitTestConvertElement(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_getValue(self):
        self.assertEqual((ConvertibleElement.getValue()), convertElement.initValue())
    def test_getUnit(self):
        self.assertEqual((ConvertibleElement.getUnit()), convertElement.initUnit())
    def test_getSystem(self):
        self.assertEqual(convertElement.desiredUnitsSystem(), "Metric" or "Imperial")

if __name__ == '__main__':
    unittest.main()
