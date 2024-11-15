## Original README.mdi
Plaese refer to [README_mmrot.md](https://github.com/ausmlab/building_OBB/blob/main/README_mmrot.md).

## Installation

Please refer to [Installation](https://mmrotate.readthedocs.io/en/latest/install.html) for installation instructions.

## Preparing Data
Please make sure that data files sturcture should be the following.
```
[DATA_ROOT]
    |--annotations
    |    |--instances_tran.json
    |    |--instances_val.json
    |    |--instances_test.json
    |--train
    |    |--XXX.png
    |--val
    |    |--YYY.png
    |--test
         |--ZZZ.png
```

Then, run `MakeOBBAnnotations.py` to make OBB annotations from polygon.
- Make sure that you should change `DATA_ROOT` to your own path.
- Each text file is created according to each image name.
- Order of annotations are the same as DOTA format.
- a path of `OBB` having OBB annotations will be added.
```
[DATA_ROOT]
    |--annotations
    |    |--instances_tran.json
    |    |--instances_val.json
    |    |--instances_test.json
    |--OBB
    |    |--train
    |    |    |--XXX.txt
    |    |--val
    |    |    |--YYY.txt
    |    |--test
    |         |--ZZZ.txt
    |--train
    |    |--XXX.png
    |--val
    |    |--YYY.png
    |--test
         |--ZZZ.png
```



## Training/Testing
- There are config files that I used in the `./configs/bldg_redet`  and `configs/bldg_roi_trans`.
- You have to change 'DATA_ROOT'to your own path.
- You can use each file to train and test the model. Please refer to detailed option at [get_started.md](https://github.com/ausmlab/building_OBB/blob/main/docs/en/get_started.md).
 
