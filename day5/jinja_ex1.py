#!/usr/bin/env python
from __future__ import print_function
import jinja2

template_file = 'juniper_bgp.j2'
with open(template_file) as f:
    bgp_template = f.read()

my_vars = {
    'peer_as' : 22,
    'neighbor1' : '10.100.99.1',
    'neighbor2' : '10.100.83.1',
    'neighbor3' : '10.100.8.1',
}

template = jinja2.Template(bgp_template)
print(template.render(my_vars))

