#!/bin/bash

import openai
import re
import random
from rapnamelist import rapname
from namegen import full_name
import ralphlists
import ralphprompts
from ralphfuncs import * 

def randscene():
    scenariolist = [ralphblog8,ralphblog7,ralph_impeached,ralphblog6,ralphband2,ralphband,ralphblog5,ralphpoem,ralphblog4,ralphblog3,ralphblog2,ralphmovie,ralphtale3,ralphtale2,ralphinherit,product,tarantino,ralphseuss,ralphstein,story2,church2,church,prison,hemingway,shakespeare,summercamp,scenario5,scenario4,scenario3,scenario2,scenario1,ralphintro,ralphrant,ralpheditor,wallyralph,ralphbeating]
    return random.choice(scenariolist)

def airesult(name):
    if name == 'rand':
        prompt = f"{instruct} {randscene()}"
    elif name == 'album':
        prompt = f"{instruct} create the title for an album.  The name of the album will be drawn from the following text: {randscene()}.  Only return the name of the album."
    elif name == 'blogtitle':
        prompt = f"{instruct} As Ralph, I want you to create title for a blog post based on the following scenario: {randscene()}.  The response will be only up to 8 words long."
    else:
        prompt = f"{instruct} {name}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2000,
            n=3,
            stop=None,
            temperature=0.8, 
        )

        result = response.choices[0].text
        result_lines = result.split("\n")[1:]
        result_without_first_line = "\n".join(result_lines)
        return result_without_first_line
    
if __name__ == "__main__":

    # output = f"{airesult()}\n"
    print(title_creator())
    print(airesult(ralphband2))

    # with open('ralphtexts.txt', 'a') as f:
    #     f.write(output)
    #     print("Result written to ralphtexts.txt.")
    #     f.close()
  
