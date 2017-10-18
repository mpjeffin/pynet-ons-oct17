# content of test_sample.py
import pytest
from getpass import getpass
from netmiko import ConnectHandler

@pytest.fixture(scope="module")
def netmiko_connect():
    """Establish a netmiko connection."""
    cisco1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password': getpass()
    }
    return ConnectHandler(**cisco1)
