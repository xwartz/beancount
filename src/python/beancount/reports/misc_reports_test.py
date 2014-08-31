import argparse
import unittest

from beancount.reports import misc_reports
from beancount.reports import report
from beancount.reports import report_test
from beancount.parser import options


class TestMiscReports(unittest.TestCase):

    def test_all_reports_empty(self):
        # Test rendering all reports from empty liss of entries.
        entries = []
        errors = []
        options_map = options.DEFAULT_OPTIONS.copy()

        for report_, format_ in report_test.iter_reports(misc_reports.__reports__):
            output = report_.render(entries, errors, options_map, format_)
            self.assertEqual(options.DEFAULT_OPTIONS, options_map)
            self.assertTrue(isinstance(output, str))