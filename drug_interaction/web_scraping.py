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

# ##explanatino of the code 
# .1 Library Imports
# python
# Copy code
# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# Explanation:
# * Streamlit: A library used to create simple web applications in Python. Here, it helps in building an interactive UI where users can input drug names and view the results.
# * Requests: This is a Python HTTP library used for sending HTTP requests. In this case, it fetches the HTML content of the Drugs.com page.
# * BeautifulSoup: Part of the bs4 module, it is used for parsing and scraping HTML or XML documents. It helps extract and navigate the information needed for drug interactions from the fetched HTML.

# 2. Scrape Drug Interactions Function
# python
# Copy code
# def scrape_drug_interactions(drug_name):
# Explanation:
# * Purpose: This function is responsible for scraping the drug interaction data from the Drugs.com website for a particular drug.
# * Input: It takes a drug_name as an argument, which represents the name of the medication entered by the user.

# 3. Construct URL and Request the Page
# python
# Copy code
# url = f"https://www.drugs.com/drug_interactions.html?drugs={drug_name}"
# response = requests.get(url)
# Explanation:
# * URL Construction: The drug name entered by the user is dynamically appended to the base URL https://www.drugs.com/drug_interactions.html?drugs=, making a request for interaction information on that specific drug.
# * requests.get(url): Sends an HTTP request to the constructed URL and stores the response in the responsevariable.

# 4. Check Response Status Code
# python
# Copy code
# if response.status_code != 200:
#     return {"Error": f"Failed to retrieve data (Status code: {response.status_code})."}
# Explanation:
# * Purpose: After making the HTTP request, we check the status code to ensure that the request was successful.
# * Status Code 200: Indicates success. If it's not 200, the function returns an error message stating the failure to retrieve the data and provides the status code.

# 5. Parse HTML Using BeautifulSoup
# python
# Copy code
# soup = BeautifulSoup(response.text, 'html.parser')
# Explanation:
# * HTML Parsing: Once the page is fetched, we convert the HTML content into a BeautifulSoup object using html.parser as the parsing engine. This allows us to navigate and extract specific data from the HTML structure.

# 6. Initialize Interactions Dictionary
# python
# Copy code
# interactions = {}
# Explanation:
# * Purpose: This dictionary will store the interaction details, including interaction titles, descriptions, and severity, which will be scraped from the page.

# 7. Locate Interaction Section
# python
# Copy code
# interaction_section = soup.find("div", class_="page-section-interactions")
# Explanation:
# * Finding the Section: The find method searches the HTML document for the first div tag with the class "page-section-interactions", which (according to the website structure) contains the drug interaction information.
# * Error Handling: If this section is not found, it means there are no interaction details available for the specified drug.

# 8. Display the HTML Structure for Debugging
# python
# Copy code
# st.write(interaction_section.prettify())  # View the entire interaction section.
# Explanation:
# * Debugging: This line is added to display the parsed HTML content of the interaction section in a well-structured (pretty) format. This helps visualize what the HTML looks like for understanding how the data is structured on the page.

# 9. Extract Interaction Details
# python
# Copy code
# interaction_list = interaction_section.find_all("div", class_="interaction-list")
# Explanation:
# * Find All Interactions: Once we have the interaction section, the code searches for multiple div elements with the class "interaction-list", where each div represents a specific interaction. The assumption is that the website uses this class name for grouping the interaction details.

# 10. Loop Through Interactions
# python
# Copy code
# for interaction in interaction_list:
#     interaction_title = interaction.find("h4")  # Example title tag
#     interaction_detail = interaction.find("p")  # Example detail tag
#     severity = interaction.find("span", class_="severity")  # Example severity tag
# Explanation:
# * Looping Through Data: For each interaction in the interaction_list, the code extracts three key pieces of information:
#     * Title: Found inside an h4 tag, which contains the drug or interaction name.
#     * Details: Found inside a p (paragraph) tag, which contains the description of the interaction.
#     * Severity: Optionally found inside a span tag with the class "severity". This contains the severity level of the interaction (e.g., mild, moderate, severe).

