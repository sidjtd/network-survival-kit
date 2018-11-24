#!/usr/bin/env python
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Network Survival Kit',
                                    description='Command line network toolkit')

    parser.add_argument('ip', nargs=1, default='127.0.0.1', help='IP address')

    parser.add_argument('--port', '-p', type=int)

    parser.add_argument('--protocal', '-P', nargs='?', default='tcp', choices=['tcp', 'udp', 'icmp'])

    args = parser.parse_args()
    print('Arguments: {}'.format(args))
    print('IP Address: {}'.format(args.ip))
    print('Port is: {}'.format(args.port))