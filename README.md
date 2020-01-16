# numpy_ringbuffer

[![Build Status](https://travis-ci.org/eric-wieser/numpy_ringbuffer.svg?branch=master)](https://travis-ci.org/eric-wieser/numpy_ringbuffer)
[![codecov](https://codecov.io/gh/eric-wieser/numpy_ringbuffer/branch/master/graph/badge.svg)](https://codecov.io/gh/eric-wieser/numpy_ringbuffer)

Ring (aka circular) buffers backed by a numpy array, supporting:

 * Operations from `collections.deque`
   * `b.append(val)`
   * `b.appendleft(val)`
   * `b.extend(val)`
   * `b.extendleft(val)`
   * `b.pop(val)`
   * `b.popleft(val)`
 * The `collections.Sequence` protocol (unoptimized)
 * C-side unwrapping into an array with `np.array(b)`
 * Arbitrary element dtypes, including extra dimensions like `RingBuffer(N, dtype=(int, 3))` or `RingBuffer((N, 3), dtype=3)`
 * 1d circular columns via `RingBuffer((N, 1), dtype=int)`

For example:

```python
import numpy as np
from numpy_ringbuffer import RingBuffer

r = RingBuffer(capacity=4, dtype=np.bool)
r.append(True)
r.appendleft(False)
print(np.array(r))  # array([False, True])
```