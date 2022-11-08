from flask import Flask, render_template, request
import requests
import smtplib


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", blogs=posts)


@app.route("/about/")
def about_page():
    return render_template("about.html")


@app.route("/contact/", methods=['GET', 'POST'])
def contact_me():
    if request.method == 'GET':
        return render_template("contact.html", msg_sent=False)
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        message = f"From: \"codingpractice123321@gmail.com\" <codingpractice123321@gmail.com>\n" \
                  f"To: claudiachurch00@gmail.com\n" \
                  f"Subject: New Message\n\n" \
                  f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}".encode("utf-8")
        print(message)

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="codingpractice123321@gmail.com", password="yoqrrfieweaaovbp")
            connection.sendmail(from_addr="codingpractice123321@gmail.com",
                                to_addrs="claudiachurch00@gmail.com", msg=message)

        return render_template("contact.html", msg_sent=True)


@app.route("/post.html/<int:index>")
def blog_post(index):
    requested_post = None
    for blog in posts:
        if blog["id"] == index:
            requested_post = blog
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(port=5017, debug=True)