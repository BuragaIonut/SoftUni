class Article:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author

    def Edit(self, new_content):
        self.content = new_content

    def ChangeAuthor(self, new_author):
        self.author = new_author
    def Rename(self, new_title):
        self.title = new_title
    def ToString(self):
        print(f'{self.title} - {self.content}:{self.author}')

article = input().split(', ')
curent_title = article[0]
curent_content = article[1]
curent_author = article[2]
curentobject = Article(curent_content, curent_content, curent_author)
n = int(input())
for i in range(n):
    line = input().split(': ')
    if line[0] == 'Edit':
        curentobject.Edit(line[1])
    elif line[0] == 'ChangeAuthor':
        curentobject.ChangeAuthor(line[1])
    elif line[0] == 'Rename':
        curentobject.Rename(line[1])
curentobject.ToString()
