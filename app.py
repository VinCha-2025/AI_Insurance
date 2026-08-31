import streamlit as st
import requests


st.set_page_config(
    page_title="AI Insurance Claim Approval",
    page_icon="🏥",
    layout="centered"
)


st.title("🏥 AI Health Insurance Claim Approval")
st.write(
    "Submit a health insurance claim for automated "
    "AI-assisted evaluation."
)


st.divider()


# Claim inputs

age = st.number_input(
    "Patient Age",
    min_value=1,
    max_value=120,
    value=45
)


diagnosis = st.text_input(
    "Diagnosis",
    placeholder="Example: Appendicitis"
)


procedure = st.text_input(
    "Medical Procedure",
    placeholder="Example: Appendectomy"
)


claim_amount = st.number_input(
    "Claim Amount (₹)",
    min_value=0.0,
    value=80000.0,
    step=1000.0
)


st.divider()


if st.button(
    "🔍 Evaluate Claim",
    type="primary"
):

    if not diagnosis or not procedure:

        st.warning(
            "Please enter both diagnosis and procedure."
        )

    else:

        claim = {
            "age": age,
            "diagnosis": diagnosis,
            "procedure": procedure,
            "claim_amount": claim_amount
        }

        try:

            response = requests.post(
                "http://127.0.0.1:8000/claims",
                json=claim,
                timeout=120
            )

            if response.status_code == 200:

                result = response.json()

                st.subheader("Claim Result")

                decision = result["decision"]["decision"]

                if decision == "APPROVED":

                    st.success(
                        f"Decision: {decision}"
                    )

                elif decision == "MANUAL REVIEW":

                    st.warning(
                        f"Decision: {decision}"
                    )

                else:

                    st.error(
                        f"Decision: {decision}"
                    )


                st.subheader("AI Explanation")

                st.info(
                    result["explanation"]
                )


                st.subheader(
                    "Rule Engine Reason"
                )

                st.write(
                    result["decision"]["reason"]
                )


                st.subheader(
                    "Retrieved Policy Evidence"
                )

                for evidence in result[
                    "policy_evidence"
                ]:

                    with st.expander(
                        "Policy Evidence"
                    ):

                        st.write(
                            evidence["text"]
                        )

                        st.caption(
                            "FAISS distance: "
                            + str(
                                round(
                                    evidence["distance"],
                                    4
                                )
                            )
                        )

            else:

                st.error(
                    "Backend returned an error."
                )

                st.write(response.text)

        except requests.exceptions.RequestException:

            st.error(
                "Could not connect to the FastAPI backend. "
                "Make sure FastAPI is running."
            )