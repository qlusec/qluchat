# QluChat: A Cybersecurity Chatbot for Threat Intelligence Analysis
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/-Python-000?&logo=Python)
________________________________________________________________________
## Table of Contents

- **[Overview](#overview)**
- **[Key Features](#key_features)**
- **[Dependencies](#dependencies)**
- **[Installation](#installation)**
- **[Configuration](#configuration)**
- **[Usage](#usage)**
- **[License](#license)**
- **[Acknowledgements](#acknowledgements)**
- **[Contributions](#contributions)**
________________________________________________________________________
## Overview

QluChat is a command-line tool written in Python. The tool's purpose is to give Cybersecurity researchers and professionals, especially beginners an easily digestible insight into threat intelligence data. The goal of the Chatbot is to enhance threat intelligence analysis by using artificial intelligence to provide quick, comprehensible summaries of raw data for users using VirusTotal and OpenAI APIs.
___
## Key Features

**VirusTotal API**: QluChat integrates the VirusTotal API domain endpoint in order to retrieve data from various Cybersecurity engines on whether the user-specified domain entered for analysis is malicious or safe.

**OpenAI GPT-3.5 Turbo API**: The data gathered from VirusTotal's API is ingested into OpenAI's GPT-3.5 Turbo model, where natural language processing is utilized to analyze the data providing insights and summaries into the domain.
___
## Dependencies
- **requests**: Used for making HTTP requests to the VirusTotal and OpenAI APIs.
```python
pip install requests # It can also be pip3 instead of pip depending on your system
```
___
## Installation

1. Clone the repository
```bash
git clone https://github.com/qlusec/qluchat.git
```
___ 
## Configuration 

1. For enhanced security, set your API keys as environment variables using your terminal. Replace "APIKEYHERE" with your actual API keys from VirusTotal and OpenAI. 
```bash
export VT_API=APIKEYHERE
export AI_API=APIKEYHERE
```

___
## Usage

1. Run the script
```python
python QluChat.py # It can also be python3 instead of python depending on your system
```
2. Input the domain you want to analyze when prompted
3. QluChat will fetch threat intelligence data from VirusTotal and engage GPT-3.5 Turbo to provide insights and summaries.
___
## License

This project is licensed under the MIT License 
___
## Acknowledgements

QluChat was developed by **Javon Strachan** as a personal project.
___________
## Contributions

Contributions to this project are welcome! Feel free to submit pull requests or open issues if you encounter any problems or have ideas for improvements.
_______________________________
_Disclaimer: This project is for educational and personal use only. It should not be used for any malicious or unethical activities. Always respect the terms of service and policies of the APIs and services used._

