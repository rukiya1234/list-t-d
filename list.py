les, Lists & Dictionary Exercises

# I. Find length of tuple without len()
def tuple_length(t):
    count = 0
    for _ in t:
        count += 1
    return count

# II. Max and Min from tuple
def max_min_tuple(t):
    return max(t), min(t)

# III. Remove duplicates from list
def remove_duplicates(lst):
    return list(set(lst))

# IV. Square elements
def square_elements(lst):
    return [x**2 for x in lst]

# V. Merge dictionaries
def merge_dicts(d1, d2):
    return {d1, d2}

# VI. Swap keys and values
def swap_dict(d):
    return {v: k for k, v in d.items()}

# VII. Fibonacci with memoization
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# VIII. Pythagorean triplets
def pythagorean_triplets(n):
    return [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a*a+b*b==c*c]

# IX. Shopping cart
def shopping_cart():
    cart = {}
    def add_item(item, price):
        cart[item] = cart.get(item, 0) + price
    def remove_item(item):
        if item in cart:
            del cart[item]
    def total():
        return sum(cart.values())
    return add_item, remove_item, total

# X. LRU cache (simple)
from collections import OrderedDict
class LRUCache:
    def init(self, max_size):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)
