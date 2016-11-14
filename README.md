# numpy_ringbuffer

[![Build Status](https://travis-ci.org/eric-wieser/numpy_ringbuffer.svg?branch=master)](https://travis-ci.org/eric-wieser/numpy_ringbuffer)

[![codecov](https://codecov.io/gh/eric-wieser/numpy_ringbuffer/branch/master/graph/badge.svg)](https://codecov.io/gh/eric-wieser/numpy_ringbuffer)

Circular buffers (aka ring buffers) backed by a numpy array, supporting the operations:

 * `b.append(val)`
 * `b.appendleft(val)`
 * `b.pop(val)`
 * `b.popleft(val)`
 * `np.array(b)` - fast unwrapping into a numpy array, for vectorization

For example:

```python
import numpy as np
from numpy_ringbuffer import RingBuffer

r = RingBuffer(capacity=4, dtype=np.bool)
r.append(True)
r.appendleft(False)
print(np.array(r))  # array([False, True])
```