# 11. Store Interaction Information
# python
# Copy code
# if interaction_title and interaction_detail:
#     title = interaction_title.text.strip()
#     details = interaction_detail.text.strip()
#     severity_text = severity.text.strip() if severity else "Unknown severity"

#     interactions[title] = {
#         "details": details,
#         "severity": severity_text
#     }
# Explanation:
# * If Found: If both the title and detail for an interaction are found, they are extracted and stripped of unnecessary whitespace.
# * Default Severity: If the severity is not found, it's set to "Unknown severity".
# * Store in Dictionary: The interaction title, details, and severity are stored in the interactions dictionary under the drug's name.

# 12. Error Handling
# python
# Copy code
# except Exception as e:
#     st.error(f"Error during scraping: {e}")
# Explanation:
# * Exception Handling: If any error occurs during the scraping process (e.g., changes to the HTML structure or network issues), the error is displayed in the Streamlit app using st.error(), and the user is informed.

# 13. Main Function
# python
# Copy code
# def main():
#     st.title("Drug Interaction Checker")
#     drug_names = st.text_input("Enter medication names (comma-separated):")
# Explanation:
# * App Title: This sets the title of the Streamlit app as "Drug Interaction Checker".
# * Text Input: The user is prompted to enter multiple medication names in a text box, separated by commas.

# 14. Check Interactions Button
# python
# Copy code
# if st.button("Check Interactions"):
# Explanation:
# * Button Interaction: When the user clicks the Check Interactions button, the app triggers the drug interaction checking process. This is where the action of scraping begins.

# 15. Process Each Drug
# python
# Copy code
# drug_list = [name.strip() for name in drug_names.split(',') if name.strip()]
# all_interactions = {}
# Explanation:
# * Split and Clean Drug Names: The user input (comma-separated drug names) is split into a list. Any extra whitespace around the names is removed using strip(), and empty entries are filtered out.
# * Prepare to Store All Results: all_interactions is an empty dictionary used to store the interaction data for all entered drugs.

# 16. Loop Through Drugs and Scrape Interactions
# python
# Copy code
# for drug in drug_list:
#     interactions = scrape_drug_interactions(drug)
#     if interactions:
#         all_interactions[drug] = interactions
# Explanation:
# * For Each Drug: For each drug in the user-provided list, the code calls scrape_drug_interactions() to get its interaction details.
# * Store Interactions: If interactions are found, they are stored in the all_interactions dictionary under the drug's name.

# 17. Display Results
# python
# Copy code
# st.write("### Interaction Results")
# Explanation:
# * Results Section: This creates a section to display the interaction results once the scraping is complete.

# 18. Display Interactions for Each Drug
# python
# Copy code
# if all_interactions:
#     for drug, interaction_data in all_interactions.items():
#         st.write(f"**Interactions for {drug}:**")
#         if "Error" in interaction_data:
#             st.write(interaction_data["Error"])
#         else:
#             for interaction, data in interaction_data.items():
#                 st.write(f"- **{interaction}**: {data['details']} (Severity: {data['severity']})")
# Explanation:
# * Iterate and Display: The app loops through each drug and its associated interactions, displaying them in a readable format. Errors (if any) are shown in case the scraping fails or there are no interactions.
# * Format: Interaction titles are displayed in bold, followed by the details and severity level.

# 19. Reset Button
# python
# Copy code
# if st.button("Reset"):
#     st.rerun()
# Explanation:
# * Reset Functionality: If the user clicks Reset, the Streamlit app is rerun (reloaded), clearing the inputs and resetting the UI.

# 20. Run the App
# python
# Copy code
# if __name__ == "__main__":
#     main()
# Explanation:
# * Main Entry Point: When the script is run directly (not imported), it calls the main() function to start the Streamlit app.

# Use Case Summary:
# * Objective: This app allows users to input one or more medication names and checks for possible drug interactions using data scraped from Drugs.com.
# * Interaction: The app displays the interaction details and severity in a user-friendly format.
