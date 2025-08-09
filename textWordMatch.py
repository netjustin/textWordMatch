from collections import Counter
# 2 sample text files picked because of their presence in OOB Windows 11 installation. They match on 11 words, 9 of which are unique.
path_file1 = 'C:\\Windows\\SysWOW64\\Drivers\\gmreadme.txt'
path_file2 = 'C:\\Windows\\SysWOW64\\WindowsPowerShell\\v1.0\\en-US\\default.help.txt'
def overlapping_word_count(str1,str2):
    words1=str1.split()
    words2=str2.split()
    overlap = Counter(words1) & Counter(words2)
    return sum(overlap.values())
def overlapping_word_count_unique(str1,str2):
    words1=set(str1.split())
    words2=set(str2.split())
    overlap = Counter(words1) & Counter(words2)
    return sum(overlap.values())
with open(path_file1, 'r') as file:
    file1 = file.read()
with open(path_file2, 'r') as file:
    file2 = file.read()
print(overlapping_word_count(file1, file2))
print(overlapping_word_count_unique(file1, file2))