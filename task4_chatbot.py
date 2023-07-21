from nltk.chat.util import Chat

pairs = [
    [
        r"Hi|Hello|Hey",
        ["Hello User, I am Samin, a Tours and Travel chatbot, made by Pratim Hazra.\nHow are you? ",]
    ],
    [
        r"fine|I'm fine|I'm fine. How are you?",
        ["Good, welcome to our Tours and Travels Services.\nTell me How can I help you?",]
    ],
    [
        r"I want to book a trip",
        ["Great, Choose across India\ni.Rajasthan\nii.Delhi\niii.Uttarakhand\niv.West Bengal\nv.Himachal Pradesh\nvi.Kerala\nvii.Goa\n Choose option number.",]
    ],
[
        r"i|ii|iii|iv|v|vi",
        ["Great Choice. how many members will travel? One-ten",]
    ],
    [
        r"one|two|three|four|five|six|seven|eight|nine|ten",
        ["okay, In which month you want this trip",]
    ],
    [
        r"January|February|March|April|May|June|July|August|September|October|November|December",
        ["Now, Select week no. first-fourth",]
    ],
    [
        r"first|second|third|fourth",
        ["Now, Select Room no. 1-5",]
    ],
    [
        r"1|2|3|4|5",
        ["Our package for per person is 19999/- only including GST.\n The Booking Confirmation and payment link will be sent through text message to your number",]
    ],
    [
        r"Ok|Okay",
        ["Thank You for using Smarttour services with Samin, please visit again, bye take care",]
    ]
]

reflections = {
    "i": "you",
    "i'm": "you are",
    "i am": "you are",
    "i was": "you were",
    "i've": "you have",
    "i'd": "you would",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
print("Start chat with chatbot assisstant")
chat = Chat(pairs, reflections)
chat.converse()
