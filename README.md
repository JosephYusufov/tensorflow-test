# TensorFlow Learning Log
Joseph Yusufov
***
## 2020-08-20
A Tensor is an abstraction used to refer to any type of matrix, whether it be 1d (Vector), 2d, or n-dimensional.
- The `rank` of a tensor is synonymous with the dimenion, i.e. a 2-dimensional tensor is a tensor of rank 2
- The `shape` of a tensor is synonymous to the shape of an array. For example:
~~~
[
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]

shape: (4, 3)
~~~
- in TensorFlow, reshaping tensors is very important to manipulating data. the function `tf.reshape(tensor, shape: array)` can be used to reshape a tensor, given that the shape provided contains the same number of elements as the original tensor.
***
