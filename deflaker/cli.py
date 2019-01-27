# -*- coding: utf-8 -*-

"""Console script for deflaker."""
import sys
import argparse
from .deflaker import find_flaky_tests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sha', type=str, default='HEAD~1', help='SHA to compare against to find flaky tests.')
    parser.add_argument('--repo', type=str, help='File path to git repo to get changes for.', required=True)
    parser.add_argument('--tests', type=str, help='File path to test.', required=True)
    args = parser.parse_args()

    sys.stdout.write('Finding flaky tests...\n')
    flaky_tests = find_flaky_tests(sha=args.sha, git_repo=args.repo, tests=args.tests)

    if flaky_tests:
        sys.stdout.write('\n'.join(flaky_tests))
    else:
        sys.stdout.write('No flaky tests!')
    sys.stdout.write('\n')
    

if __name__ == '__main__':
    main()
