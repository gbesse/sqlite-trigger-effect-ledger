import unittest
from sqlite_trigger_effect_ledger.core import run
class DomainTests(unittest.TestCase):
 def test_indirect_and_rollback(self):
  x=run({'rows':[{'id':1,'qty':5}],'updates':[{'id':1,'qty':4},{'id':1,'qty':-1}]});self.assertTrue(x['rolled_back']);self.assertEqual(x['stock'],[(1,5)]);self.assertEqual(x['audit'],[]);self.assertEqual(x['attempted_change_counter'],2)
 def test_success(self):
  x=run({'rows':[{'id':1,'qty':5}],'updates':[{'id':1,'qty':4}]});self.assertEqual(x['events'][0]['total_change_delta'],2);self.assertEqual(x['audit'],[(1,5,4)])
 def test_missing(self):
  x=run({'rows':[],'updates':[{'id':1,'qty':0}]});self.assertEqual(x['events'][0]['direct_rows'],0)
