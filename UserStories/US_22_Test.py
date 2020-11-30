import unittest
from UserStories.US_22 import US_22
from Programs.Base_File import Repository

class US_22_Test(unittest.TestCase):
    def test_US_22(self):
        """ Function that tests user story 22 """
        repository = Repository("../GedcomFiles/SSW_555_updatedwithUS_2_3.ged")
        expected = []
        actual = US_22(repository.get_individual(), repository.get_family())
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)