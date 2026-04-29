import unittest
from myDict import Dict

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertEqual(isinstance(d,Dict),True)
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual('key' in d,True)
        self.assertEqual(d['key'], 'value')
    def test_key_error(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_value_error(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
