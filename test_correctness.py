import importlib
import os
import re
import unittest
from collections import OrderedDict

from utils import get_input_for_day


class AdventTests(unittest.TestCase):
    def test_all(self):
        for expected, module in zip(AdventTests.answers, AdventTests.module_dict):
            actual = self.solve(module)
            with self.subTest(msg=f'{module} | expected:{expected}, actual:{actual}'):
                self.assertEqual(expected, actual)

    def solve(self, module_name):
        day = re.match(r'd(\d+)', module_name).group()
        return AdventTests.module_dict[module_name].run(get_input_for_day(day))

    @classmethod
    def setUpClass(cls):
        with open('spoilers.txt') as answers:
            cls.answers = [int(ans.rstrip('\n')) for ans in answers.readlines() if ans.strip()]

        cls.module_dict = dict()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        files = [f[:-3] for f in os.listdir(current_dir) if f.startswith('d') and f.endswith('.py')]
        for file in files:
            module = importlib.import_module(file)
            cls.module_dict[file] = module

        cls.module_dict = OrderedDict(sorted(cls.module_dict.items(),
                                             key=lambda pair: tuple(map(int, re.findall(r'\d+', pair[0])))))
        assert len(cls.answers) == len(cls.module_dict), "module or answer missing"


if __name__ == '__main__':
    unittest.main(buffer=False)
