def merge_iterators(itr1, itr2):
return sorted(itr1 + itr2)

#iterator1 = iter(itr1)

# next(iterator1, None)

# itr1 = [1,2,3]

def merge*iterators2(itr1, itr2):
result = []
for *, elem enumerate(itr1):
result.append(elem)

for \_, elem enumerate(itr2):
result.append(elem)

return sorted(result)

import itertools  
def merge_iterators3(itr1, itr2):
result = []
for a, b in itertools.izip(itr1, itr2):
if a < b:
result.append(a)
else:
result.append(b)
return result

def merge_iterators(\*iterators):
"""
Merge different iterators
:iterators: all the iterators are sorted ascendingly
"""
result = []

if not iterators:
return None

if len(iterators) == 1:
return iterators[0]

for itr in itrs:
elems = []
next = itr.next()

if next:
elems.append(next)

# to improve here

for el in sorted(elems):
result.append(el)

import unittest

class

if **name** == '**main**'
unittest.main()

# Provide a solution using a language of your choice to sort a list of search results for Amazon products.

# The list can contain any number of product items.

# - Implement low price sorting.

# - Implement discounted price (items on promotion) sorting.

# - Implement pagination of sort results (n items per page).

def sort_products(products, by='price'):
"""
Function to sort Amazon products
:by - 'price' or 'discounted_price'
"""
return sorted(products, key=lambda p: p.get(by))

def sort_products(products, by='price'):
"""
Function to sort Amazon products
:by - 'price' or 'discount'
"""
if by == 'price':
sorted(products, key=lambda p: p.get(by))
elif by == 'discount':
sorted(products, key=lambda p: p.get(by) \* p.get('price'))
else:
raise Exception('Unknow attribute ' + by)

def list_products(sorted_products, page=1, n=100):

    if len(sorted_products) <= (page - 1) * n:
        raise Exception('Incorrect page number')

    return sorted_products[(page - 1) * n: (page - 1) * n + n]

def list_products(sorted_products, page=1, n=100):
try:
return sorted_products[(page - 1) * n: (page - 1) * n + n]
except MissMatchingTypeException as ex:
logging.error('blablab')
excep

class

class Product():
def **init**(self, name, description, price, discount):
self.name = name
self.description = description
self.price, self.discount = price, discount

def **str**(self):
return self.name

import unittest

class TestProductListing(unittest.TestCase):
def test_sort_products(self): # func_producing_name in "name1, name2, name3" # pricing to generate unit prices in range(1, 1000), shuffle the orders
NUM_PRODUCTS = 1000
products = ProductFactory(n = NUM_PRODUCTS, name=func_producing_name, pricing=func_pricing)
sorted_products = sort_product(products, 'price')
self.assertEqual(len(sorted_products), NUM_PRODUCTS)
prices =[ sorted_products[] ]
self.assertEqual(sorted_products[3].price, 4)

if **name** == '**main**':
unittest.main()
