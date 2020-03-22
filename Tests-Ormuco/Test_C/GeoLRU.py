#!/usr/bin/env python

'''
Strategy:
Build a class for the GeoItem, containing it's properties
Build a class for the Cache, containing it's rules
Provide the interfaces PUT and GET, to deadly simple use.

Instantiate the object GeoItem
Instantiate the object LRU_cache

Put GeoItems in cache
Manipulate GeoItems in cache

To Do: Separate Public and Private sections, granting public access only to the Put and Get methods
'''

class GeoItem(object):
	def __init__(self, key, value, region, time):
		self.key = key
		self.value = value
		self.region = region
		self.time = time
		self.saved = False
		self.consistency = False
		self.previous_e = None
		self.next_e = None

	def __str__(self):
		return "(%s, %s, %s, %s, %s, %s)" % (self.key, self.value, self.region, self.time, self.saved, self.consistency)


class LRU(object):
	def __init__(self, limit):
		self.error = False
		self.check = False      # check consistency
		self.success = False    # Write on disk Success
		self.new_key = 0
		self.new_value = ""
		self.region = ""
		self.time = 0

		if limit <= 0:
			raise ValueError("Limit must be grater than 0")

		self.limit = limit
		self.actual_size = 0
		self.first_e = None
		self.last_e = None

		self.lru_cash_map = {}

	def get_value(self, s_key):
		# return the element and moves it to the first [0] position of the LRU
		# if the element has expired or being discarded returns null (None)
		if s_key not in self.lru_cash_map:
			return None

		element = self.lru_cash_map[s_key]
		if self.first_e == element:
			return element.value
		self.remove_element(element)
		self.insert_element(element)
		self.time_tick()
		self.write_to_disk()            # To do
		self.check_consistency("A")     # To do: pass self.region
		return element.value

	def put_value(self, new_element):
		# insert new value in the first position [0] of the LRU list
		self.new_key = new_element.key
		self.new_value = new_element.value
		self.region = new_element.region
		self.time = new_element.time

		self.time_tick()    # decreases lifetime for everyone before inserting the new item
							# so if any item expires opens a new place in the cache

		if self.new_key in self.lru_cash_map:
			element = self.lru_cash_map[self.new_key]
			element.value = self.new_value
			if self.first_e != element:
				self.remove_element(element)
				self.insert_element(element)
		else:
			insert_element = GeoItem(self.new_key, self.new_value, self.region, self.time)
			if self.actual_size == self.limit:
				del self.lru_cash_map[self.last_e.key]
				self.remove_element(self.last_e)
			self.insert_element(insert_element)
			self.lru_cash_map[self.new_key] = insert_element

		self.write_to_disk()

	def remove_element(self, element):
		if not self.first_e:
			return

		# remove one element in the middle, not first, not last one
		if element.previous_e:
			element.previous_e.next_e = element.next_e
		if element.next_e:
			element.next_e.previous_e = element.previous_e

		# Only one element on lru cache
		if not element.next_e and not element.previous_e:
			self.first_e = None
			self.last_e = None

		# if the element is the last
		if self.last_e == element:
			self.last_e = element.next_e
			self.last_e.prev_e = None

		self.actual_size -= 1
		return element

	def insert_element(self, element):
		# insert element at cache first position (newest)
		if not self.first_e:
			self.first_e = element
			self.last_e = element
		else:
			element.previous_e = self.first_e
			self.first_e.next_e = element
			self.first_e = element
		self.actual_size += 1       # limit is verified in put_elemet()

	def check_consistency(self, region):
		# TO DO: Call close regions to check data consistency
		self.check = region
		# to do: verify neighbors, compare data, check consistency
		self.error = False
		if self.error:
			return "Error "+self.check
		else:
			return self.check+" OK"

	def write_to_disk(self):
		# TO DO: write the file to disk
		self.error = False
		self.success = not self.error
		return self.success

	def time_tick(self):
		# every manipulation on the LRU decreases the time to live of each object on list
		# when the time falls to 0 the item is discarded (expires)
		element = self.first_e
		# run through all elements
		while element:
			element.time -=1
			if element.time <= 0:
				self.remove_element(element)
			element = element.previous_e

	def print_values(self):
		element = self.first_e
		# run through all elements
		while element:
			print element       # using builtin __str__ defined in class
			element = element.previous_e
		print

if __name__ == "__main__":
	cache = LRU(5)                           # create the LRU cache with 5 elements limit
	# All items starting with same Time To Live (TTL = 10)
	item = GeoItem(1, "Quick", "A", 05)      # create an item key = 1, value = Quick, Region = A, time to live = 5
	cache.put_value(item)                    # Put the item on the cache
	item = GeoItem(2, "Brown", "B", 05)      # create an item key = 2, value = Brown, Region = B, time to live = 6
	cache.put_value(item)                    # Put the item on the cache
	item = GeoItem(3, "Fox", "A", 05)        # create an item key = 3, value = Fox,   Region = A, time to live = 2
	cache.put_value(item)                    # Put the item on the cache
	item = GeoItem(4, "Jumps", "C", 05)      # create an item key = 4, value = Jumps, Region = C, time to live = 1
	cache.put_value(item)                    # Put the item on the cache
	item = GeoItem(5, "Over", "C", 05)       # create an item key = 5, value = Over,  Region = C, time to live = 8
	cache.put_value(item)                    # Put the item on the cache
	item = GeoItem(6, "Lazy", "D", 05)       # create an item key = 6, value = Lazy,  Region = D, time to live = 9
	cache.put_value(item)                    # Put the item on the cache - Oldest item (1 - quick) is discarded
	# each move made on the cache decreases TTL for existing elements
	cache.print_values()

	cache.get_value(3)                      # get the element 3,
											# move it to the first position [0].
											# Decreases lifetime for all elements on LRU.
											# item 2 (Brown) expires.
	cache.print_values()

'''	
--OUTPUT:

(6, Lazy, D, 5, False, False)
(5, Over, C, 4, False, False)
(4, Jumps, C, 3, False, False)
(3, Fox, A, 2, False, False)
(2, Brown, B, 1, False, False)

(3, Fox, A, 1, False, False)
(6, Lazy, D, 4, False, False)
(5, Over, C, 3, False, False)
(4, Jumps, C, 2, False, False)
'''