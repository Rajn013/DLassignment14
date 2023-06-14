#!/usr/bin/env python
# coding: utf-8

# Is it okay to initialize all the weights to the same value as long as that value is selected randomly using He initialization?

# No, it is not recommended to initialize all weights to the same value, even if randomly selected using He initialization. It is important to have diverse and unique weights to break symmetry and allow the network to learn distinct features.

# Is it okay to initialize the bias terms to 0?

# Yes, it is generally acceptable to initialize the bias terms to 0 in neural networks.

# Name three advantages of the ELU activation function over ReLU.
# 

# ELU handles negative values, allowing for the propagation of negative information.
# ELU has a smooth gradient near zero, avoiding the "dying ReLU" problem and promoting stable gradient flow.
# ELU handles saturation better for negative inputs, reducing the vanishing gradient problem

# In which cases would you want to use each of the following activation functions: ELU, leaky ReLU (and its variants), ReLU, tanh, logistic, and softmax?

# ELU (Exponential Linear Unit):
# 
# Use when you want to allow negative values and capture negative information effectively.
# Helpful in combating the "dying ReLU" problem and promoting better learning.
# 
# Leaky ReLU (and its variants):
# 
# Use when you want to mitigate the "dying ReLU" problem and avoid dead neurons.
# Provides a small non-zero slope for negative inputs.
# 
# ReLU (Rectified Linear Unit):
# 
# Use as a default choice for most cases.
# Efficient and often provides good performance.
# Effective for models with sparse activation and faster convergence.
# 
# tanh (Hyperbolic Tangent):
# 
# Use when you need activation values squashed between -1 and 1.
# Suitable for modeling positive and negative relationships.
# logistic (Sigmoid):
# 
# Use in binary classification problems, where the output represents a probability between 0 and 1.
# 
# softmax:
# 
# Use in multi-class classification problems, where the model assigns probabilities to each class.

# What may happen if you set the momentum hyperparameter too close to 1 (e.g., 0.99999) when using a MomentumOptimizer?
# 

# the momentum hyperparameter too close to 1 (e.g., 0.99999) when using a MomentumOptimizer can lead to reduced responsiveness, overshooting, oscillations, difficulty in escaping local minima, and poor convergence. It is generally advisable to choose a moderate momentum value that balances the benefits of momentum with the risk of these undesirable effects.

# Name three ways you can produce a sparse model.
# 

# L1 Regularization (Lasso regularization): Adding a penalty term that encourages the reduction of less important weights to zero, promoting sparsity in the model.
# 
# Dropout: Randomly setting a fraction of neuron activations to zero during training, leading to sparsity as some neurons become inactive.
# 
# Thresholding: Setting small magnitude weights to zero after training, effectively pruning and inducing sparsity in the model.

# Does dropout slow down training? Does it slow down inference (i.e., making predictions on new instances)?
# 

# Dropout can slightly impact training speed but generally does not significantly slow it down.
# During inference, dropout is turned off, and it does not introduce any additional computation or slowdown.
# The benefits of dropout, such as regularization and improved generalization, outweigh the minor increase in training time.

# In[ ]:




