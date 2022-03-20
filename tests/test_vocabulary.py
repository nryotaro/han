import unittest
import han.vocabulary as v


class VocabularyTestCase(unittest.TestCase):
    def test(self):
        sut = v.build_vocabulary(
            [["blue"], ["blue", "glass"]], unknown_index=-1
        )
        self.assertEqual(set(sut.get_stoi().keys()), set(["blue", "glass"]))
        self.assertEqual(sut["a"], -1)
