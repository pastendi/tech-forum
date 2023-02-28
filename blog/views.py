from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        "slug": "how-to-secure-your-wifi-network",
        "image": "scene1.jpg",
        "author": "John Doe",
        "date": "2022-03-01",
        "title": "How to Secure Your WiFi Network",
        "content": "WiFi is the backbone of our connected lives. However, many of us take it for granted and do not secure it properly. In this blog post, we will discuss some best practices to secure your WiFi network. First, change the default name and password of your WiFi network. This will make it difficult for hackers to access your network. Second, enable WPA2 encryption. This will ensure that all the data transmitted over your WiFi network is encrypted and secure. Third, disable remote management. This will prevent unauthorized access to your router's settings. Lastly, keep your router's firmware up to date. This will ensure that any security vulnerabilities are patched. By following these best practices, you can secure your WiFi network and ensure that your online activity remains private and secure."
    },
    {
        "slug": "the-rise-of-augmented-reality-in-gaming",
        "image": "scene2.jpg",
        "author": "Jane Smith",
        "date": "2022-03-05",
        "title": "The Rise of Augmented Reality in Gaming",
        "content": "Augmented reality (AR) is revolutionizing the gaming industry. AR games allow players to experience virtual worlds in a more immersive way than ever before. In this blog post, we will discuss some of the most popular AR games and how they are changing the gaming landscape. Pokemon Go is perhaps the most well-known AR game. It uses your smartphone's GPS and camera to create an immersive Pokemon-catching experience. Another popular AR game is Ingress, which encourages players to explore the real world and complete challenges. Minecraft Earth is a newer AR game that lets players build virtual structures in the real world. As AR technology continues to improve, we can expect to see even more exciting AR games in the future. AR games are not just a fun way to pass the time, they are also helping to pave the way for a more immersive and interactive future."
    },
    {
        "slug": "the-future-of-self-driving-cars",
        "image": "scene1.jpg",
        "author": "Mike Johnson",
        "date": "2022-03-10",
        "title": "The Future of Self-Driving Cars",
        "content": "Self-driving cars are no longer just a futuristic idea. They are becoming a reality, and their impact on the world could be enormous. In this blog post, we will explore some of the potential benefits and challenges of self-driving cars. One of the main benefits of self-driving cars is that they could reduce accidents caused by human error. They could also reduce traffic congestion and improve fuel efficiency. However, there are also challenges that need to be addressed, such as cybersecurity and legal issues. Self-driving cars will also require significant investment in infrastructure and technology. Despite these challenges, the potential benefits of self-driving cars are too great to ignore. In the near future, we can expect to see more and more self-driving cars on the roads, and"
    }
]


def index(request):
    return render(request, 'blog/index.html', {'posts': posts})


def all_posts(request):
    return render(request, 'blog/all-posts.html', {'posts': posts})


def single_post(request, slug):
    post = next(post for post in posts if post['slug'] == slug)
    return render(request, 'blog/single-post.html', {'post': post})
