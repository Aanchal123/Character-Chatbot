# Character-Chatbot
A chatbot is a type of AI software, developed for the purpose of simulating a conversation with the user. They converse in natural language via messaging applications, websites, or any other form of communication platform. 

Some chatbots use extensive word-classification processes, Natural Language processors, and sophisticated AI, while others simply scan for general keywords and generate responses using common phrases obtained from an associated library or database. 

In this project, I have developed a model where the user can create a chatbot specific to a character. The user will be able to interact with the chatbot by giving it a few personality traits and the chatbot will be able to hold a conversation accordingly. If a personality is not specified then the chatbot has been given a default character - ‘Joey’ from the T.V show ‘Friends’. 

It was made possible by using Simple Transformers Model along with the pre-trained model provided by Hugging Face. This includes the training dataset for various personality traits; but for giving the chatbot a unique default character, I trained the model and fine-tuned it to a dataset we created ourselves in the same JSON format from every episode’s script of the show. 

Lastly I used Tkinter package to build the GUI for the chatbot and connected it the trained model and the chatbot was ready to chat.
