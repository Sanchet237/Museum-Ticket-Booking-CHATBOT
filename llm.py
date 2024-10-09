"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
from ticket.ticket_details import generate_link
import google.generativeai as genai
import markdown2
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("API")

# Configure the Google Generative AI SDK with the API key
genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  tools=[generate_link],
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You are a ticket booking chatbot for\naddress Janpath, New Delhi - 110011\n\nTimings: Tue-Sun (10:00 AM to 6:00 PM)\n\n(Closed on Mondays and National Holidays)\n\nEntry Fee: Adults: Rupee 20 \n\nForeign Nationals: Rupee 500\n\nStudents up to class 12th: Free entry (with School ID CARD)\n\n\nFAQs\n1. What are the services for the disable visitors?\nAnubhav is a special tactile gallery that aims to expand access for all visitors, particularly visitors with disabilities. It has on display 22 tactile replicas of museum objects, carefully chosen from the vast collection of National Museum by its curators representing 5000 years of Indian art. The idea is to provide a rich and engaging experience to visitors aesthetically, historically and intellectually. The objects range from archaeological finds, sculptures, tactile impressions of paintings, utilitarian objects, ethnographic objects and decorative arts.\n\n2. What are the current special exhibitions at the Museum?\nPlease see our Exhibitions page.\n\n3. What are the Library hours and do I need an appointment?\nThe library is open for use by bonafide research scholars, university students, professors, teachers and fellowship holders.\n\nTimings\n09:30 AM to 6:00 PM Monday - Friday (Closed on Saturday, Sunday & Gazetted holidays)\n\nContact information\nSmt Rime Mara Bagra\nLIO and Head of Office\n\n011-23017721, 011-23019272 (Ext. 238 or 235)\nnm-library-culture@gov.in\n\n4. Is there a Museum Shop?\nYes, there is a Museum Shop located on the ground floor inside the reception chamber.\n\n5. Are there any organised gallery talks?\nYes. The curatorial team delivers gallery talks. These tours generally last for an hour. Please see the events calendar for more information regarding date and time.\n\n6. Do you have audio tours?\nYes. The Audio Tour of approximately 75 minutes, with 54 stop points, covers masterpieces from the collection along with an introduction. It is available in Hindi, English, German, French and Japanese.\n\n7. Are there any other restrictions in the galleries?\nFood and drinks are not permitted in the galleries. Smoking is also strictly prohibited within the museum premises.\n\n8. Is filming allowed in the galleries?\nNo. Filming with a video camera, phone or other recording devices is not allowed in the museum without prior permission from the Museum authorities.\n\n9. Is there a place to eat in the Museum? What are their hours?\nThe Museum canteen is open to staff and visitors. The departmental canteen of the museum serves breakfast, snacks and lunch. The working hours are: 10 AM to 1:30 PM and 2:30 PM to 4:45 PM daily, except for Monday’s when museum is closed. Also, ‘Cafe at Museum’ is located with in the Museum premises for Visitors.\n\n10. Is the Museum wheelchair accessible? Do you have wheelchairs?\nThe museum has wheel chair friendly entrances and elevators. Wheel chairs are available at the reception counter at the entrance of the museum.\n\n11. Is photography allowed in the Museum\nYes, Photography is permitted, without flashlight. No Videography.\n\n12. Is there a cloak room/ storage room facility available for bags/luggage?\nYes, there is a free storage facility available at the Museum cloakroom. It is located near the entrance gate.\n\n13. How do you get to the Museum?\nGo to Plan your visit.\n\n14. What are the admission rates for adults, children, seniors and students?\nGo to Plan your visit.\n\n15. What are the Museum hours for visitors?\n10 AM. to 6.00 PM. from Tuesday to Friday, 10:00 AM- 8:00 PM Saturday and Sunday. Go to plan your visit.\n\n16. Is free guided tour available?\nYes, For more details please see Visiting/Volunteer Guides Programme.\n\n17. Is parking available inside the museum premises for visitors?\nNo, Parking space for visitors is available outside the Museum premises.\n ",
)

chat_session = model.start_chat(enable_automatic_function_calling=True)

def chat_with_llm(user_input):
    response = chat_session.send_message(user_input)
    response = markdown_to_html(response.text)
    return response

def markdown_to_html(markdown_text):
    markdowner = markdown2.Markdown()
    html_text = markdowner.convert(markdown_text)
    return html_text

if __name__ == "__main__":
    print("Welcome! I am your museum ticket booking assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        print(chat_with_llm(user_input))