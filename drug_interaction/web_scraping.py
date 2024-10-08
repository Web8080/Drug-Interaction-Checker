import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_drug_interactions(drug_name):
    # Construct the URL for the specific drug's interaction page
    url = f"https://www.drugs.com/drug_interactions.html?drugs={drug_name}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        return {"Error": f"Failed to retrieve data (Status code: {response.status_code})."}

    soup = BeautifulSoup(response.text, 'html.parser')

    interactions = {}

    try:
        # Locate the section containing interactions
        interaction_section = soup.find("div", class_="page-section-interactions")

        if not interaction_section:
            return {"Error": "No interactions section found for this medication."}

        # Display the HTML structure for debugging
        st.write(interaction_section.prettify())  # View the entire interaction section.

        # Find the interaction details based on the structure you observed
        interaction_list = interaction_section.find_all("div", class_="interaction-list")  # Adjust this class name based on actual HTML structure

        if not interaction_list:
            return {"Error": "No interaction details found."}

        # Loop through each interaction entry found
        for interaction in interaction_list:
            # Update these selectors based on actual HTML content
            interaction_title = interaction.find("h4")  # Example title tag
            interaction_detail = interaction.find("p")  # Example detail tag
            severity = interaction.find("span", class_="severity")  # Example severity tag

            if interaction_title and interaction_detail:
                title = interaction_title.text.strip()
                details = interaction_detail.text.strip()
                severity_text = severity.text.strip() if severity else "Unknown severity"

                interactions[title] = {
                    "details": details,
                    "severity": severity_text
                }
            else:
                st.warning("Interaction title or details not found in this section.")

    except Exception as e:
        st.error(f"Error during scraping: {e}")

    return interactions

def main():
    st.title("Drug Interaction Checker")
    drug_names = st.text_input("Enter medication names (comma-separated):")

    if st.button("Check Interactions"):
        drug_list = [name.strip() for name in drug_names.split(',') if name.strip()]  # Avoid empty names
        all_interactions = {}

        for drug in drug_list:
            interactions = scrape_drug_interactions(drug)
            if interactions:
                all_interactions[drug] = interactions

        st.write("### Interaction Results")
        if all_interactions:
            for drug, interaction_data in all_interactions.items():
                st.write(f"**Interactions for {drug}:**")
                if "Error" in interaction_data:
                    st.write(interaction_data["Error"])
                else:
                    for interaction, data in interaction_data.items():
                        st.write(f"- **{interaction}**: {data['details']} (Severity: {data['severity']})")
        else:
            st.write("No interactions found.")

    if st.button("Reset"):
        st.rerun()

if __name__ == "__main__":
    main()
