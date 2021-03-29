import streamlit as st
import getFrame


def maxWidth():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

def header():
	st.title("ONTARIO COVID-19 DASHBOARD :mask:")
	st.markdown("---------------------------------------------------")
	col1, col2 = st.beta_columns(2)
	with col1:
		st.markdown(getFrame.recentCasePerDay(), unsafe_allow_html = True)
	with col2:
		st.markdown(getFrame.recentCaseTotal(), unsafe_allow_html = True)
	st.markdown("---------------------------------------------------")
	st.markdown('<h2><i>About </i></h1>', unsafe_allow_html = True)
	st.write("This is a COVID-19 dashboard for the province of Ontario designed in mind to have a simple, usable, and easily understandable user interface.")
	st.write("Refresh page for the most up to date information :repeat_one:")
	st.write("")
	st.write("")

def newCases():
	st.subheader("New COVID-19 Cases By Day ONTARIO")
	col1, col2 = st.beta_columns(2)
	with col1:
		st.line_chart(getFrame.caseByDayGraph())
	with col2:
		st.write(getFrame.caseByDayTableForm())


def totalCases():
	st.subheader("Total COVID-19 Cases By Day ONTARIO")
	col1, col2 = st.beta_columns(2)
	with col1:
		st.area_chart(getFrame.caseTotalGraph())
	with col2:
		st.write(getFrame.caseTotalTableForm())

if __name__ == "__main__":
	maxWidth()
	header()

	col1, col2 = st.beta_columns(2)

	with col1:
		newCasesBtn = st.button("New Cases")

	with col2:
		totalCasesBtn = st.button("Total Cases")

	if newCasesBtn:
		newCases()

	elif totalCasesBtn:
		totalCases()

	else:
		newCases()
