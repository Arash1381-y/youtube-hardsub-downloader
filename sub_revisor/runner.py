import openai
import json

API_KEY = "sk-***"
SYSTEM_MSG = "Help me as a translator assistant. I will give you a subtitle in english and its persian translation. I want you to revise the persian translation, revise and rewrite it"
# SYSTEM_MSG2
openai.api_key = API_KEY
MODEL_NAME = "gpt-3.5-turbo"


def tokenize():
    pass


def get_file_content(filename):
    content = None
    with open(filename, "r") as f:
        content = f.read()

    return content


def revise(original_filename, translation_filename):
    orig_file_content = get_file_content(original_filename)
    trans_file_content = get_file_content(translation_filename)
    org_lst = orig_file_content.split("\n\n")
    trans_lst = trans_file_content.split("\n\n")


    english_sub = "Here is all the english subtitle to check translations with: " + orig_file_content
    
    #discussions = [{"role": "system", "content": SYSTEM_MSG}, {"role": "system", "content" : english_sub}]
    discussions = [{"role": "system", "content": SYSTEM_MSG}]


    ai_translation = []
    index = 0
    while True:
        str1 = "Here is the part of subtitle in English: \n"
        english_sub_part = org_lst[index]
        str2 = "\nHere is persian part of subtitle: \n"
        persian_sub_part = trans_lst[index]
        index += 1
        quiestion = "\nplease revise the persian translation and check it is true\n"
        msg = str1 + english_sub_part + str2 + persian_sub_part + quiestion
        discussions.append({"role": "user", "content": msg})

        completion = openai.chat.completions.create(
            model=MODEL_NAME, messages=discussions
        )

        x = json.loads(str(completion))
        response = x["choices"][0]["message"]["content"]

        ai_translation.append(response)
        discussions.append({"role": "assistant", "content": response})

        print("\nAI says: ", response, "\n")


def run():
    revise("sub_revisor/out_org.srt", "sub_revisor/out.srt")


run()
