## Requiem for Hip Hop
##### Documenting the decline of rap music using NLP

<br/>
***Objective:*** Utilize K-means clustering and NMF for topic modeling to show that though rap is changing, it's not necessarily a [dying genre](https://www.google.com/search?q=hip+hop+dying&oq=hip+hop+dying&aqs=chrome..69i57.2351j0j1&sourceid=chrome&ie=UTF-8).
<br/>
<br/>
***Tools:*** Selenium, Beautiful Soup, MongoDB, Amazon Web Services, Python (Pandas, Numpy, Sklearn, Matplotlib)
<br/>
<br/>
***Methodology:*** Scraped lyrics of ~220,000 songs from Rap Genius. Cleaned corpus and used tf-idf to weight words. Reduced feature space using PCA. Applied K-means clustering to corpus by era. Modeled topics from each era with NMF.
<br/>
<br/>
***Conclusions:*** "MC's get a little bit of love and think they hot. Talking bout how much money they got; all y'all records sound the same [...]" - Dead Prez
<br/>
When hip-hop was in its nascent stages in the 80s and 90s, noone knew what it took to sell records. Everyone was trying to carve out their own niche in the genre. As a result, groups with distinct styles clustered together. Flavor Flav and Chuck D, both of Public Enemy, ended up in the same cluster. Rev Run, DMC, and Jam Master Jay, of Run DMC, ended up in the same cluster. All 9 members of the Wu Tang Clan ended up in the same cluster. As the years passed and artists began to realize what consumers liked, styles and lyrical content began to coalesce, and clusters became less distinct. Rap groups no longer clustered together, and there were artists appearing in multiple clusters.
<br/>
So the styles began to coalesce, that's nice. What about the actual content? What topics were people rapping about in the 80s, and what topics are they rapping about today? The lyrics predominantly fell into one of four categories: Social/Political, Violence/Gangster, Partying/Drugs, Wealth/Materialism. Social and Political hip-hop was big in the 80s. Violence and Gangster rap was the predominant topic of the 90s. Partying, Drugs, and Materialism dominate the 2000s and 2010s.
<br/>
The take away? It's important to not conflate the decline of creativity in hip hop with the decline of hip hop music in general. Spotify [analyzed 20 billion tracks](http://www.independent.co.uk/arts-entertainment/music/news/hip-hop-is-the-most-listened-to-genre-in-the-world-according-to-spotify-analysis-of-20-billion-10388091.html) in 2015 and found that hip hop is still the most popular genre in the world. What this means for all you aspiring rappers out there is: just because you might not be creative, doesn't mean you can't still sell records.
