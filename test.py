import unittest
import numpy as np
from numpy_ringbuffer import RingBuffer

class TestAll(unittest.TestCase):
	def test_append(self):
		r = RingBuffer(5)

		r.append(1)
		np.testing.assert_equal(r, np.array([1]))
		self.assertEqual(len(r), 1)

		r.append(2)
		np.testing.assert_equal(r, np.array([1, 2]))
		self.assertEqual(len(r), 2)

		r.append(3)
		r.append(4)
		r.append(5)
		np.testing.assert_equal(r, np.array([1, 2, 3, 4, 5]))
		self.assertEqual(len(r), 5)

		r.append(6)
		np.testing.assert_equal(r, np.array([2, 3, 4, 5, 6]))
		self.assertEqual(len(r), 5)

	def test_appendleft(self):
		r = RingBuffer(5)

		r.appendleft(1)
		np.testing.assert_equal(r, np.array([1]))
		self.assertEqual(len(r), 1)

		r.appendleft(2)
		np.testing.assert_equal(r, np.array([2, 1]))
		self.assertEqual(len(r), 2)

		r.appendleft(3)
		r.appendleft(4)
		r.appendleft(5)
		np.testing.assert_equal(r, np.array([5, 4, 3, 2, 1]))
		self.assertEqual(len(r), 5)

		r.appendleft(6)
		np.testing.assert_equal(r, np.array([6, 5, 4, 3, 2]))
		self.assertEqual(len(r), 5)

	def test_2d(self):
		r = RingBuffer(5, dtype=(np.float, 2))

		r.append([1, 2])
		np.testing.assert_equal(r, np.array([[1, 2]]))
		self.assertEqual(len(r), 1)
		self.assertEqual(np.shape(r), (1, 2))

		r.append([3, 4])
		np.testing.assert_equal(r, np.array([[1, 2], [3, 4]]))
		self.assertEqual(len(r), 2)
		self.assertEqual(np.shape(r), (2, 2))

		r.appendleft([5, 6])
		np.testing.assert_equal(r, np.array([[5, 6], [1, 2], [3, 4]]))
		self.assertEqual(len(r), 3)
		self.assertEqual(np.shape(r), (3, 2))

if __name__ == '__main__':
	unittest.main()
