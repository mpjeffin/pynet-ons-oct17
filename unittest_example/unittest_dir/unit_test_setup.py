import unittest
from netmiko import ConnectHandler

class TestNetDevice(unittest.TestCase):
    def SetUp(self):
        cisco1 = {
            'device_type': 'cisco_ios',
            'ip':   '184.105.247.70',
            'username': 'pyclass',
            'password': getpass()
        }
        self.net_connect = ConnectHandler(**cisco1)

    def test_prompt(self):
        print(self.net_connect.find_prompt())
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
