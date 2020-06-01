from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)    		
posts = {
	0: {
		'id' : 0,
		'title' : 'Post 0',
		'content' : 'This is my blog post 0!'
	},
	1: {
		'id' : 1,
		'title' : 'Post 1',
		'content' : 'This is my blog post 1!'
	},
	2: {
		'id' : 2,
		'title' : 'Post 2',
		'content' : 'This is my blog post 2!'
	}
}

@app.route('/')
def home():
	return render_template('home.jinja2', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
	post = posts.get(post_id)
	if not post:						# post = None if not found
		return render_template('404.html', message="A post with id {} is not found.".format(post_id))
	return render_template('post.html', post = post)		


@app.route('/post/create/', methods=['GET', 'POST'])						
def create():
	if request.method == 'POST':
		title = request.form.get('title')
		content = request.form.get('content')
		post_id = len(posts)
		posts[post_id] = { 'id': post_id, 'title': title, 'content': content}

		return redirect(url_for('post', post_id=post_id))
	return render_template('create.jinja2')


if __name__ == '__main__':
	app.run(debug=True)			
