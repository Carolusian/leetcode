# -*- coding: utf-8 -*-
import argparse
import collections
from datetime import datetime

def count_log_errors(f):
    cnt = collections.Counter()
    with open(f, 'r') as handler:
        for _, l in enumerate(handler):
            segments = l.split()
            slot = datetime.strptime(segments[3][1:-6], '%d/%b/%Y:%H')
            if segments[8].startswith('2'):
                cnt[slot] += 1

    return cnt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count error occurences in log filel.')
    parser.add_argument('--logfile', type=str)
    args = parser.parse_args()
    print(count_log_errors(args.logfile))
