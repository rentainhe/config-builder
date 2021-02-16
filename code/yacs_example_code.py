# import Cfg class
from yacs.config import CfgNode as CN

# create a Node
__C = CN()

# set the default config params
__C.input = CN()
__C.input.size = (32, 32)

__C.model = CN()
__C.model.name = 'resnet18'
__C.model.classes = 100

__C.dataset = CN()
__C.dataset.name = 'cifar100'
__C.dataset.dir = './data/cifar100'
__C.dataset.batch_size = 128
__C.dataset.eval_batch_size = 64

__C.dataloader = CN()
__C.dataloader.num_workers = 8
__C.dataloader.pin_memory = True
__C.dataloader.drop_last = True

__C.transforms = CN()
__C.transforms.normalization = CN()
__C.transforms.normalization.mean = [0.5, 0.5, 0.5]
__C.transforms.normalization.std = [0.5, 0.5, 0.5]


def get_cfg_defaults():
    return __C.clone()  # use clone() to get a copy one

print(__C.clear())  # None

__C.merge_from_file(r'../test_config_files/config_file.yaml')
print("merge_from_file example: ")
print(__C)
print()

opts = ["input.size", (224, 224), "model.name", "vgg"]
__C.merge_from_list(opts)
print("merge_from_list example: ")
print(__C)
print()

__C.freeze()
try:
    __C.model.name = 'vgg'
except:
    print("after freeze operation you can not change the value")
print()

__C.defrost()
__C.model.name = 'vgg'
print("after defrost operation you can change the value")
print("model.name: ")
print(__C.model.name)