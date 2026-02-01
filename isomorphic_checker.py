from collections import defaultdict
from typing import Tuple


class IsomorphicChecker:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.mapping_a = {}
        self.mapping_b = {}

    def is_isomorphic(self):
        pass

    def check_degree_sequence(self):
        c = sorted([len(self.a[v])  for v in self.a])
        d = sorted([len(self.b[v]) for v in self.b])

        return c is d

    def initial_part(self):
        def par_by_degree(g):
            pars = defaultdict(set)
            for node in g:
                degree = len(g[node])
                pars[degree].add(node)
            return list(pars.values())
        return par_by_degree(self.a), par_by_degree(self.b)
    def refine_step(self):
        pass

    def refine_part(self, m, n, max_iter=100):
        for _ in range(max_iter):
            self.refine_step(m)
            self.refine_step(n)

            if self:
                pass

    @staticmethod
    def part_signature(par):
        return Tuple(sorted([len(p) for p in par ]))