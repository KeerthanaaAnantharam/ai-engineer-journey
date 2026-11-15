#validate that the domain is not on the banned list

domain ="gmail.com"
banned_domains = ["spam.com", "fake.org", "hacker.in"]
print(domain not in banned_domains) 