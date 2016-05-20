# CSRecon Python - Because Censys + Shodan = A Good Time :)
# Author: Mark Clayton
# Github: https://github.com/markclayton

import sys
import argparse
import os
import json
import requests
import shodan

target = ""
CENSYS_API_ID = "<CENSYS_API_ID>"
CENSYS_SECRET = "<CENSYS_SECRET>"
SHODAN_API_KEY = "<SHODAN_API_KEY>" # change shodan kEY

def censys(only_censys):
    global target
    shodan_targets = []
    CENSYS_API_URL = "https://www.censys.io/api/v1"
    print "[*] Running Censys...."

    basic_auth = {"username": CENSYS_API_ID, "password": CENSYS_SECRET}
    params = {'query': target}
    res = requests.post(CENSYS_API_URL + '/search/ipv4', auth=(CENSYS_API_ID, CENSYS_SECRET), json=params)
    if res.status_code != 200:
        print "CENSYS error occured: %s" % res
        sys.exit(1)

    for r in res.json()['results']:
        ip = r['ip']
        proto = r['protocols']
        print '[%s] IP: %s' % ("*", ip)
        for p in proto:
            print '\t %s' % (p)
        if not only_censys:
            shodan_targets.append(r['ip'])

    # print shodan_targets
    if only_censys:
        sys.exit(1)
    else:
        run_shodan(shodan_targets)


def run_shodan(targets):
    print "[*] Running Shodan...."
    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        result = api.search("Google")

        for ip in targets:
            query = ' '.join(ip)
            result = api.search(ip)
            for service in result['matches']:
                print "Shodan match: %s" % service['ip_str']
                print "Org: %s" % service['org']
                print "Hostnames: %s" % service['hostnames']
                print "Port: %s" % service['port']

    except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)

def main():
    global target
    only_censys = False
    only_shodan = False
    parser = argparse.ArgumentParser(
    description="CSRecon - Censys and Shodan Reconnaisance Tool")
    parser.add_argument('target', help='specify a target company name')
    parser.add_argument("-c", "--censys", help="only run the censys module", action="store_true")
    parser.add_argument("-s", "--shodan", help="only run the shodan module", action="store_true")
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    target = args.target
    if args.censys:
        only_censys = True
        censys(only_censys)
    elif args.shodan:
        only_shodan = True
        run_shodan(target)
    else:
        censys(False)


main()
