from utils import configs
import torch
from evaluate import load_model_tokenizer, translate
from train import read_data
import re
def test_trans(sentence):
# Translate a sentence
    # sentence = "My family is very poor, I had to go through hard life when I was young, now I have a better life."
    print("--- English input sentence:", sentence)
    print("--- Translating...")
    device = torch.device(configs["device"])
    model, source_tokenizer, target_tokenizer = load_model_tokenizer(configs)
    trans_sen = translate(
        model=model, 
        sentence=sentence, 
        source_tokenizer=source_tokenizer, 
        target_tokenizer=target_tokenizer, 
        target_max_seq_len=configs["target_max_seq_len"], 
        beam_size=configs["beam_size"], 
        device=device
    )
    print("--- Sentences translated into Vietnamese:", trans_sen)
    return trans_sen

# Translate a sentence
def get_data():
    valid_src_data, valid_trg_data = read_data(configs["valid_source_data"], configs["valid_target_data"])
    nees=[]
    for dat in valid_src_data:
        if len(dat.split())>= configs["source_max_seq_len"]:
            nee=' '.join(dat.split()[0:128])
            # print(len(nee.split()))
        else:
            nee=dat
        nees.append(nee)
    return nees
if __name__=='__main__':
    
    device = torch.device(configs["device"])
    model, source_tokenizer, target_tokenizer = load_model_tokenizer(configs)

    rel=[]
    nees=get_data()
    for i in range(len(nees[0:10])):   
        sentence = nees[i]
        
        # seq = re.sub(
        # r"[\*\"“”\n\\…\+\-\/\=\(\)‘•:\[\]\|’\!;]", " ", str(sentence))
        # seq = re.sub(r"[ ]+", " ", seq)
        # seq = re.sub(r"\!+", "!", seq)
        # seq = re.sub(r"\,+", ",", seq)
        # seq = re.sub(r"\?+", "?", seq)
        # seq = seq.lower()
        
        trans_rel=test_trans(sentence)
        rel.append(trans_rel)
    with open('result_sub_trans.txt','w',encoding='utf-8')as f:
        for j in range(len(rel)):
            f.write(rel[i]+'\n')
    # print("--- Sentences translated into Vietnamese:", trans_sen)