"""Parsing bgp output getting prefix and as_path."""
from __future__ import print_function

def main():
    filename = "show_ip_bgp.txt"
    f = open(filename)

    show_bgp = f.read()

    fields = show_bgp.split("Weight Path")
    bgp_table = fields[1]
    bgp_table = bgp_table.strip()

    for line in bgp_table.splitlines():
        line = line.strip()
        fields = line.split()
        prefix = fields[1]
        as_path = fields[5:-1]
        print("Prefix: {}, AS_Path: {}".format(prefix, as_path))


if __name__ == "__main__":
    main()
