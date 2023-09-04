import json
import copy
import openai
import os
import ast

openai.organization = "org-2Ed3ng726m9hGEL5cd6e5Kvr"
openai.api_key = os.getenv("OPENAI_API_KEY")

##### for references
### Open json file
with open('./reference_dict_keyword.json') as f:
    reference_dict = json.load(f)

reference_dict_temp = copy.deepcopy(reference_dict)

keyword_embeddings = []
label_group = []

## read from dict and save key words
for k, v in reference_dict_temp.items():
    if int(k) < 814: 
        continue
    if 'abstract' in v:
        paper_info = 'Paper Title: %s; Abstract: %s.'%(v['title'], v['abstract'])

        request = ' Please just output an answer with a json file, such as {\'keywords\':[], \'research type\':[], \'methodology\':[],...} (no more other words)' #' Please answer with one word or phrase.'

        prompt =  paper_info + ' Please provide 5 keywords for this paper. Then, please categorize this academic paper in research type (Empirical, theoretical, review, meta-analysis or case study), methodology (Quantitative, qualitative or mixed-methods), purposes (Exploratory, descriptive, explanatory, or prescriptive), discipline (Biology, physics, economics, computer science, sociology... or others), content (Application, methodological, or technical) and application area (please answer with one word or phrase).' + request
        message = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=1.2,
        messages = message)
        json_line = ast.literal_eval(response['choices'][0]['message']['content'])
        print(json_line)
        v['keywords'] = json_line #response['choices'][0]['message']['content']

        # prompt = paper_info + ' This paper belongs to which category? Empirical, theoretical, review, meta-analysis or case study?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['type'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])
        
        # prompt = paper_info + ' This paper belongs to which category? Quantitative, qualitative or mixed-methods?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['methodology'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])

        # prompt = paper_info + ' This paper belongs to which category? Exploratory, descriptive, explanatory, or prescriptive?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['purpose'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])     


        # prompt = paper_info + ' This paper belongs to which category? Biology, physics, economics, computer science, sociology... or others?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['field'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])     


        # prompt = paper_info + ' This paper belongs to which category? Positivist, interpretiist, or critical?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['paradigm'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])  

        # prompt = paper_info + ' This paper belongs to which category? Application, methodological, or technical?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['subject'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])

        # prompt = paper_info + ' This paper belongs to which category? Cross-sectional, longitudinal?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['scope'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])


        # prompt = paper_info + ' This paper belongs to which category? Broad overview or Deep Dive?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['depth'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])

        # prompt = paper_info + ' This paper belongs to which category? Confirmatory, or exploratory?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['conclusion'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])

        # prompt = paper_info + ' This paper belongs to which category? Cutting-edge or foundational?' + request
        # message = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(
        # model="gpt-4",
        # max_tokens=100,
        # temperature=1.2,
        # messages = message)
        # v['novelty'] = response['choices'][0]['message']['content']  
        # # print(response['choices'][0]['message']['content'])
        # ## save the dict with key words
        with open("reference_dict_keyword2.json", "w") as outfile:
            json.dump(reference_dict_temp, outfile)
    print(k)
## save the dict with key words
with open("reference_dict_keyword2.json", "w") as outfile:
    json.dump(reference_dict_temp, outfile)

# # Opening JSON file
# for i, s in enumerate(['trust', 'simulatability', 'fairness', 'transparency', 'others']):
#     types_of_encoding = ["utf8"] #"cp1252"
#     for encoding_type in types_of_encoding:
#         with codecs.open('abstract_%s.json'%s, encoding = encoding_type, errors ='replace') as file_json:
#             # returns JSON object as 
#             # a dictionary
#             abstract_dict = json.load(file_json)
#             # Closing file
#             file_json.close()
#             # print(citation_dict)
#             # print(pub_not_found)
#             for k,v in abstract_dict.items():
#                 print(k)
#                 keywords = kw_model.extract_keywords(v['abstract'], top_n=10, keyphrase_ngram_range=(1, 1))
#                 v['keywords'] = keywords
#                 #candidates = [keyword[0] for keyword in keywords]
#                 # k_embedding = np.asarray([sentence_model.encode(keyword[0]) for keyword in keywords])
#                 # k_embedding = k_embedding.mean(axis=0)
#                 k_embedding = sentence_model.encode(keywords[1][0])
#                 #print(keywords_embedding.shape)
#                 keyword_embeddings.append(k_embedding)
#                 label_group.append(i)

# ##### for citation
# ### Open json file
# with open('./citation_dict_temp3.json') as f:
#     citation_dict = json.load(f)

# citation_dict_temp = copy.deepcopy(citation_dict)

# keyword_embeddings = []
# label_group = []

# ## read from dict and save key words
# for k,v_list in citation_dict_temp.items():
#     for v in v_list:
#         if 'abstract' in v:
#             # print(k, v['title'])

#             prompt = 'Paper Title: %s; Abstract: %s. Can you give a key word of the application area of this paper?'%(v['title'], v['abstract'])
#             message = [{"role": "user", "content": prompt}]

#             response = openai.ChatCompletion.create(
#             model="gpt-4",
#             max_tokens=100,
#             temperature=1.2,
#             messages = message)

#             print(response['choices'][0]['message']['content'])
#             v['application'] = response
# #             #candidates = [keyword[0] for keyword in keywords]
# #             # k_embedding = np.asarray([sentence_model.encode(keyword[0]) for keyword in keywords])
# #             # k_embedding = k_embedding.mean(axis=0)

# #             # ### save the key word embeddings
# #             # k_embedding = sentence_model.encode(keywords[1][0])
# #             # keyword_embeddings.append(k_embedding)        

# # ## save the dict with key words
# with open("citation_dict_keyword.json", "w") as outfile:
#     json.dump(citation_dict_temp, outfile)