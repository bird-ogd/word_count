from pprint import pprint
import operator
import csv

def csv_to_list(csv_file):
	f = open(csv_file)
	reader = csv.reader(f)
	result = list(csv.reader(f))
	return result

def word_count(str, excl_words):
	counts = dict()
	words = str.split()

	for word in words:
		if word.lower() not in excl_words:
			if word.lower() in counts:
				counts[word.lower()] += 1
			else:
				counts[word.lower()] = 1
	return counts

filedoc = open('text_doc')
string = filedoc.read()

excl_words = csv_to_list("excluded_words.csv")
excl_words = [item for sublist in excl_words for item in sublist]
word_list = word_count(string, excl_words)
sorted_word_list = sorted(word_list.items(), key=operator.itemgetter(1))

pprint(sorted_word_list)