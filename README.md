## Requiem for Hip Hop
##### Documenting the decline of rap music using NLP


***Objective:*** Utilize K-means clustering and NMF for topic modeling to show that though rap is changing, it's not necessarily a [dying genre](https://www.google.com/search?q=hip+hop+dying&oq=hip+hop+dying&aqs=chrome..69i57.2351j0j1&sourceid=chrome&ie=UTF-8).

***Tools:*** Selenium, Beautiful Soup, MongoDB, Amazon Web Services, Python (Pandas, Numpy, Sklearn, Matplotlib)

***Methodology:*** Scraped lyrics of ~220,000 songs from Rap Genius. Cleaned corpus and used tf-idf to weight words. Reduced feature space using PCA. Applied K-means clustering to corpus by era. Modeled topics from each era with NMF.

***Conclusions:*** "MC's get a little bit of love and think they hot. Talking bout how much money they got; all y'all records sound the same [...]" - Dead Prez
When hip-hop was in its nascent stages in the 80s and 90s, noone knew what it took to sell records. Everyone was trying to carve out their own niche in the genre. As a result, Flavor Flav and Chuck D, both of Public Enemy, ended up in the same cluster. Rev Run, DMC, and Jam Master Jay, of Run DMC, ended up in the same cluster. All 9 members of the Wu Tang Clan ended up in the same cluster. Groups with distinct styles clustered together. As the years passed and artists began to realize what consumers liked, styles and lyrical content began to coalesce, and clusters became less distinct. Social and Political hip-hop was big in the 80s (Public Enemy, KRS-One). Violence and Gangster rap was the predominant topic of the 90s (N.W.A., Mobb Deep). Partying, Drugs, and Materialism dominate the 2000s and 2010s (Gucci Mane, Rick Ross).
