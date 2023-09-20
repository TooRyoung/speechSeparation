import os
import torchaudio
from tqdm import tqdm

# 设置音频文件夹路径
data_dir = 'data'
# split_names = ['train', 'test']
split_names = ['train']

# 遍历每个拆分（train、test）
for split_name in split_names:
    s1_dir = os.path.join(data_dir, split_name, 's1')

    # 获取s1文件夹中所有音频文件的列表
    s1_files = os.listdir(s1_dir)

    # 遍历s1文件夹中的每个音频文件
    for s1_file in tqdm(s1_files, desc=f'Cleaning {split_name}/s1'):
        s1_path = os.path.join(s1_dir, s1_file)

        # 使用torchaudio加载音频文件
        waveform, sample_rate = torchaudio.load(s1_path)

        # 计算音频持续时间（时长），单位为秒
        duration_seconds = waveform.shape[1] / sample_rate

        # 如果音频持续时间小于5秒，则删除s1中对应的文件
        if duration_seconds < 5:
            # 删除s1文件
            os.remove(s1_path)

    s2_dir = os.path.join(data_dir, split_name, 's2')

    # 获取s2文件夹中所有音频文件的列表
    s2_files = os.listdir(s2_dir)

    # 遍历s2文件夹中的每个音频文件
    for s2_file in tqdm(s2_files, desc=f'Cleaning {split_name}/s2'):
        s2_path = os.path.join(s2_dir, s2_file)

        # 使用torchaudio加载音频文件
        waveform, sample_rate = torchaudio.load(s2_path)

        # 计算音频持续时间（时长），单位为秒
        duration_seconds = waveform.shape[1] / sample_rate

        # 如果音频持续时间小于5秒，则删除s2中对应的文件
        if duration_seconds < 5:
            # 删除s2文件
            os.remove(s2_path)


print("Cleaning completed.")