import pandas as pd
df=pd.read_csv('data/employee_performance.csv')
print(df.info())

mean_satisfy=df['고객만족도'].mean()
df['고객만족도']=df['고객만족도'].fillna(mean_satisfy)
print(df.isnull().sum())

df=df.dropna(subset=['근속연수']) #오직 근속연수 열에 값이 비어있는 행만 삭제
print(df.isnull().sum()) #누락된 만큼 하나씩 빠짐

print(df['고객만족도'].quantile(0.75))

print(df.groupby['부서'].mean().sort_values(ascending=False))



