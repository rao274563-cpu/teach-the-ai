\# 🤖 Teach the AI



\*\*Teach the AI\*\* is an interactive learning experience that helps students learn Machine Learning by \*\*teaching an AI student instead of simply answering questions\*\*.



\## 💡 Idea



Traditional AI tutoring gives students explanations and answers.



Teach the AI reverses the interaction:



\*\*AI Student → Student teaches → AI challenges → Reasoning evaluated → Mastery updated → Next challenge adapted\*\*



The goal is to make the student explain concepts in their own words, reveal misconceptions, and demonstrate understanding.



\## 🎯 Learning Path



The prototype currently focuses on four Machine Learning concepts:



1\. \*\*Overfitting\*\*

2\. \*\*Features vs Labels\*\*

3\. \*\*Training vs Testing\*\*

4\. \*\*Model Evaluation\*\*



The system uses different misconceptions and challenges for each concept.



\## 🔄 How It Works



\### 1. AI Student presents a misconception



For example:



> "My model has 99% training accuracy, so it must be a very good model."



\### 2. Student teaches the AI



The student explains why the AI student's statement may or may not be correct.



\### 3. AI Student responds



Gemini generates a short response and asks a follow-up question or challenges the student's reasoning.



\### 4. Reasoning is evaluated



The student's explanation is evaluated on:



\* Concept Understanding

\* Reasoning Quality

\* Generalization



\### 5. Learner Model updates mastery



The three scores are combined into a simple mastery score.



The learner is classified as:



\* \*\*Needs Guidance:\*\* below 50

\* \*\*Developing:\*\* 50–74

\* \*\*Proficient:\*\* 75–89

\* \*\*Mastered:\*\* 90+



\### 6. Adaptation Engine selects the next challenge



The next challenge depends on the learner's mastery.



When mastery reaches 90+, the system moves the learner to the next concept.



\## 🧠 Why This Is Different



The student is not rewarded simply for selecting the correct answer.



Instead, the student must \*\*explain, reason, defend, and generalize\*\* their understanding.



This turns AI from an answer generator into an environment where the learner actively demonstrates understanding.



\## 🛠️ Technology



\* Python

\* Streamlit

\* Google Gemini API

\* `google-genai`

\* python-dotenv



\## 📁 Project Structure



```text

teach-the-ai/

│

├── app.py

├── ai\_student.py

├── reasoning.py

├── learner\_model.py

├── adaptation.py

├── requirements.txt

├── .gitignore

└── README.md

```



\### File Responsibilities



\*\*app.py\*\*

Main Streamlit application and learning loop.



\*\*ai\_student.py\*\*

Controls the AI student's behavior and misconceptions.



\*\*reasoning.py\*\*

Analyzes the student's explanation using Gemini.



\*\*learner\_model.py\*\*

Stores attempts, calculates mastery, and determines the learner level.



\*\*adaptation.py\*\*

Selects the next challenge based on mastery and concept.



\## 🚀 Run Locally



\### 1. Clone the repository



```bash

git clone https://github.com/rao274563-cpu/teach-the-ai.git

cd teach-the-ai

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



Activate it on Windows:



```powershell

.venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure the Gemini API key



Create a `.env` file:



```text

GEMINI\_API\_KEY=your\_api\_key\_here

```



Never commit the API key to GitHub.



\### 5. Run the application



```bash

streamlit run app.py

```



\## 🌐 Deployment



The application can be deployed using Streamlit Community Cloud.



For deployment, add `GEMINI\_API\_KEY` through the application's \*\*Secrets\*\* settings rather than committing the `.env` file.



\## 🎓 Hackathon Concept



Teach the AI explores a simple question:



> \*\*What changes when the student has to teach the AI instead of the AI simply teaching the student?\*\*



The prototype focuses deeply on one subject—Machine Learning—and uses active explanation, reasoning evaluation, learner modeling, and adaptive challenges to create a more student-centered learning experience.



