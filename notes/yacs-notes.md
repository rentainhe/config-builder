## yacs使用记录

yacs库，用于为一个系统构建config文件

### Install

```bash
$ pip install yacs
```

### Import

```python
from yacs.config import CfgNode as CN
```

### Usage

#### create config node

需要创建`CN()`这个作为容器来装载我们的参数，这个容器可以嵌套

```python
from yacs.config import CfgNode as CN
__C = CN()
__C.name = 'test'
__C.model = CN()  # 嵌套使用
__C.model.backbone = 'resnet'
__C.model.depth = 18

print(__C)  
'''
  name: test
  model:
      backbone: resnet
      depth: 18
'''
```

### API reference

use `__C` as created config file

#### 1. clone()

return a copy config file, so the defaults will not be altered

```python
def get_cfg_defaults():
	return __C.clone()
```

#### 2. clear()

clear your config file, you will get  `None` as the result

```python
print(__C.clear())  # None
```

#### 3. merge_from_file()

对于不同的实验，你有不同的超参设置，所以你可以使用yaml文件来管理不同的configs，然后使用`merge_from_file()`这个方法，这个会比较每个experiments特有的config和默认参数的区别，会将默认参数与特定参数不同的部分，用特定参数覆盖。

```python
__C.merge_from_file("./test_config.yaml")
```

Addition:

- 你需要merge的yaml文件中，不能有default参数中不存在的参数，不然会报错，但是可以比default中设定的参数少，比如default文件中有name参数，这是不需要特定改动的，你可以在yaml中不设置name这个key。

```python
from yacs.config import CfgNode as CN
# default cfgs
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18

# yaml cfgs
# 不报错的情况1：参数和default中一样多，并且层级关系一致
name: test
model:
    backbone: resnet
    depth: 18

# 不报错的情况2：参数可以比default中少，以下例子就不包含name和model.backbone
model: 
    depth: 34

# 报错的情况1：以下多了model.batch_normalization这个额外的key，这在default中是不存在的
name: test
model:
    backbone: resnet
    depth: 29
    batch_normalization: True

# 报错的情况2：关键词不一致，这里的关键词是na_me，而default中是name
na_me: test
```

#### 4. merge_from_list()

可以用`list`来传递参数

```python
from yacs.config import CfgNode as CN
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18
print(__C)
'''
model:
  backbone: resnet
  depth: 18
name: test
'''

opts = ["name", 'test_name', "model.backbone", "vgg"]
__C.merge_from_list(opts)
print(__C)
'''
model:
  backbone: vgg
  depth: 18
name: test_name
'''
```

other details are the same as `merge_from_file`

#### 5. merge_from_other_cfg()

the same as `merge_from_file` and `merge_from_list`, the only difference is that the merged file is also a `CfgNode` class

#### 6. freeze()

freeze the configs, and you can not change the value after this operation

```python
from yacs.config import CfgNode as CN
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18

# freeze the config
__C.freeze()
# try to change the name's value, raise an error
__C.name = 'test2'  # error
```

#### 7. defrost()

reverse operation of `freeze()`

```python
from yacs.config import CfgNode as CN
__C = CN()
__C.name = 'test'
__C.model = CN()
__C.model.backbone = 'resnet'
__C.model.depth = 18

# freeze the config
__C.freeze()
# try to change the name's value, raise an error
__C.name = 'test2'  # error

__C.defrost()  # not freeze cfgs, after this operation you can change the value
__C.name = 'test2'  # work
```



