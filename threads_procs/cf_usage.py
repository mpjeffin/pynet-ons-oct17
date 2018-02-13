#!/usr/bin/env python3
'''
Use processes and Netmiko to connect to each of the devices. Execute
'show version' on each device. Use concurrent futures built-in queue
to pass the output back to the parent process. Record the amount of
time required to do this.
'''
import concurrent.futures as cf
from datetime import datetime

from netmiko import ConnectHandler

from my_devices import device_list as devices


def show_version(a_device):
    '''
    Use Netmiko to execute show version.
    Return the result as a dictionary.
    '''

    output_dict = {}
    remote_conn = ConnectHandler(**a_device)
    hostname = remote_conn.base_prompt
    output = remote_conn.send_command("show version | inc ersion")
    output_dict[hostname] = output
    return output_dict


def main():
    '''
    Use processes and Netmiko to connect to each of the devices. Execute
    'show version' on each device. Use concurrent futures built-in queue
    to pass the output back to the parent process. Record the amount of
    time required to do this.
    '''

    start_time = datetime.now()

    # Start a ThreadPool (or ProcessPool if you change Thread to Process)
    # Using 5 workers (threads/processes) simultaneously

    with cf.ThreadPoolExecutor(max_workers=5) as executor:

        # Start the Netmiko operation and mark each future with its device dict

        future_to_device = {
            executor.submit(show_version, a_device): a_device
            for a_device in devices
        }

        # Do something with the results as they complete. Could be a print,
        # a database write to, or write to a CSV to store for later use

        for future in cf.as_completed(future_to_device):

            device = future_to_device[future]['ip']

            try:
                data = future.result()
            except Exception as exc:
                print("{} generated an exception: {}".format(device, exc))
            else:
                print("{}: {}".format(device, data))

    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()
