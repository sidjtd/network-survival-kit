#!/usr/bin/env python
import argparse

def pingsweep(args):
    print(args)

def traceroute(args):
    print(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Network Survival Kit',
                                    description='Command line network toolkit')

    # parser.add_argument('ip', nargs=1, default='127.0.0.1', help='IP address')

    # parser.add_argument('--port', '-p', type=int)

    # parser.add_argument('--protocal', '-P', nargs='?', default='tcp', choices=['tcp', 'udp', 'icmp'])

    subparsers = parser.add_subparsers(help='Module specific utilities')

    parser_pingsweep = subparsers.add_parser('pingsweep', help='Perform network ping sweep')
    parser_pingsweep.add_argument('ip', nargs=1, help='Target IP Address')
    parser_pingsweep.set_defaults(func=pingsweep)

    parser_traceroute = subparsers.add_parser('traceroute', help='Trace the route')
    parser_traceroute.add_argument('ip', nargs=1, help='Target IP Address')
    parser_traceroute.set_defaults(func=traceroute)

    args = parser.parse_args()
    print('Arguments: {}'.format(args))
    # print('IP Address: {}'.format(args.ip))
    # print('Port is: {}'.format(args.port))
    # if args.ip:
    #     pingsweep(args.ip)