#leetcode link: https://leetcode.com/problems/design-twitter/description/
from collections import defaultdict
import heapq
class Twitter:
    time = 0
    def __init__(self):
        self.userFeedMap = defaultdict(set)
        self.userFollowerMap = defaultdict(set) 
        self.tweetUserMap = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        Twitter.time-=1
        self.tweetUserMap[userId].add((Twitter.time, tweetId))
        for user in self.userFollowerMap[userId]:
            self.userFeedMap[user].add((Twitter.time,tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        output=[]
        minHeapForRecentTweet = [ list(x) for x in self.tweetUserMap[userId].union(self.userFeedMap[userId])]
        heapq.heapify(minHeapForRecentTweet)
        iterator = 10
        while(iterator and minHeapForRecentTweet):
            tweetId = heapq.heappop(minHeapForRecentTweet)[1]
            output.append(tweetId)
            iterator-=1
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowerMap[followeeId].add(followerId)
        tweetsToUpdate = self.tweetUserMap[followeeId]
        for tweet in tweetsToUpdate:
            self.userFeedMap[followerId].add(tweet)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followersList = self.userFollowerMap[followeeId]
        if followerId in followersList: followersList.remove(followerId)
        tweetsToUpdate = self.tweetUserMap[followeeId]
        userFeed = self.userFeedMap[followerId]
        for tweet in tweetsToUpdate:
            if(tweet in userFeed):
                userFeed.remove(tweet)
        


# Your Twitter object will be instantiated and called as such:
userId, tweetId = 1, 5
followerId, followeeId = 2,1
obj = Twitter()
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)