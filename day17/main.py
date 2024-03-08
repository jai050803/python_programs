class User:
    def __init__(self,user_id,name):
        self.id = user_id
        self.username = name
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1
    def follow_back(self,user):
        self.following += 1
        user.followers += 1
    

user_1 = User("001","jai")
user_2 = User("002","jiya")
user_2.follow(user_1)
print("when jiya follow jai")
print(f"followers count of jai is {user_1.followers}")
print(f"following count of jai is {user_1.following}")
print(f"followers count of jiya is {user_2.followers}")
print(f"following count of jiya is {user_2.following}")
print("when jai follow back jiya")

user_1.follow_back(user_2)

print(f"followers count of jai is {user_1.followers}")
print(f"following count of jai is {user_1.following}")
print(f"followers count of jiya is {user_2.followers}")
print(f"following count of jiya is {user_2.following}")


