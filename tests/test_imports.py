import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestImports(unittest.TestCase):
    def test_grpc_import(self):
        import grpc
        self.assertTrue(True)
    
    def test_protobuf_import(self):
        from src.client import nexus_bus_pb2
        self.assertIsNotNone(nexus_bus_pb2)

if __name__ == "__main__":
    unittest.main()
