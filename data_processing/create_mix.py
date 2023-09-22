import os
import torchaudio

# 定义文件夹路径
data_folder = "..\\data"
type = 'tr'

# 分别获取s1和s2文件夹下的音频文件列表
s1_folder = os.path.join(data_folder, type, "s1")
s2_folder = os.path.join(data_folder, type, "s2")
s1_files = sorted([os.path.join(s1_folder, fname) for fname in os.listdir(s1_folder) if fname.endswith(".wav")])
s2_files = sorted([os.path.join(s2_folder, fname) for fname in os.listdir(s2_folder) if fname.endswith(".wav")])

# 确保s1和s2文件数量相同
if len(s1_files) != len(s2_files):
    print("Number of files in s1 and s2 folders should be the same.")
else:
    # 创建输出文件夹
    output_folder = os.path.join(data_folder, type, "mix")
    os.makedirs(output_folder, exist_ok=True)

    # 循环遍历音频文件并进行融合和保存
    for i in range(len(s1_files)):
        # 读取选定的音频文件
        s1_waveform, s1_st = torchaudio.load(s1_files[i])
        s2_waveform, s2_st = torchaudio.load(s2_files[i])
        # if s1_st != s2_st:
        #     print(f"Skipping files {os.path.basename(s1_files[i])} and {os.path.basename(s2_files[i])}. They do not have the same sample rate.")
        #     continue
        # else:
        #     print("s1:"+str(len(s1_waveform[0]))+" "+str(s1_st))
        #     print("s2:"+str(len(s2_waveform[0]))+" "+str(s2_st))
        # 确保两段音频都至少有5秒以上的长度
        desired_length = 5 * s1_st  # 5秒的长度（采样率为s1_st或s2_st）
        if len(s1_waveform[0]) < desired_length or len(s2_waveform[0]) < desired_length:
            print(f"Skipping files {os.path.basename(s1_files[i])} and {os.path.basename(s2_files[i])}. They should be at least 5 seconds long.")
        else:
            # 将两段音频进行叠加
            mixed_waveform = s1_waveform[:, :desired_length] + s2_waveform[:, :desired_length]

            # 构建输出文件名
            file_prefix = f"{i+1:03d}"
            output_file = os.path.join(output_folder, f"{file_prefix}mix.wav")

            # 保存叠加后的音频文件
            torchaudio.save(output_file, mixed_waveform, s1_st)

            print(f"Mixed audio saved to: {output_file}")