# -*- coding: utf-8 -*-
"""Main module."""
import pytest
import coverage
import re
from git import Repo
from unidiff import PatchSet
from collections import defaultdict


class Plugin:
    """
    Plugin to hook into pytest between tests.
    https://docs.pytest.org/en/latest/_modules/_pytest/hookspec.html
    """

    def __init__(self, file_name_to_lines_numbers):
        self.flaky_tests = set()
        self.file_name_to_lines_numbers = file_name_to_lines_numbers

    def has_coverage_overlap_with_file_changes(self, coverage_data):
        """
        :param CoverageData coverage_data: the coverage data from the test run
        :returns: if the file changes has any overlap with the coverage data
        :rtype: boolean
        """
        for file_name, line_numbers in self.file_name_to_lines_numbers.items():
            if set(coverage_data.lines(file_name)).intersection(line_numbers):
                return True
        return False

    def pytest_runtest_logreport(self, report):
        if report.failed:  
            data = self.cov.get_data()
            if not self.has_coverage_overlap_with_file_changes(data):
                self.flaky_tests.add(report.nodeid)

    def pytest_runtest_call(self, item):
        self.cov = coverage.Coverage()
        self.cov.start()

    def pytest_runtest_teardown(self, item):
        self.cov.stop()


def get_file_name_to_lines_numbers(repo, sha):
    """
    Parse git diff, see format:
    http://www.gnu.org/software/diffutils/manual/diffutils.html#Detailed-Unified

    :param Repo repo: The repo to get file changes for.
    :param str sha: The SHA to compare diff with.
    :returns: File name to line numbers.
    :rtype: dict(str, set)
    """
    files = PatchSet(repo.git.diff(sha, **{'unified': 0}))
    path = repo.working_dir
    file_name_to_lines_numbers = defaultdict(set)
    for file in files:
        file_name = '{path}/{file}'.format(file=file.target_file[2:], path=path)
        file_name_to_lines_numbers[file_name] = set([
            line.target_line_no 
            for hunk in file
            for line in hunk.target_lines()
        ])
    return file_name_to_lines_numbers


def find_flaky_tests(sha, git_repo, tests):
    """
    :param str git_repo: The file path to the git repo.
    :param str sha: The SHA to compare diff with.
    :param str tests: File path to the tests.
    :returns: List of flaky tests
    :rtype: list(str)
    """
    plugin = Plugin(
        file_name_to_lines_numbers=get_file_name_to_lines_numbers(
            repo=Repo(git_repo),
            sha=sha,
        ),
    )
    pytest.main([tests, '-s', '-p', 'no:terminal'], plugins=[plugin])
    return list(plugin.flaky_tests)
