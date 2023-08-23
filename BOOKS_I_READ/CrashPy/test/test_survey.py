
'''testing the AnonymousSurvey class'''

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''Test for the class AnonymousSurvey'''

    def test_store_single_response(self):
        '''test that a single response is stored properly'''

        question = "What language did you learn first?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn("English",my_survey.response)

    def test_store_three_response(self):
        '''test that three responses are stored properly'''

        question = 'What language did you first learn?'
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.response)


if __name__ == "__main__":
    unittest.main()
