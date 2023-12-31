# DPRNN

# 1.环境配置
具体环境配置在requirement.txt文件中，使用以下命令来构建环境。
```shell
pip install -r requirements.txt
```
其中torch的gpu版本的安装需要额外的驱动，在这里不再赘述，有需要可以上网自行查找。

# 2.构建数据集

## 数据集文件夹结构
├── data       
|  ├── cv    
|  |  ├── mix    
|  |  ├── s1    
|  |  └── s2     
|  ├── tr    
|  |  ├── mix    
|  |  ├── s1    
|  |  └── s2     
|  ├── tt    
|  |  ├── mix    
|  |  ├── s1    
|  |  └── s2     

## 收集单人纯净音频
将单人音频分别放入s1和s2文件夹中。

## 生成混合音频文件
首先，重命名并清洗掉过短的单人音频文件。    
注：应修改rename_file.py和clean_s1_s2.py中的文件夹目录。
```shell
python ./data_processing/rename_file.py
python ./data_processing/clean_s1_s2.py 
```
其次，生成混合音频，且整体只保留5s的音频。    
注：应修改create_mix.py中的type属性。
```shell
python ./data_processing/create_mix.py
```
同时，裁剪原有单人音频，保留和混合音频长度相同的5秒。    
注：应修改cut_s1_s2.py中的文件夹目录。
```shell
python ./data_processing/cut_s1_s2.py
```
最后，为训练集和验证集生成scp文件。
```shell
python ./data_processing/create_scp.py
```

# 3.训练
训练所需的参数均在train.yml，可按需调整。
```shell
python train_rnn.py
```

# 4.测试
以下为单一文件测试，输出后的结果放在test/spk1和test/spk2下。
```shell
python dualrnn_test_wav.py
```
