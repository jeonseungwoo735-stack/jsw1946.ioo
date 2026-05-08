import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1.
# 데이터 로드 (경로가 맞다는 가정 하에)
df_a = pd.read_json(r'C:\Users\KDT21\Desktop\김기석 강사님\과제\heart_failure_a.json')
df_b = pd.read_json(r'C:\Users\KDT21\Desktop\김기석 강사님\과제\heart_failure_b.json')
df = pd.merge(df_a, df_b, on='person_id', how='inner')

st.title('박출계수 / 나이')
# st.write('이 플롯은 박출계수와 나이의 관계를 사망 여부(DEATH_EVENT)별로 색상을 구분하여 보여줍니다.')

# sns.jointplot은 JointGrid 객체를 반환하므로 .fig를 통해 Figure를 추출해야 합니다.
g = sns.jointplot(data=df, x='ejection_fraction', y='age', hue='DEATH_EVENT')

# 핵심: g.fig를 st.pyplot()에 전달
st.pyplot(g.fig)
# =============================================================================================================

# 2. 
st.title('흡연 여부에 따른 혈소판 수치 분석')

# --- [요구사항 구현: 라디오 버튼] ---
# 사용자에게 선택지를 제공합니다.
choice = st.radio(
    "확인하고 싶은 그룹을 선택하세요:",
    ('전체', '흡연자(1)', '비흡연자(0)')
)

# 선택한 값에 따라 데이터를 필터링합니다.
if choice == '흡연자(1)':
    filtered_df = df[df['smoking'] == 1]
elif choice == '비흡연자(0)':
    filtered_df = df[df['smoking'] == 0]
else:
    filtered_df = df

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))

# 사진 속 코드와 동일하게 설정:
# x='DEATH_EVENT', y='platelets', hue='smoking', split=True
sns.violinplot(data=filtered_df, x='DEATH_EVENT', y='platelets', hue='smoking', split=True, ax=ax)

# 그래프 출력
st.pyplot(fig)
# =============================================================================================================

# 3.
st.title('심부전 데이터 시간별 분포 분석')


st.subheader('시간(time)에 따른 사망 사건(DEATH_EVENT) 분포')

# 도화지 생성
fig, ax = plt.subplots(figsize=(10, 6))

# 사용자님이 작성하신 코드 옵션 및 사진의 시각적 형태 반영
# x='time', bins=20, hue='DEATH_EVENT'
sns.histplot(
    data=df, 
    x='time', 
    bins=20, 
    hue='DEATH_EVENT', 
    multiple="stack", # 사진처럼 0과 1이 쌓여서 보이도록 설정
    ax=ax
)

# 그래프 레이블 설정 (사진과 동일하게)
ax.set_xlabel('time')
ax.set_ylabel('Count')

# Streamlit에 그래프 표시
st.pyplot(fig)