import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("糖水浓度预测")

# 初始化 session_state 中的列表
if 'x_list' not in st.session_state:
    st.session_state.x_list = []
if 'y_list' not in st.session_state:
    st.session_state.y_list = []

# 输入
x_input = st.number_input("入射偏振角度(°)", step=0.1, key="x_input")
y_input = st.number_input("第一个暗点出现位置(cm)", step=0.1, key="y_input")

# 写入数据
if st.button("写入数据"):
    st.session_state.x_list.append(x_input)
    st.session_state.y_list.append(y_input)
    st.success(f"已添加：({x_input}, {y_input})")
if st.button("写入推荐数据"):
    st.session_state.x_list.append(0),st.session_state.x_list.append(28.6),st.session_state.x_list.append(61.19),st.session_state.x_list.append(90),st.session_state.x_list.append(104.04),st.session_state.x_list.append(118.44)
    st.session_state.y_list.append(17),st.session_state.y_list.append(27.5),st.session_state.y_list.append(33),st.session_state.y_list.append(44),st.session_state.y_list.append(51),st.session_state.y_list.append(55)
    st.success(f"已添加：({x_input}, {y_input})")
# 显示当前数据
if st.session_state.x_list:
    st.markdown(f"**当前角度数据：** {st.session_state.x_list}")
    st.markdown(f"**当前光程数据：** {st.session_state.y_list}")

# 计算拟合
if st.button("计算拟合"):
    if len(st.session_state.x_list) < 2:
        st.warning("请至少输入两个点")
    else:
        xs = np.array(st.session_state.x_list)
        ys = np.array(st.session_state.y_list)
        a, b = np.polyfit(xs, ys, 1)
        c = (1 / abs(a)) * 10 / 78.543
        td = (-0.9909 + np.sqrt((0.9909**2 + 1.96 * c))) / 0.0098

        st.markdown(f"**拟合公式：** y = {a:.4f}x + {b:.4f}")
        st.markdown(f"**浓度：** {round(c, 5)} g/mL")
        st.markdown(f"**糖度：** {round(td, 3)} Brix")

        # 画图
        fig, ax = plt.subplots()
        ax.scatter(xs, ys)
        ax.plot(xs, a * xs + b, color="red")
        st.pyplot(fig)
