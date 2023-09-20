import os
from tqdm import tqdm
import torchaudio


dirs = "dev-clean"
for dir_path in os.listdir(dirs):   # dirs = 'dev-clean'  dir_path = '174'  files_path = 'dev-clean\\174' files = ['50561',...]  file = '50561'
    files_path = os.path.join(dirs, dir_path)
    files = os.listdir(files_path)
    for file in tqdm(files, desc=f'Cleaning '):
        least_file_path = os.path.join(files_path, file)
        for s1 in os.listdir(least_file_path):
            s1_path = os.path.join(least_file_path, s1)
            if s1_path.endswith("txt"):
                os.remove(s1_path)
                continue
            elif s1_path.endswith(".flac"):

                # 使用torchaudio加载音频文件
                waveform, sample_rate = torchaudio.load(s1_path)

                # 计算音频持续时间（时长），单位为秒
                duration_seconds = waveform.shape[1] / sample_rate
                new_file_path = s1_path[:-4] + "wav"
                os.rename(s1_path, new_file_path)
                # 如果音频持续时间小于5秒，则删除s1中对应的文件
                if duration_seconds < 5:
                    # 删除s1文件
                    os.remove(new_file_path)
            else:
                print(s1_path)
