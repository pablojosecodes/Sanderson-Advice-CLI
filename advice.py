import openai
import json
import sys
import os
import numpy as np
from numpy.linalg import norm

f = open('json/newEmbeddings.json', 'r')
overArchingDct = json.load(f)
f = open('json/segementedTranscripts.json')
promptDct = json.load(f)
f = open('json/Sanderson.json')
Sands = json.load(f)
f = open('json/timestamps.json', 'r')
timestamps = json.load(f)
def getEmbedding(input_string):
    response = openai.Embedding.create(
        input=input_string,
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']
    return embeddings

def cosine_similarity(A, B):
    return np.dot(A,B)/(norm(A)*norm(B))


def getClosestEmbedding(odct, query):
    query = getEmbedding(query)
    
    closest = 0
    closestPairing = (0,0)
    
    for d in odct.keys():
        if str(d).strip() == "0":
            continue
        
        for x in odct[d].keys():
            emb = odct[d][x]
            cosine = cosine_similarity(emb, query)
            if (cosine > closest):
                closest = cosine
                closestPairing = (d, x)


    return closestPairing

def get_video_link(time, nId):
    # print(str(Sands['items'][nId]['snippet']['resourceId']['videoId']))
    link = ("https://www.youtube.com/watch?v=" + str(Sands['items'][nId]['snippet']['resourceId']['videoId'])  + "&t=" + str(time) + "s")
    title = str(Sands['items'][nId]['snippet']['title'])
    iterate = timestamps[str(nId+1)]
    # print(nId)
    # print(iterate)
    ans = "Video"
    for i in iterate:
#         print(i)
        if str(i[0]).strip() == str(time).strip():
            ans = i[1]
            break
    return (link, title, ans)

def get_context(query):
    
    tup = getClosestEmbedding(overArchingDct, query)
    return (promptDct[tup[0]][tup[1]], tup[0], tup[1])

def answer(query):
    ans = get_context(query)
    context = ans[0]
    # print(context)
    links = (get_video_link(int(ans[2]), int(ans[1])))
    
    return (openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are Brandon Sanderson, a famous and extremely helpful author. Repond as him."},
#             {"role": "system", "content": context},
            {"role": "user", "content": query + " Respond in a few full sentences. Use the following context: \""  + context + "\""}
      ]
    ), links)



def main():
    openai.api_key = os.environ['OPENAI_API_KEY']
    theINPUT = input("Ask brandon anything: ")

    response = answer(theINPUT)
    print(response[0]['choices'][0]['message']['content'])


    import webbrowser
    while True:
        action = input("Next steps? (l- open link | n- new question | q- quit)\n> ")
        if action == 'l':
            webbrowser.open(response[1][0])
        else:
            break

    if action == 'n':
        main() # Woohoo- unnecessary recursion
    return 1


if __name__ == "__main__":
    main()

