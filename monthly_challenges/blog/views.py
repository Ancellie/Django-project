from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Nazarii",
        "date": date(2024, 2, 15),
        "title": "Mountain Hiking",
        "excerpt": """
        There's nothing like the views you get when hiking in the mountains!
        And i wasn't even prepared for what happened whilst I was enjoying the view!
        """,
        "content": """
            lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Officiis ...
            lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Officiis ...
            lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Officiis ...
            lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Officiis ...        
        """
    },
    {
        "slug": "visited-kfc",
        "image": "kfc.jpg",
        "author": "Nazarii",
        "date": date(2025, 2, 2),
        "title": "Visited KFC",
        "excerpt": """
        Fastfood kfc, and tea Fastfood kfc, and tea
        Fastfood kfc, and tea Fastfood kfc, and tea
        Fastfood kfc, and tea Fastfood kfc, and tea
        Fastfood kfc, and tea 
        """,
        "content": """
            lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Officiis ...
            lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Officiis ...
            lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Officiis ...
            lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Officiis ...        
        """
    }
]
# Create your views here.

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")