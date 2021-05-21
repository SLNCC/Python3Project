# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import  unittest

from  survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """ 创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']


    def  test_store_single_reponse(self):
        """测试单个答案呗妥善地储存"""
        self.my_survey = AnonymousSurvey(self.responses[0])
        self.my_survey.store_response('English')
        self.assertIn(self.responses[0],self.my_survey.responses)

    def  test_store_three_reponse(self):
        """测试单个答案呗妥善地储存"""
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()