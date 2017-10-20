from __future__ import print_function
import csv
import jinja2

def main():
    template_file = 'juniper_bgp.j2'
    with open(template_file) as f:
        bgp_template = f.read()
    template = jinja2.Template(bgp_template)

    file_name = 'csv_ex1.csv'
    with open(file_name) as f:
        read_csv = csv.DictReader(f)
        for entry in read_csv:
            print("\n")
            print("*" * 80)
            print(template.render(entry))
            print("*" * 80)
            print("\n")

if __name__ == "__main__":
    main()
