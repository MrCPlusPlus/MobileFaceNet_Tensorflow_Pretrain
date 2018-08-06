# MobileFaceNet_Tensorflow_Pretrain
A tensorflow implementation from xsr-ai about mobilefacenet with pretrained parameters

The usage of this repo is same as Xsr-ai's implementation. Please review the [page](https://github.com/xsr-ai/MobileFaceNet_TF).

The pretrained model is transformed from the model provided by insightface in mxnet version. The network architectures provided by Xsr-ai and insightface are different, so I mainly modify the architecture of Xsr-ai’s implementation.

The pretrained model can be downloaded by [here](https://pan.baidu.com/s/1d2BNiV9MQrSUkIau98MymA). 

You can test the pretrained model by run "python verification.py" when you have all dependencies and data. 

This is my log when I verificate my code:

[lfw]XNorm: 11.375188<br>
[lfw]Accuracy: 0.00000+-0.00000<br>
[lfw]Accuracy-Flip: 0.99450+-0.00478<br>
Max of [lfw] is 0.99450

# References
[Mobilefacenet_TF](https://github.com/xsr-ai/MobileFaceNet_TF)<br>
[InsightFace_MXNET](https://github.com/deepinsight/insightface)
