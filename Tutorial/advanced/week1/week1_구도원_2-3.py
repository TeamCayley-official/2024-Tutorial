#절대 경로와 상대 경로 

import pandas as pd
pd.read_csv("파일경로", encoding="cp949")

from glob import glob
#유닉스 스타일의 경로 패턴을 확장 가능함. glob을 사용해서.
file_name = golb("data/*")[0]
#상대경로, 첫번째 파일.

#여러 파일을 한 번에 로드하는 방법
glob("data/store/(여기에 일치하는글자 뭘 넣어도됨)*.csv")

glob("*_*_*.csv")

file_list= []
for file_csv_name in file_csv:
    print(file_csv_name)
    #파일하나
    temp = pd.read_csv(file_csv_name, low_memory=False)
    file_list.append(temp)

df = pd.concat(file_list)
df.shape

len(file_list)




