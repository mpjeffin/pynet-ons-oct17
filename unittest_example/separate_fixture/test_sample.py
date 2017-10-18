
def test_prompt(netmiko_connect):
    print(netmiko_connect.find_prompt())
    assert netmiko_connect.find_prompt() == 'pynet-rtr1#'

def test_show_version(netmiko_connect):
    output = netmiko_connect.send_command("show version")
    assert 'Configuration register is 0x2102' in output
