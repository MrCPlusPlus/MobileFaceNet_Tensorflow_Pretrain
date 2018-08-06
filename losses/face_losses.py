import tensorflow as tf
import math

# This repo only provide softmax_loss. For more different losses, please review the original git:
# https://github.com/xsr-ai/MobileFaceNet_TF or https://github.com/deepinsight/insightface
def softmax_loss(logits, label):
    softmax_loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=label, logits=logits))    
    return softmax_loss