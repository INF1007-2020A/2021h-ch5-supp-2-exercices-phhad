#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	text = ''
	count = 0
	for j in text:
		if j.isalnum(text):
			count += 1
		else:
			count -= 1
	return count

def get_word_length_histogram(text):
	return [0]

def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
