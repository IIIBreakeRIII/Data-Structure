class Post:
    def __init__(self, date, content):
        self.date = date
        self.content = content

    def __str__(self):
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)
    
    
class BlogUser:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        new_post = Post(date, content)
        self.posts.append(new_post)

    def show_all_posts(self):
        for post in self.posts:
            print(post)

    def __str__(self):
        return "안녕하세요 {}입니다.\n".format(self.name)
    

blog_user_1 = BlogUser("성태호")

print(blog_user_1)

blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이었다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

blog_user_1.show_all_posts()
