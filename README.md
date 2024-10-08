# Drug-Interaction-Checker
A simple web application to check drug interactions using data scraped from Drugs.com. This tool uses Streamlit for the frontend and BeautifulSoup for web scraping.


## Features

Enter Multiple Drugs: Input multiple drug names (comma-separated) to check for interactions.
Interaction Details: Provides details of interactions including severity (if available).
Web Scraping: Uses BeautifulSoup to scrape interaction data from Drugs.com.
Interactive Interface: Built with Streamlit to provide an easy-to-use interface.
Error Handling: Notifies users if any issues occur during scraping or if no interactions are found.


##Technologies Used

Python: The core language for the backend and scraping logic.
Streamlit: A fast way to build and share data apps in Python.
BeautifulSoup: A Python library for pulling data out of HTML and XML files.
Requests: A simple HTTP library to make web requests.


###Requirements

To run this app, ensure you have the following installed:

Python 3.8+
pip
Python Packages
You can install the required packages by running:

bash
Copy code
pip install -r requirements.txt
Where requirements.txt contains:

txt
Copy code
streamlit
beautifulsoup4
requests


##How to Run

##Clone the repository:
bash
Copy code
git clone https://github.com/web8080/drug-interaction-checker.git

##Navigate to the project directory:
bash
Copy code
cd drug-interaction-checker


## Install the dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:
bash
Copy code
streamlit run code.py
The app will start locally, and you can access it in your browser at:
arduino
Copy code
http://localhost:8501
Usage

Enter one or more medication names, separated by commas, in the input field.

Click Check Interactions to fetch drug interactions from Drugs.com.
View the interaction details, including severity, if available.
Click Reset to clear the input and search again.


#Example

Interaction Results for Ciprofloxacin and Amoxicillin:
 less
Copy code
Interactions for Ciprofloxacin:
- Increased risk of side effects when taken with Amoxicillin. (Severity: Moderate)

Interactions for Amoxicillin:
- Interaction with Ciprofloxacin can increase toxicity. (Severity: Major)
Error Handling

Failed Scraping: If the app cannot retrieve data from the website (e.g., network issues or changes in the website structure), it will return a message indicating the error.

No Interactions Found: If no interactions are found, the app will notify the user that there were no interactions for the entered drug(s).


#Contributing

Contributions are welcome! Please follow the steps below:

Fork the repository.
Create a new branch.
Make your changes and test them.
Submit a pull request.


#License
