# 273Kelvin
NYU Deep Learning Project

Abstract from paper

We present a semi-supervised model
for object detection tasks. The goal is to accurately
predict bounding boxes and their labels
for objects inside images. Our dataset comprises
512,000 unlabeled 224×224 images and 50,000
labeled images of various sizes that we split 60:40
for training and validation purposes. The number
of objects we train our model to recognize
is 100. We approach the task by training a selfsupervised
model to learn visual representations
from the unlabeled dataset and feed this trained
model as a backbone to a downstream task that
outputs bounding boxes and labels. We then finetune
the whole model in a supervised fashion with
the labeled dataset. We utilize SimCLR (Chen
et al., 2020), a contrastive technique, as the framework
to train the ResNet-18 backbone and Faster
R-CNN (Ren et al., 2015) for the downstream
object detection task. Overall, we achieved an
Average Precision (AP) - Intersection of Union
(IoU)=0.50:0.95 - of 0.093 on the validation set
after training for ten epochs.
