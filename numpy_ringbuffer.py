import numpy as np
from collections import Sequence

class RingBuffer(Sequence):
	raise_on_overwrite = False

	def __init__(self, capacity, dtype=np.float64):
		self._arr = np.empty(capacity, dtype)
		self._left_index = 0
		self._right_index = 0
		self._capacity = capacity


	def _unwrap(self):
		""" Copy the data from this buffer into unwrapped form """
		return np.concatenate((
			self._arr[self._left_index:min(self._right_index, self._capacity)],
			self._arr[:max(self._right_index - self._capacity, 0)]
		))

	def _fix_indices(self):
		"""
		Enforce our invariant that 0 <= self._left_index < self._capacity
		"""
		if self._left_index >= self._capacity:
			self._left_index -= self._capacity
			self._right_index -= self._capacity
		elif self._left_index < 0:
			self._left_index += self._capacity
			self._right_index += self._capacity
	@property
	def is_full(self):
		return len(self) == self._capacity


	# these mirror methods from deque
	@property
	def maxlen(self):
		return self._capacity

	def append(self, value):
		if self.is_full:
			if self.raise_on_overwrite:
				raise ValueError
			else:
				self._left_index += 1

		self._arr[self._right_index % self._capacity] = value
		self._right_index += 1
		self._fix_indices()

	def appendleft(self, value):
		if self.is_full:
			if self.raise_on_overwrite:
				raise ValueError
			else:
				self._right_index -= 1

		self._left_index -= 1
		self._fix_indices()
		self._arr[self._left_index] = value

	def pop(self):
		if len(self) == 0:
			raise IndexError
		self._right_index -= 1
		self._fix_indices()
		res = self._arr[self._right_index % self._capacity]
		return res

	def popleft(self):
		if len(self) == 0:
			raise IndexError
		res = self._arr[self._left_index]
		self._left_index += 1
		self._fix_indices()
		return res


	def __array__(self):
		return self._unwrap()

	# implement Sequence methods
	def __len__(self):
		return self._right_index - self._left_index

	def __getitem__(self, item):
		return self._unwrap()[item]

	def __iter__(self):
		return iter(self._unwrap())

	# Everything else
	def __repr__(self):
		return '<RingBuffer of {!r}>'.format(np.asarray(self))