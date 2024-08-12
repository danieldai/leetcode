from typing import List


class Twitter:

    def __init__(self):
        self.follows = dict()
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # print('tweets', self.tweets)
        results = []

        userIds = {userId}
        if userId in self.follows:
            userIds.update(self.follows[userId])

        # print('userIds', userIds)
        for tweet in self.tweets[::-1]:
            # print('tweet[0]', tweet[0], userIds)
            if tweet[0] in userIds:
                results.append(tweet[1])
            if len(results) >= 10:
                break
        
        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)