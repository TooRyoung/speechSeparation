import os
import torchaudio
import torch

# 设置截取后的目标长度（以采样点为单位，5秒*采样率）
desired_length_seconds = 5

# 输入文件夹路径和输出文件夹路径
input_folder_s1 = 'data\\tr\\s1'
input_folder_s2 = 'data\\tr\\s2'
output_folder_s1 = 'data\\tr\\s1_trimmed'
output_folder_s2 = 'data\\tr\\s2_trimmed'

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder_s1, exist_ok=True)
os.makedirs(output_folder_s2, exist_ok=True)

# 获取输入文件夹中的所有音频文件
s1_files = [os.path.join(input_folder_s1, fname) for fname in os.listdir(input_folder_s1) if fname.endswith('.wav')]
s2_files = [os.path.join(input_folder_s2, fname) for fname in os.listdir(input_folder_s2) if fname.endswith('.wav')]

# 遍历 s1 文件夹中的音频文件
for s1_file in s1_files:
    # 读取音频文件
    waveform, sample_rate = torchaudio.load(s1_file)
    desired_length_samples = desired_length_seconds * sample_rate
    # 截取到指定的长度
    trimmed_waveform = waveform[:, :desired_length_samples]

    # 获取原始文件名
    filename = os.path.basename(s1_file)

    # 构建输出文件路径
    output_file = os.path.join(output_folder_s1, filename)

    # 保存截取后的音频文件（保持原有的采样率）
    torchaudio.save(output_file, trimmed_waveform, sample_rate)

# 遍历 s2 文件夹中的音频文件（与上述代码类似，只需更改输入和输出文件夹路径）
for s2_file in s2_files:
    waveform, sample_rate = torchaudio.load(s2_file)
    desired_length_samples = desired_length_seconds * sample_rate
    trimmed_waveform = waveform[:, :desired_length_samples]
    filename = os.path.basename(s2_file)
    output_file = os.path.join(output_folder_s2, filename)
    torchaudio.save(output_file, trimmed_waveform, sample_rate)

print("音频文件截取完成。")