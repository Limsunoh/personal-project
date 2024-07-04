from pprint import pprint
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display_mem(self):
        return f"회원님의 이름은 '{self.name}' 이며 아이디는 '{self.username}' 입니다."
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display_post(self):
        pprint(f"글의 제목은'{title}'이며 내용은 '{content}'입니다")


members = []
member1 = Member("Limsonoh", "sunoh", "sunoh123")
member2 = Member("Limcholrang", "cholrang", "cholrang123")
member3 = Member("honggildong", "gildong", "gildong123")
members.append(member1)
members.append(member2)
members.append(member3)

for member in members:
    print(member.name)

for member in members:
    print(member.display_mem())

post_data = [
    ("클래스", "클래스란 무엇인가", "sunoh"),
    ("메서드", "메서드는 무엇인가", "sunoh"),
    ("인스턴스", "인스턴스는 무엇일까?", "sunoh"),
    ("리스트", "리스트란 무엇인가", "cholrang"),
    ("딕셔너리", "딕셔너리란 무엇인가", "cholrang"),
    ("함수", "함수란 무엇일까?", "cholrang"),
    ("조건문", "조건문이란 무엇인가", "gildong"),
    ("변수", "변수란 무엇인가", "gildong"),
    ("맵", "맵,람다,필터식이란 무엇일까?", "gildong"),
]
posts = []
for title, content, author in post_data:
    posts.append(Post(title, content, author))

for post in posts:
    if post.author == member2.username:
        print(f"{member2.username} 님의 게시물 제목: {post.title}")

keyword = '무엇인가'
for post in posts:
    if keyword in post.content:
        print(f"- {post.title}")
