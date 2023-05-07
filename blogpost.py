# blogpost - holds all the contents of the blogpost and transfers\
# it into a text document with the blog title after complete generation.

# The blogpost content prints dynamically as they are generated

import os
import openai
import sys

#checks if title was given by the user
if (len(sys.argv) != 2):
        print("Please Enter a Title")
else:
        title = sys.argv[1]

print("loading your blogpost on", title, "... ... ...\n")
title = title.upper()
print(title, "\n")
blogpost = title + "\n"

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt="I want to write a blog post about '"+title+"'.\
        Give a list of 5 sections in a numbered bullet point format\
        about this blog post"

synopsis = openai.Completion.create(
        model="text-davinci-003",
        prompt = prompt,
        max_tokens=500,
        temperature=0.7
        )

synopsis = synopsis.choices[0].text
synopsis = synopsis.strip()
lines = synopsis.splitlines()

#writes the individual sections of the blogpost
for section in lines:
    blogpost = blogpost + section.upper()
    print(section.upper(), "\n")

    prompt = "I am writing a blog post with the title '"+title+"'.\n\
             The list of sections of this blog post is the following\n\
             "+synopsis+"\nWrite the section '"+section+"' in a detailed\
             and complete way, in 500 words minimum",
    synopsis = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=750,
            temperature=0.7
            )
    synopsis = synopsis.choices[0].text
    synopsis = synopsis.strip()
    print(synopsis, "\n\n")
    blogpost = blogpost + synopsis + "\n\n"

#writes output to txt file
file = title + ".txt"
with open (file, "w") as f:
    f.write(blogpost)
