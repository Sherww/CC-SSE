from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
from keras.models import Sequential
from keras.utils import np_utils 
import keras
import numpy as np 


tokenizer = Tokenizer()

def dataset_preparation(data):

	# basic cleanup
    corpus = data.lower().split("\n")

	# tokenization	
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1

	# create input sequences using list of tokens
    input_sequences = []
    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        input_sequences.append(token_list)

	# pad sequences 
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

	# create predictors and label
    predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
    label = np_utils.to_categorical(label, num_classes=total_words)

    return predictors, label, max_sequence_len, total_words

def create_model(predictors, label, max_sequence_len, total_words):
	print('train model...')
	model = Sequential()
    # add input embedding layer
	model.add(Embedding(total_words, 10, input_length=max_sequence_len-1))
    #add hidden layer
	model.add(LSTM(150, return_sequences = True))
	model.add(Dropout(0.2))
	model.add(LSTM(128))
    # output layer
	model.add(Dense(total_words, activation='softmax'))

	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	earlystop = EarlyStopping(monitor='loss', min_delta=0, patience=25, verbose=1, mode='auto')
	model.fit(predictors, label,batch_size=32, epochs=150, verbose=1, callbacks=[earlystop],validation_split=0.1)
	print( model.summary())
	return model 

def generate_text(seed_text, next_words, max_sequence_len):
	for _ in range(next_words):
		token_list = tokenizer.texts_to_sequences([seed_text])[0]
		token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
		predicted = model.predict_classes(token_list, verbose=1)
		
		output_word = ""
		for word, index in tokenizer.word_index.items():
			if index == predicted:
				output_word = word
				break
		seed_text += " " + output_word
	return seed_text


if __name__=='__main__':
    
    data = open('train_sub_lstm_final.txt',encoding='utf-8').read()
    # dataset_preparation(data)
    predictors, label, max_sequence_len, total_words = dataset_preparation(data)
    model = create_model(predictors, label, max_sequence_len, total_words)
    model.save('model_lstm_sub.h5')
    model = keras.models.load_model('model_lstm_sub.h5')   
    with open('test_sub_input_final.txt','r',encoding='utf-8')as f:
    	result=[]
    	data=f.readlines()
    	for dat in data:
    		b=generate_text(dat,1,max_sequence_len)
    		result.append(b)
    with open('result_sub.txt','w',encoding='utf-8')as ff:
    	for data in result:
    		ff.write(str(data.replace('\n',''))+'\n')