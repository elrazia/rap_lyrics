## Requiem for Hip Hop
##### Documenting the decline of rap music using NLP

<br/>
**Objective:** Utilize unsupervised learning and topic modeling to highlight the changes in rap music over time that are leading people to believe that [the genre is on the decline](https://www.google.com/search?q=hip+hop+dying&oq=hip+hop+dying&aqs=chrome..69i57.2351j0j1&sourceid=chrome&ie=UTF-8).
<br/>
<br/>
**Tools:** Selenium, Crawlera, Beautiful Soup, MongoDB, Amazon Web Services, Python (Pandas, Numpy, Sklearn, Matplotlib)
<br/>
<br/>
**Methodology:** Scraped lyrics of ~220,000 songs from Rap Genius. Cleaned corpus and used tf-idf to weight words. Reduced feature space using PCA. Applied K-means clustering to corpus by era. Modeled topics from each era with NMF.
<br/>
<br/>
**Conclusions:** 
<br/>

*"You got to have style, and learn to be original [...]" - KRS-One*
<br/>
The 1980s were the nascent years of hip hop music. Early rappers had distinct styles and used the genre to make bold statements. The statements varied by rap group and by neighborhood, but the messages were loud and clear. KRS-One wanted to "Stop the Violence", Run-D.M.C repudiated "Sucker MCs", and the Juice Crew let it be known that [hip hop originated in Queensbridge](https://en.wikipedia.org/wiki/The_Bridge_Wars). LL Cool J [needed love](https://en.wikipedia.org/wiki/I_Need_Love)—preferably from an [around the way girl](https://en.wikipedia.org/wiki/Around_the_Way_Girl), Public Enemy preached [black nationalism](https://en.wikipedia.org/wiki/It_Takes_a_Nation_of_Millions_to_Hold_Us_Back), and N.W.A. brought police brutality into the national spotlight. These styles and statements are evident in the way that the analysis groups the artists based on lyrics. Lyrics from individual rappers cluster together with other rappers from a particular rap group. Chuck D's lyrics and Flavor Flav's lyrics (both members of Public Enemy) end up in the same cluster. Rev Run, DMC, and Jam Master Jay (all of Run-D.M.C) end up in the same cluster. The Beastie Boys end up in the same cluster. The algorithm finds patterns in regional vernacular and to a greater extent, lyrical content, and groups similar rappers together.
<br/>
<br/>

*"MC's get a little bit of love and think they hot. Talking bout how much money they got; all y'all records sound the same [...]" - Dead Prez*
<br/>
In the 1990s and 2000s, as hip hop began to commercialize and artists discovered what consumers wanted to hear, styles and lyrical content began to coalesce. From a data standpoint, this manifests itself in the clusters becoming less distinct. Rap groups no longer cluster together, and artists appear in multiple clusters. In short, the algorithm was unable to group rappers as the decades went on due to the lyrical content becoming more similar.
<br/>
So commercialization of hip hop music led to artists in large part rapping about the same things. Can we identify what these things are? That is to say: what topics were people rapping about in the 80s, and what topics are they rapping about today? The lyrics in the dataset fell predominantly into one of four categories: Social/Political, Violence/Gangster, Partying/Drugs, Wealth/Materialism. Social and Political hip-hop was the most popular subject in 1980s rhymes. Violence and Gangster rap was the predominant topic of the 1990s. Partying, Drugs, and Materialism dominated the 2000s and 2010s.
<br/>
<br/>

*"Super Nintendo, Sega Genesis. When I was dead broke, man, I couldn't picture this. 50-inch screens, money-green leather sofa. Got two rides, a limousine with a chauffeur" - Notorious B.I.G*
<br/>
The trajectory of hip hop music gravitated away from political commentary, which only affected a portion of the population. The message of coming from a rough background and making it big was more in line with the [American Dream](https://en.wikipedia.org/wiki/American_Dream), something the majority of consumers were able to identify with.
<br/>
<br/>
The take away? There are indeed changes that have happened over hip hop's 35+ year run. It's both conceivable and understandable for people to conflate these changes with the decline of the genre. That being said, Spotify [analyzed 20 billion tracks](http://www.independent.co.uk/arts-entertainment/music/news/hip-hop-is-the-most-listened-to-genre-in-the-world-according-to-spotify-analysis-of-20-billion-10388091.html) in 2015 and found that hip hop is still the most popular genre in the world. The genre is changing, sure, but it's still as popular as it ever was.
