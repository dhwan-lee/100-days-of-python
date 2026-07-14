from flask import Flask, render_template, request
import smtplib
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = [
    {
        "id": 1,
        "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.",
        "title": "The Life of Cactus",
        "subtitle": "Who knew that cacti lived such interesting lives.",
        "image_url": "https://i1.wp.com/blog.plantdelights.com/wp-content/uploads/2015/08/Ferocactus-wislizeni-A3AZ-028-in-flower.jpg",
    },
    {
        "id": 2,
        "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.",
        "title": "Top 15 Things to do When You are Bored",
        "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
        "image_url": "https://c2.staticflickr.com/4/3026/2838434910_d770a0bb94_z.jpg?zz=1",
    },
    {
        "id": 3,
        "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.",
        "title": "Introduction to Intermittent Fasting",
        "subtitle": "Learn about the newest health craze.",
        "image_url": "https://dinnerthendessert.com/wp-content/uploads/2019/11/Fruit-Cake-Muffins-16x9.jpg",
    }
]

OWN_EMAIL = os.environ.get("OWN_EMAIL")
OWN_PASSWORD = os.environ.get("OWN_PASSWORD")

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form

        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])

        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
