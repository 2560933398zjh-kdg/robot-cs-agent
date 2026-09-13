import time

import streamlit as st
from agent.react_agent import ReactAgent

# 标题
st.title("智扫通机器人智能客服")
st.divider() #分隔符

if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()    #st.session_state 是 Streamlit 的会话状态字典，用于在多次页面重绘（rerun）之间保持数据

if "message" not in st.session_state:
    st.session_state["message"] = []    #message：存储整个对话历史，格式为 [{"role": "user"/"assistant", "content": "..."}]

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 用户输入提示词
prompt = st.chat_input()  #Streamlit 提供的聊天输入组件，返回用户输入的字符串

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    response_messages = []
    with st.spinner("智能客服思考中..."):
        res_stream = st.session_state["agent"].execute_stream(prompt)

        def capture(generator, cache_list):

            for chunk in generator:
                cache_list.append(chunk) # 将每个chunk存入缓存列表

                for char in chunk:
                    time.sleep(0.01) # 人为延迟，模拟打字效果
                    yield char  # 逐字符输出

        st.chat_message("assistant").write_stream(capture(res_stream, response_messages))
        st.session_state["message"].append({"role": "assistant", "content": response_messages[-1]})
        st.rerun() # 强制刷新页面，显示最新消息
