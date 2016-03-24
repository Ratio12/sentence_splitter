# 句子以 . ? !作为分隔
# 1. . + 空格 + lowercase 不算
# 2. . + 数字 中间无空格  不算
# 3. . + 空格 + uppercase 之前跟上Mr Mrs Dr 等不算
# 4. . + 字母 不算
# 5. . + 符号 如,  more 不算

import string


def sentence_split(file_path):
    sentences = []
    # chr(32)*10 在结尾处补上十个空格 避免循环到最后一个句号时溢出
    f = open(file_path).read() + chr(32) * 10
    length = len(f)
    # enumerate() 遍历序列中的元素与下标
    for i, char in enumerate(f):
        if (i + 2) < length:
            if char == '.' or char == '?' or char == '!':
                if f[i + 1] == chr(32) and f[i + 2].islower():
                    continue
                if f[i + 1].isdigit():
                    continue
                if f[i - 2] + f[i - 1] in ['Mr', 'Mrs', 'Dr', 'Jr']:
                    continue
                if f[i + 1].isalpha():
                    continue
                if f[i + 1] in string.punctuation:
                    continue

                if not sentences == []:
                    # 将连接sentences中所有元素
                    tmp = "".join(sentences)
                    # 截取所要的部分
                    cut = f[:i + 1].replace(tmp, "")
                    sentences.append(cut)
                else:
                    sentences.append(f[:i + 1])

    # 清除左右两边的空格
    # bonus
    return [i.strip(" ") for i in sentences]
    pass


def test_splitter():
    sentences = sentence_split(file_path)
    assert sentences == ['Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.',
                         'Did he mind?', "Adam Jones Jr. thinks he didn't.", "In any case, this isn't true...",
                         "Well, with a probability of .9 it isn't."], \
        "The split sentences don't match the expected output."
    print("Congrats, your sentence splitter seems to work perfectly!")


# you may change this line to locate your text file
file_path = r"sample text.txt"
write_to_path = r"sampleTest.txt"


# 在程序目录下新建一个文本文件，将整理后的句子写入该文件
def write(file_path, write_to_path):
    sentences = sentence_split(file_path)
    new_file = open(write_to_path, 'w')
    for i, mes in enumerate(sentences):
        new = str(i + 1) + '.' + chr(32) + mes + '\n'
        new_file.writelines(new)


"""
The test_splitter function, when called, shouldn't raise any AssertionError
"""
test_splitter()
write(file_path, write_to_path)
