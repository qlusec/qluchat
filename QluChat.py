import os
import openai
import requests
import json
import re

class QluChat:

   def __init__(self):
        self.userinput = self.get_valid_domain()
        self.ai_api = os.environ.get('AI_API')
        self.vt_api = os.environ.get('VT_API')
    
   def get_valid_domain(self):
        while True:
            user_input = input("Insert the domain you would like analyzed (format: example.com):\n")
            # Use a regular expression to check if the input matches the expected format
            if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', user_input):
                return user_input
            else:
                print("Invalid domain format. Please enter a valid domain.")
    

   def ThreatIntel(self):
        

        url = "https://www.virustotal.com/api/v3/domains/" + self.userinput

        headers = {
            "accept": "application/json",
            "x-apikey": f"{self.vt_api}"
        }

        self.response = requests.get(url, headers=headers)
        data = self.response.json()

        last_analysis_results = data.get("data", {}).get("attributes", {}).get("last_analysis_results", {})
        last_analysis_stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        total_votes = data.get("data", {}).get("attributes", {}).get("total_votes", 0)
        id = data.get("data", {}).get("id", "")
        type = data.get("data", {}).get("type", "")

        # Create a dictionary to hold all the data
        self.virustotal_data = {
            "last_analysis_results": last_analysis_results,
            "last_analysis_stats": last_analysis_stats,
            "total_votes": total_votes,
            "id": id,
            "type": type
        }

         # Convert the VirusTotal data dictionary to a formatted string
        formatted_virustotal_data = json.dumps(self.virustotal_data, indent=2)
    
         # Store the formatted VirusTotal data as an attribute
        self.formatted_virustotal_data = formatted_virustotal_data

    
   def ChatBot(self):

            formatted_virustotal_data = json.dumps(self.virustotal_data, indent=2)

            user_message = f"VirusTotal data:\n{self.formatted_virustotal_data}\n\n"
            user_message += "ChatGPT, analyze this data and give me easily digestible summary. If theres no data say that you don't have enough and try later"
 
            # Define the OpenAI API endpoint
            url = "https://api.openai.com/v1/chat/completions"  
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant on Cybersecurity matters only."},
                    {"role": "user", "content": user_message}
                ]
              } 
            headers = {
                "Authorization": f"Bearer {self.ai_api}",
                "Content-Type": "application/json"
              } 
            
            response = requests.post(url, json=data, headers=headers)
            response_json = response.json()
            
            if 'choices' in response_json:
                generated_text = response_json['choices'][0]['message']['content']
                print(generated_text)  # Print only the generated text
            else:
                print("Response does not contain 'choices'")


    


def main():
    # Create instance of QluChat class that will ask for user input of a domain to be passed to ThreatIntel function
    qluchat_instance = QluChat()
    # Run Threat Intel function on the domain provided gathering domain reputation data from VT API and pass it to ChatBot function
    qluchat_instance.ThreatIntel()
    # Ingest VT API threat intel data into the ChatBot for analysis to provide user
    qluchat_instance.ChatBot()
    


    
if __name__ == "__main__":
    main()
        
