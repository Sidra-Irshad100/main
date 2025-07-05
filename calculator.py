import streamlit as st
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

st.set_page_config(page_title="Calculator", layout="centered")
st.title("🎉 Calculator by Sidra Irshad 🎉")

if "expression" not in st.session_state:
    st.session_state.expression = ""

st.text_input("Expression", value=st.session_state.expression, key="display", disabled=True)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Button logic
for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            if btn == "C":
                st.session_state.expression = ""
            elif btn == "=":
                st.session_state.expression = str(evaluate_expression(st.session_state.expression))
            else:
                st.session_state.expression += btn

st.markdown("### Result")
st.write(st.session_state.expression)
