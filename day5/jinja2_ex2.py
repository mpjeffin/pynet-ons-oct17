#!/usr/bin/env python
from __future__ import print_function
import jinja2

my_vars = { 'intf_list': [
    ('ge-0/0/0', '10.10.10.1/24'),
    ('ge-0/0/1', '10.10.11.1/24'),
    ('ge-0/0/2', '10.10.12.1/24'),
    ('ge-0/0/3', '10.10.13.1/24')
] }

interface_template = """
interfaces {
{%- for intf, ip_addr in intf_list %}
    {{ intf }} {
        unit 0 {
            replace:
            family inet {
                address {{ ip_addr }};
            }
        }
    }
{%- endfor %}
}
"""

template = jinja2.Template(interface_template)
print(template.render(my_vars))
