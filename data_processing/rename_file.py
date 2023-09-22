import os

# 指定音频文件所在的文件夹路径
folders1_path = '../data/tr/s1'
folders2_path = '../data/tr/s2'

# 获取文件夹中所有的音频文件
audios1_files = [f for f in os.listdir(folders1_path) if f.endswith('.wav')]
audios2_files = [f for f in os.listdir(folders2_path) if f.endswith('.wav')]

# 设置计数器，从1开始
counter = 1

# 循环遍历音频文件并重命名
for audio_file in audios1_files:
    # 构建新的文件名
    new_file_name = f'{counter:03d}s1.wav'

    # 构建完整的文件路径
    old_file_path = os.path.join(folders1_path, audio_file)
    new_file_path = os.path.join(folders1_path, new_file_name)

    # 重命名文件
    os.rename(old_file_path, new_file_path)

    # 增加计数器
    counter += 1

# 设置计数器，从1开始
counter = 1

# 循环遍历音频文件并重命名
for audio_file in audios2_files:
    # 构建新的文件名
    new_file_name = f'{counter:03d}s2.wav'

    # 构建完整的文件路径
    old_file_path = os.path.join(folders2_path, audio_file)
    new_file_path = os.path.join(folders2_path, new_file_name)

    # 重命名文件
    os.rename(old_file_path, new_file_path)

    # 增加计数器
    counter += 1
print("重命名完成！")