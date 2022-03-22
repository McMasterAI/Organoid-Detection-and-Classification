#Simple inference script for loading and performing single image inference on a model

import tensorflow as tf
from tensorflow.python.platform import gfile
import numpy as np

GRAPH_PB_PATH = './frozen_inference_graph.pb'

graph = tf.Graph()

with tf.gfile.GFile(GRAPH_PB_PATH, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

with graph.as_default():
    # Define input tensor
    input = tf.placeholder(np.uint8, shape = [None, None, None, 3], name='image_tensor')
    #self.dropout_rate = tf.placeholder(tf.float32, shape = [], name = 'dropout_rate')
    tf.import_graph_def(graph_def, {'image_tensor': input})

graph.finalize()

rand_int2 = np.random.randint(10,90,(1,250,250,3))


##OUTPUT NODE NAMES:
# import/detection_boxes
# import/detection_scores
# import/detection_multiclass_scores
# import/detection_features
# import/detection_classes
# import/num_detections
# import/raw_detection_boxes
# import/raw_detection_scores

detection_scores = graph.get_tensor_by_name("import/detection_scores:0")
detection_boxes = graph.get_tensor_by_name("import/detection_boxes:0")
detection_multiclass_scores = graph.get_tensor_by_name("import/detection_multiclass_scores:0")
detection_features = graph.get_tensor_by_name("import/detection_features:0")
detection_classes = graph.get_tensor_by_name("import/detection_classes:0")
num_detections = graph.get_tensor_by_name("import/num_detections:0")
raw_detection_boxes = graph.get_tensor_by_name("import/raw_detection_boxes:0")
raw_detection_scores = graph.get_tensor_by_name("import/raw_detection_scores:0")

output_tensors = [detection_scores, detection_boxes, detection_multiclass_scores, detection_features, detection_classes,
num_detections, raw_detection_boxes, raw_detection_scores]

sess = tf.Session(graph = graph)
output = sess.run(output_tensors, feed_dict = {input: rand_int2})

print(output)




###Useful code segments###

##Checking input nodes
# print('Check out the input placeholders:')
# nodes = [n.name + ' => ' +  n.op for n in graph_def.node if n.op in ('Placeholder')]
# for node in nodes:
#     print(node)

## print out all layers of graph - run after graph.finalize()
# layers = [op.name for op in graph.get_operations()]
# for layer in layers:
#     print(layer)