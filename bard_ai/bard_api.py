from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "agi7ZvmbjT2F0sv1a1PX5yxGBovbvM5N0tk17UjmQ_NvshF0ESafk-lylIGQQrBfmqVywg.",
    "__Secure-1PSIDTS": "sidts-CjIBSAxbGY_oblWyT6ec2nhub0DP2-pRaN03XnSSkhvROD8tqQPLzoLs7kkDARDcJuZP6RAA",
    "__Secure-1PSIDCC": "APoG2W9Cti31gXCZO8zSGXfdH0IG8NdSx3xqC20fnV3w7wD3lCasJwr4s8kgwsGIArGEQOqOFVV2"
}

bard = BardCookies(cookie_dict=cookie_dict)

context = "My name is Umesh Kumar. I finished my graduation in 2023 in Masters in Data Science program at" \
          " Indiana University Bloomington. I finished my undergraduation sever years earlier than graduation year. "

questions = "1. What is my name? \n 2. From which university did I graduate? \n " \
            "3. In which year I finished my undergraduate?"

print(bard.get_answer("Answer the following questions based on context given." + context + questions)['content'])
# print(bard.get_answer('Recommend me a movie')['content'])
