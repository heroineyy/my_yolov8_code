from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import ModelCheckpoint
import numpy as np
import random
import sys

# 读取文本数据
with open('text_data.txt', 'r') as f:
    text = f.read()

# 预处理文本数据
text = text.lower()
text = text.replace('\n', ' ')
# ord(i)将当前整数 i 转成对应的 ascii 字符
text = ''.join([i if ord(i) < 128 else '' for i in text])
chars = sorted(list(set(text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))
num_chars = len(text)
num_vocab = len(chars)

# 构建训练数据
seq_length = 100
dataX = []
dataY = []
for i in range(0, num_chars - seq_length, 1):
    seq_in = text[i:i + seq_length]
    seq_out = text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)

# 将训练数据转化为LSTM的输入格式
X = np.reshape(dataX, (n_patterns, seq_length, 1))
X = X / float(num_vocab)
y = np_utils.to_categorical(dataY)

# 定义LSTM模型
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# 定义模型训练的回调函数
filepath = "weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

# 训练模型
model.fit(X, y, epochs=50, batch_size=128, callbacks=callbacks_list)

# 随机生成文本
start_index = random.randint(0, num_chars - seq_length - 1)
for diversity in [0.2, 0.5, 1.0, 1.2]:
    print('\n\n----- diversity:', diversity)

    generated = ''
    sentence = text[start_index:start_index + seq_length]
    generated += sentence
    print('----- Generating with seed: "' + sentence + '"')
    sys.stdout.write(generated)

    for i in range(400):
        x = np.reshape([char_to_int[char] for char in sentence], (1, len(sentence), 1))
        x = x / float(num_vocab)
        prediction = model.predict(x, verbose=0)[0]
        index = np.argmax(prediction)
        result = int_to_char[index]
        generated += result
        sentence = sentence[1:] + result
        sys.stdout.write(result)
        sys.stdout.flush()
    print('\n\n----- Generated text: "' + generated + '"')
