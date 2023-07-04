"""
start 4:20ish
finish 4:46pm"""

from typing import (
    List,
)
from collections import defaultdict
import heapq


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        alphabet = set()
        for w in words:
            alphabet = alphabet.union(w)

        # construct graph where lexographically first -> lexographically next
        adj_matrix = defaultdict(set)

        # groups of words where the prefix matches (starting prefix is "")
        groups = [words]
        while groups:
            next_groups = []
            for group in groups:
                letter_to_group = defaultdict(list)
                last_letter = None
                for word in group:
                    if last_letter and last_letter != word[0]:
                        # create edge
                        adj_matrix[last_letter].add(word[0])
                    last_letter = word[0]

                    # add to matching prefix group
                    if len(word) > 1:
                        letter_to_group[word[0]].append(word[1:])
                    else:
                        # in case lexographical order is wrong
                        if letter_to_group[word[0]]:
                            return ""

                # add valid groups to the next group for future processing
                for next_group in letter_to_group.values():
                    if len(next_group) > 1:
                        next_groups.append(next_group)
            groups = next_groups

        # toplogically sort graph
        in_degree = defaultdict(int)
        no_in_degree_set = alphabet.copy()
        for v in adj_matrix:
            for u in adj_matrix[v]:
                in_degree[u] += 1
                if u in no_in_degree_set:
                    no_in_degree_set.remove(u)

        # generate lexographically smallest order & return
        ret_str = ""
        no_in_degree_heap = list(no_in_degree_set)
        heapq.heapify(no_in_degree_heap)
        while no_in_degree_heap:
            next_letter = heapq.heappop(no_in_degree_heap)
            ret_str += next_letter
            for u in adj_matrix[next_letter]:
                in_degree[u] -= 1
                if in_degree[u] == 0:
                    heapq.heappush(no_in_degree_heap, u)

        if len(ret_str) == len(alphabet):
            return ret_str
        else:
            return ""
