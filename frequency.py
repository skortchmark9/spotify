import sys
import json
from collections import Counter
import common

def main():
    stopwords = [line.strip() for line in open(sys.argv[1])]
    tweet_file = open(sys.argv[2])

    tweets = common.get_tweets_text(tweet_file)

    words = Counter()

    for tweet in tweets:
        words.update([parse(word) for word in tweet.split() if parse(word) not in stopwords])

    all_words = sum(words.values())

    for word, freq in words.most_common():
        print('{0} {1}'.format(word.encode('utf-8'), float(freq) / all_words))


def parse(word):
    return word.lower().split("'")[0]

if __name__ == '__main__':
    main()
