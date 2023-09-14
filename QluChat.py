import os
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
            # Use a regular expression to validate user input
            if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', user_input):
                return user_input
            else:
                print("Invalid domain format. Please enter a valid domain.")
    

   def DomThreatIntel(self):
        
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
                self.generated_text = response_json['choices'][0]['message']['content']
                print(self.generated_text)  # Print only the generated text
            else:
                print("Response does not contain 'choices'")
    



def main():
     while True:
             menu_choice = input("Press the number corresponding with your choice\n1) Analyze a domain\n2) Exit\n")
             if menu_choice == "1":
                  qluchat = QluChat()
                  qluchat.DomThreatIntel()
                  qluchat.ChatBot()
             elif menu_choice == "2":
                  print("Thank you for using QluChat!")
                  break
             else:
                  print("Invalid input, try again!")
    


    
if __name__ == "__main__":
    main()
        
