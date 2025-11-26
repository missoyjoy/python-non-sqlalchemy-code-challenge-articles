#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


        # Sample authors
    ahmed = Author("Ahmed")
    zara = Author("Zara")

    # Sample magazines
    tech = Magazine("TechWorld", "Technology")
    fashion = Magazine("StyleHub", "Fashion")

    # Sample articles
    a1 = Article(ahmed, tech, "The Rise of AI")
    a2 = Article(ahmed, tech, "AI in 2025")
    a3 = Article(zara, fashion, "Fall Trends 2025")
    a4 = Article(zara, fashion, "Sustainable Style")
    a5 = Article(zara, fashion, "Fashion and Climate")


        # Test relationships
    print("Ahmed's articles:", ahmed.articles())
    print("Ahmed's magazines:", ahmed.magazines())
    print("Ahmed's topic areas:", ahmed.topic_areas())

    print("TechWorld articles:", tech.articles())
    print("TechWorld contributors:", tech.contributors())
    print("TechWorld article titles:", tech.article_titles())
    print("TechWorld contributing authors:", tech.contributing_authors())

    print("StyleHub contributors:", fashion.contributors())
    print("StyleHub contributing authors:", fashion.contributing_authors())


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
