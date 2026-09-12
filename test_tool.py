import unittest
from tool import plan
class BatchTests(unittest.TestCase):
 def test_capacity(self):self.assertEqual(plan([3,3,5,2],2,6),[[0,1],[2],[3]])
 def test_oversize(self):
  with self.assertRaises(ValueError):plan([7],2,6)
if __name__=='__main__':unittest.main()
