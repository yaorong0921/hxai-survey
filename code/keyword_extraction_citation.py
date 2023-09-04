import json
import copy
import openai
import os
import ast
openai.organization = "org-2Ed3ng726m9hGEL5cd6e5Kvr"
openai.api_key = os.getenv("OPENAI_API_KEY")



##### for citation
### Open json file
with open('./citation_dict_temp3.json') as f:
    citation_dict = json.load(f)

citation_dict_temp = copy.deepcopy(citation_dict)

keyword_embeddings = []
label_group = []
count = 0
## read from dict and save key words
for count, (k, v_list) in enumerate(citation_dict_temp.items()):
    for v in v_list:
        if 'abstract' in v:
            # print(k, v['title'])
            paper_info = 'Paper Title: %s; Abstract: %s.'%(v['title'], v['abstract'])

            request = ' Please just output an answer with a json file, such as {\'keywords\':[], \'research type\':[], \'methodology\':[],...} (no more other words)' #' Please answer with one word or phrase.'

            prompt =  paper_info + ' Please provide 5 keywords for this paper. Then, please categorize this academic paper in research type (Empirical, theoretical, review, meta-analysis or case study), methodology (Quantitative, qualitative or mixed-methods), purposes (Exploratory, descriptive, explanatory, or prescriptive), discipline (Biology, physics, economics, computer science, sociology... or others), content (Application, methodological, or technical) and application area (please answer with one word or phrase).' + request
            message = [{"role": "user", "content": prompt}]
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=100,
            temperature=1.2,
            messages = message)
            try:
                json_line = ast.literal_eval(response['choices'][0]['message']['content'])
                # print(json_line)
                v['keywords'] = json_line #response['choices'][0]['message']['content']
                # prompt = 'Paper Title: %s; Abstract: %s. Can you give a key word of the application area of this paper?'%(v['title'], v['abstract'])
                # message = [{"role": "user", "content": prompt}]

                # response = openai.ChatCompletion.create(
                # model="gpt-4",
                # max_tokens=100,
                # temperature=1.2,
                # messages = message)

                # print(response['choices'][0]['message']['content'])
                # v['application'] = response['choices'][0]['message']['content']
    #             #candidates = [keyword[0] for keyword in keywords]
    #             # k_embedding = np.asarray([sentence_model.encode(keyword[0]) for keyword in keywords])
    #             # k_embedding = k_embedding.mean(axis=0)

    #             # ### save the key word embeddings
    #             # k_embedding = sentence_model.encode(keywords[1][0])
    #             # keyword_embeddings.append(k_embedding)        
                # ## save the dict with key words
                with open("citation_dict_keyword.json", "w") as outfile:
                    json.dump(citation_dict_temp, outfile)
            except:
                print('Wrong with: '+ k)

    # print(k)
# ## save the dict with key words
with open("citation_dict_keyword.json", "w") as outfile:
    json.dump(citation_dict_temp, outfile)