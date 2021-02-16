from yacs.config import CfgNode as CN
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18
print(__C)
opts = ["name", 'test_name', "model.backbone", "vgg"]
__C.merge_from_list(opts)
print(__C)

__C.freeze()
__C.defrost()
__C.name = 'try_to_change_the_name'
print(__C)