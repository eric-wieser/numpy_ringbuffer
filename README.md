# numpy_ringbuffer

[![Build Status](https://github.com/eric-wieser/numpy_ringbuffer/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/eric-wieser/numpy_ringbuffer/actions/workflows/main.yml)
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
 * Arbitrary element dtypes, including extra dimensions like `RingBuffer(N, dtype=(int, 3))`

For example:

```python
import numpy as np
from numpy_ringbuffer import RingBuffer

r = RingBuffer(capacity=4, dtype=np.bool)
r.append(True)
r.appendleft(False)
print(np.array(r))  # array([False, True])
```