from collections import defaultdict, deque

def create_adj_word_set(wordlist):
	## count letters of each one
	adj_word_set = defaultdict(set)
	for word in wordlist:
		
		for i in range(len(word)):
			key = word[:i] + "*" + word[i+1:]
			adj_word_set[key].add(word)
	return adj_word_set

def get_neighbors(word, adj_word_set):
	neighbors = set()
	for i in range(len(word)):
		key = word[:i] + "*" + word[i+1:]
		neighbors = neighbors.union(adj_word_set[key])
	neighbors.remove(word)
	return neighbors

def solution(begin_word, end_word, wordlist):
	wordlist += [begin_word]

	# construct the graph… efficiently
	adj_word_set = create_adj_word_set(wordlist)
	print(adj_word_set)
	
	# run BFS on the graph from begin_word -> end_word
	queue = deque([(begin_word, 1)])  # (node, distance)
	seen = set([begin_word])
	while queue:
		next_item, distance = queue.popleft()
		for n in get_neighbors(next_item, adj_word_set):
			if n not in seen:
				
				print((n, distance + 1))
				if n == end_word:
					return distance + 1
				seen.add(n)
				queue.append((n, distance + 1))
	
	return 0

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return solution(beginWord, endWord, wordList)