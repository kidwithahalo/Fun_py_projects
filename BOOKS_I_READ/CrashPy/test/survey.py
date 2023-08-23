class AnonymousSurvey:
    '''collect anonymous answers to a survey question'''

    def __init__(self, question):
        '''store a question, and prepare to store responses'''
        self.question = question
        self.response = []

    def show_question(self):
        '''show the survey question'''
        print(self.question)

    def store_response(self, new_response):
        '''store the responses to survey'''
        self.response.append(new_response)

    def show_results(self):
        '''show all the responses to a survey'''
        print('Survey results: ')
        for respond in self.response:
            print(f"- {respond}")
