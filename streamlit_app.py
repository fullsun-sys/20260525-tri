import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="일차함수 그래프 탐구", layout="wide")

st.title("📈 일차함수 그래프의 모형 변화")
st.markdown(
    "학생이 직접 `a`와 `b`를 바꾸며 `y = ax + b` 그래프가 어떻게 변하는지 관찰할 수 있는 앱입니다."
)

n_points = 200

with st.sidebar:
    st.header("변수 조절")
    a = st.slider("기울기 a", min_value=-5.0, max_value=5.0, value=1.0, step=0.1, format="%.1f")
    b = st.slider("절편 b", min_value=-10.0, max_value=10.0, value=0.0, step=0.5, format="%.1f")
    x_min = st.slider("x 최소값", min_value=-10, max_value=0, value=-5)
    x_max = st.slider("x 최대값", min_value=1, max_value=10, value=5)

    st.divider()
    st.subheader("관찰 포인트")
    st.write("- `a`가 커지면 그래프가 더 가파르게 올라갑니다.")
    st.write("- `a`가 작아지면 그래프가 완만해지고, 음수이면 내려갑니다.")
    st.write("- `b`가 커지면 그래프가 위로 평행 이동합니다.")
    st.write("- `b`가 작아지면 그래프가 아래로 평행 이동합니다.")

x = np.linspace(x_min, x_max, n_points)
y = a * x + b

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color="#2563eb", linewidth=2.5)
ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
ax.axvline(0, color="gray", linewidth=0.8, linestyle="--")
ax.grid(True, linestyle=":", alpha=0.4)
ax.set_title(f"y = {a:.1f}x + {b:.1f}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(x_min, x_max)

# 그래프의 기준선과 주요 점 표시
ax.scatter([0], [b], color="#dc2626", zorder=3, label=f"(0, {b:.1f})")
ax.legend(loc="upper left")

col1, col2 = st.columns([2, 1])
with col1:
    st.pyplot(fig)

with col2:
    st.subheader("함수 정보")
    st.metric("기울기 a", f"{a:.1f}")
    st.metric("절편 b", f"{b:.1f}")
    st.info(
        f"현재 그래프의 식은 **y = {a:.1f}x + {b:.1f}** 입니다."
    )

    st.subheader("직관적 설명")
    st.write(
        "기울기 `a`는 그래프의 기울기를 정하고, 절편 `b`는 y축과 만나는 위치를 정합니다."
    )

st.divider()

st.subheader("비교 관찰")
compare_col1, compare_col2, compare_col3 = st.columns(3)

with compare_col1:
    st.write("기본 그래프")
    base_fig, base_ax = plt.subplots(figsize=(4, 3))
    base_ax.plot(x, y, color="#2563eb", linewidth=2.0)
    base_ax.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    base_ax.axvline(0, color="gray", linewidth=0.8, linestyle="--")
    base_ax.grid(True, linestyle=":", alpha=0.4)
    base_ax.set_title("현재 그래프")
    st.pyplot(base_fig)

with compare_col2:
    st.write("a를 1 증가시킨 경우")
    comp_fig1, comp_ax1 = plt.subplots(figsize=(4, 3))
    comp_ax1.plot(x, (a + 1) * x + b, color="#16a34a", linewidth=2.0)
    comp_ax1.plot(x, y, color="#2563eb", linewidth=1.5, alpha=0.5)
    comp_ax1.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    comp_ax1.axvline(0, color="gray", linewidth=0.8, linestyle="--")
    comp_ax1.grid(True, linestyle=":", alpha=0.4)
    comp_ax1.set_title("기울기 변화")
    st.pyplot(comp_fig1)

with compare_col3:
    st.write("b를 1 증가시킨 경우")
    comp_fig2, comp_ax2 = plt.subplots(figsize=(4, 3))
    comp_ax2.plot(x, a * x + (b + 1), color="#f59e0b", linewidth=2.0)
    comp_ax2.plot(x, y, color="#2563eb", linewidth=1.5, alpha=0.5)
    comp_ax2.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    comp_ax2.axvline(0, color="gray", linewidth=0.8, linestyle="--")
    comp_ax2.grid(True, linestyle=":", alpha=0.4)
    comp_ax2.set_title("절편 변화")
    st.pyplot(comp_fig2)

st.caption("이 앱은 학생이 직접 값을 조절해 그래프의 변화를 체험하도록 설계되었습니다.")
