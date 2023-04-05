#!/bin/bash

import openai
import re
import random
from rapnamelist import *
from namegen import *
from ralphlists import *
from ralphprompts import *
from ralphfuncs import * 

def randscene():
    scenariolist = [ralphblog8,ralphblog7,ralph_impeached,ralphblog6,ralphband2,ralphband,ralphblog5,ralphpoem,ralphblog4,ralphblog3,ralphblog2,ralphmovie,ralphtale3,ralphtale2,ralphinherit,product,tarantino,ralphseuss,ralphstein,story2,church2,church,prison,hemingway,shakespeare,summercamp,scenario5,scenario4,scenario3,scenario2,scenario1,ralphintro,ralphrant,ralpheditor]
    return random.choice(scenariolist)

def airesult():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=ralphsteen2,
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

    output = f"{airesult()}\n"
    print(output)

    with open('ralphtexts.txt', 'a') as f:
        f.write(output)
        print("Result written to ralphtexts.txt.")
        f.close()
  
