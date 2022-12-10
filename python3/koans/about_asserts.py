# !/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):
#each function is a test
#docstrings are descriptions of functions
#
    def test_assert_truth(self):  
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        self.assertTrue(True) # This should be True

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        self.assertTrue(True, "This should be True -- Please fix this")

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(2, 1 + 1)
#self.assertEqual(1, 1) is a call on a function called assertEqual. arguments are values you pass to functions. values can be functions as well.
    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)
#variable=name to refer to it; double equal is an operator that evaluates to a boolean. calling assertTrue on the value of the boolean on the equality of expected_value and actual_value.
#code is computer instructions; programming language is the proper way to instruct a computer to do something. python is imperative style, you tell machine exactly what to do.
#assertTrue takes one argument, which is a boolean      
    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)
#assertEqual takes two arguments.
    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.
        """

        # This throws an AssertionError exception
        assert True
#Built into Python's language is the statement known as assert
    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:
#attribute=values contained inside of an object. example:integers have a numerator and denominator.
        self.assertEqual(str, "navel".__class__) # It's str, not <type 'str'>

        # Need an illustration? More reading can be found here:
        #
        #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute