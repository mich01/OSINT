import matplotlib.pyplot as plt
# Plot a bar chart of social media followers
followers = [5000, 8000, 12000, 6000, 9000]
platforms = ['Twitter', 'Instagram', 'Facebook', 'LinkedIn', 'YouTube']
plt.bar(platforms, followers)
plt.xlabel('Social Media Platform')
plt.ylabel('Followers')
plt.title('Social Media Followers')
plt.show()
