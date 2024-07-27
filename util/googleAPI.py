import google.generativeai as genai
from dotenv import load_dotenv
import os
import re

load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key = API_KEY)


def get_safety_settings():
    safety_settings = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]

    return safety_settings

def summarize_text(input_note, input_bulletpoint, input_choose_category, input_age):
    model = genai.GenerativeModel('gemini-pro')
    messages = [
        {'role':'user',
         'parts':[f"""You are a professional note summarizer who summarizes notes based on the users note. The note that the user is providing is {input_note}.
                  
                  You will analyze the text and summarize it so that it is very detailed. However, the level of the response should be 
                  understandable by {input_age} years old. The format of response should be {input_bulletpoint}. Remember to {input_choose_category}"""]
        }
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def generate_story(input_author, input_choose_genre, input_age_level):
    model = genai.GenerativeModel('gemini-pro')
    messages = [
        {'role':'user',
         'parts':[f"""
                  You are a professional story creator who produces stories for famous authors, based on the users story choice. 
                  The author of the story is {input_author}. 
                  You will generate a story, which the genre would be {input_choose_genre}. The comprehensive level of the 
                  story that is generated should be at the age level of {input_age_level}. The duration of the story should be 
                  not too long but not too short, so that the readers can get engaged. Make sure at the top of the story. the authors
                  name of {input_author} is displayed."""]
        }
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text
    

def create_teaching_plan(input_subject, input_student_age, input_duration):
    model = genai.GenerativeModel('gemini-pro')
    messages = [
    {'role':'user',
         'parts':[f"""
                  You are a professional teaching planner who plans lessons/how people should teach to teachers.
                  The teaching planner of the subject you should be planning for is {input_subject}, where the 
                  comprehensivity of the teaching level is determined by the students age, of {input_student_age} years old. 
                  Lastly, the duration of the teaching plan will be {input_duration}, in minutes"""]
        }
    ]
    
    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def generate_website(input_web_description):
    model = genai.GenerativeModel('gemini-pro')
    messages = [
    {'role':'user',
         'parts':[f"""
                  You are a professional web developer who develops websites for programmers, writing in
                  HTML, CSS and JavaScript. The type of website you will make will be determined by 
                  the description that the user provides, which is  {input_web_description}. Once you have 
                  recieved the type of website the user wishes you to create, you will display a series of code, 
                  in order to succesfully create the website. 

                  The output should be in this format:
                  HTML:
                  <HTML Code>

                  CSS:
                  <CSS Code>

                  Javascript:
                  <Javascript Code>                 
                  
                  """]
        }
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def improve_website(input_web_fix, current_code):
    model = genai.GenerativeModel('gemini-pro')
    messages = [
    {'role':'user',
         'parts':[f"""
                  You are a professional web developer who debugs websites for programmers, writing in
                  HTML, CSS and JavaScript. The type of code you will debug/fix will be {current_code}.
                  
                  What should be fixed will be determined by {input_web_fix}. Once you have recieved the 
                  type of website the user wishes you to create, you will display a series of code that is improved and debugged, 
                  in order to succesfully improve the previous website. 

                  The output should be in this format:
                  HTML:
                  <HTML Code>

                  CSS:
                  <CSS Code>

                  Javascript:
                  <Javascript Code>
                  """]
        }
    ]

def generate_estate_plan(input_name, input_choose_house, input_rich_level, input_family_members):
    model = genai.GenerativeModel('gemini-pro')
    messages = [
    {'role':'user',
         'parts':[f"""
                  You are a professional real estate agent who creates house plans for people. First, you should greet the user, 
                  where the users name is {input_name}. Then, you will determine what type of house the user wants, determined
                  by {input_choose_house}. The wealthiness of the user is determined by {input_rich_level}, where
                  you will use your professional judgement to give them a reasonable price for the house they want (the 
                  richer they are, you should give them more options and flexibility). Also, the size of the house could be determined by
                  {input_family_members}, as more family members may require a bigger house."""]
        }
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def image_caption(image, question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    messages = [f"Write a short caption on the image, regarding the question that the user asks: {question}. Make it detailed", image]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text

def image_story(images):
    print(images)
    model = genai.GenerativeModel('gemini-1.5-flash')
    story = [f"Write a story by looking at the images provided. Make the story detailed and entertaining so that users are able to be engaged.", images]
    result = model.generate_content(story, safety_settings = get_safety_settings())
    return result.text
    

def generate_recipe(ingredients, input_time, input_difficulty):
    model = genai.GenerativeModel('gemini-pro')
    messages = [
    {'role':'user',
         'parts':[f"""
                  You don't have to use all ingredients, but you MUST use only the provided ingredients.
                  You are a professional chef who gives out recipes for people with their given ingredients. The user will
                  tell you the ingredients they have by {ingredients}. From this, you will take account of the ingredient
                  that the user has, and generate one food that the user can cook, with their given ingredients. You should
                  choose the food recipe carefully, following the duration that it takes on average to cook the specific
                  food, which is determined by {input_time}, with 1 being shortest, and 10 being largest. The difficulty of the food will be determined by 
                  {input_difficulty}, with 1 being the easiest, and 10 being the hardest.
                  Also make sure that you give out ONE food that the user can cook, with recipies for it. Lastly, make sure to
                  state the name of the food before telling the user the recipe."""]
        }
    ]

    result = model.generate_content(messages, safety_settings = get_safety_settings())
    return result.text


class Chat:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        response = self.chat.send_message("""
                                          YOU MUST GIVE A SINGLE QUESTION RESPONSE
                                          You are a professional medical assistant who tries to diagnose a patient with 
                                          a certain condition, depending on the patients response. Firstly, you should ask a 
                                          single most important question to the patient, so that you can determine how the 
                                          patient is feeling. Afterwards, keep on asking single most important questions
                                          so that you can store the valueable information that the patient is telling you,
                                          in order to diagnose the patient with a condition they have. When you think the 
                                          patient has given you enough points to diagnose them with a condition, you should 
                                          stop asking them questions and diagnose the patient with the condition they have. 

                                          The user might not speak in English. If so, you MUST respond with their language and you have to make it fluent.

                                          Example:
                                          User: I have a strong stomachache
                                          Model: Where exactly in your stomach do you feel the pain?
                                          User: Around the right side next to my belly button
                                          Model: Is the paint constant, or does it come and go?
                                          User: Its constant and hurts a lot
                                          Model: Have you noticed any other symptoms, such as vomiting, fever or changes in your bowel
                                          movements?
                                          User: I vomit from time to time
                                          Model: Based on your symptoms, you should go to the emergency department right now.
                                          Your symptons are: (The symptoms the user stated)
                                          (Your thought on what you think the patient potentially could have)

                                          You are allowed to use medical jargons since this conversation will be viewed by a medical
                                          professional
                                          """, stream=True)
        response.resolve()


class Debater:
    def __init__(self, debate_topic):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.chat = self.model.start_chat(history=[])
        self.history = []
        response = self.chat.send_message(f"""You are a professional debator, who debates other individuals. You MUST agree with the 
                                          debating topic. Your response MUST be less than 100 words.The topic that you will be debating
                                          about will be {debate_topic}, where your response should be less than 100 words, to outpoint the opponent in terms of 
                                          debating, so that you will win.""", stream=True)
        response.resolve()
        self.evaluator = genai.GenerativeModel('gemini-1.5-flash')
        self.evaluation = self.evaluator.start_chat(history=[])
        resposne = self.evaluation.send_message(f""" You are a judge that evaluates a debate. You MUST be objective, and solely
                                                decide upon the two arguments. You will be receiving a history of debate.

                                                Your output should be the win rate that you would expect if this conversation was 
                                                made at a real court, as well as detailed reasoning.
                                                
                                                For example:

                                                Result:
                                                User : 70%
                                                Model : 30%

                                                <Detailed, logical reaonsing of why you evaluated as such>
                                                """)
        response.resolve()
    
    def generate_chat(self, debate_topic):
        self.history.append({"role": "user", "message": debate_topic})
        response = self.chat.send_message(debate_topic, stream=True)
        response.resolve()
        clean_response = self.clean_text(response.text)
        self.history.append({"role": "model", "message": clean_response})
        return self.format_history()
    
    def evaluate(self):
        response = self.evaluation.send_message(self.format_history())
        return response.text

    def clean_text(self, text):
        # Remove special tags like <ctrl100>
        clean_text = re.sub(r'<.*?>', '', text)
        return clean_text

    def format_history(self):
        formatted_history = ""
        for entry in self.history:
            if entry["role"] == "user":
                formatted_history += f"User: {entry['message']}\n\n"
            elif entry["role"] == "model":
                formatted_history += f"Model: {entry['message']}\n\n"
        return formatted_history.strip()
    

class ChatBot:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        self.history = []
        initial_message = """
            You are a friend of the user. The user will ask questions and you will answer them, just like
            friends talking to each other. You can also ask questions according to the user's answer.
        """
        response = self.chat.send_message(initial_message, stream=True)
        response.resolve()

    def generate_chat(self, text_input):
        self.history.append({"role": "user", "message": text_input})
        response = self.chat.send_message(text_input, stream=True)
        response.resolve()
        clean_response = self.clean_text(response.text)
        self.history.append({"role": "model", "message": clean_response})
        return self.format_history()

    def clean_text(self, text):
        # Remove special tags like <ctrl100>
        clean_text = re.sub(r'<.*?>', '', text)
        return clean_text

    def format_history(self):
        formatted_history = ""
        for entry in self.history:
            if entry["role"] == "user":
                formatted_history += f"User: {entry['message']}\n\n"
            elif entry["role"] == "model":
                formatted_history += f"Model: {entry['message']}\n\n"
        return formatted_history.strip()
    