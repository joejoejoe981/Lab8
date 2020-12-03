import pandas as pd  # as 別名 (簡化名稱)

# 建立 資料框 DataFrame
df = pd.read_csv("students.csv")  # 讀取 CSV 轉換成 DataFrame
print(type(df))
print(df)
print('------------------ copy() ------------------')
df2 = df.copy()  # 複製新 DataFrame
print(df2)
print('------------------ head() ------------------')
df3 = df.head(n=3)  # 複製 df 最前3筆到新 DataFrame
print(df3)
print('------------------ tail() ------------------')
df4 = df.tail(n=3)  # 複製 df 最後3筆到新 DataFrame
print(df4)
print('------------------ info() ------------------')
df.info()  # 顯示 DataFrame 結構資訊
print('------------------ describe() ------------------')
df5 = df.describe()  # 建立目前 DataFrame 統計數據，複製到新DataFrame
print(df5)
print('------------------ shape ------------------')
print(df.shape)
列數, 欄數 = df.shape
print('列數', 列數, '欄數', 欄數)
print('------------------ columns ------------------')
print(df.columns)
for 欄名 in df.columns:
    print(欄名)
print('------------------ index ------------------')
print(df.index)
for i in df.index:
    print(i)
print('------------------ sort_values() ------------------')
df6 = df.sort_values(by=['eng'])  # 以 eng 排序，複製到新 DataFrame
print(df6)
print('------------------ Series 序列 ------------------')
s1 = df['eng'] < 70  # 建立 eng < 70 的序列資料
# s1 = (df['eng'] < 70) | (df['math'] < 70) # | 或
# s1 = (df['eng'] > 90) & (df['math'] > 90) # & 且
print(type(s1))
print('建立 s1 序列資料： eng < 70')
print(s1)
print('------------------ df7 ------------------')
print('根據 s1 篩出資料: eng < 70')
df7 = df[s1]  # 篩選符合 s1 ，複製到新 DataFrame
print('原始資料如下')
print(df)
print('篩出資料如下')
print(df7)  # 篩出資料
print("------------------ df['eng']  ------------------")
print('產生 s2 序列資料: 所有 eng 資料')
s2 = df['eng']
print(s2)
print('------------------ min max sum mean q  ------------------')
print('min', s2.min())
print('max', s2.max())
print('sum', s2.sum())
print('mean', s2.mean())
print('q1', s2.quantile(q=0.25))
print('q2', s2.quantile(q=0.5))   # 中位數
print('q3', s2.quantile(q=0.75))
print('------------------ 排序 Series ------------------')
s3 = s2.sort_values(ascending=True)  # 排序由低到高
print(s3)
print("------------------ df[['eng','math']]  ------------------")
print('挑選 eng , math 欄位 產生新 DataFrame')
df8 = df[['eng','math']]
print(df8)