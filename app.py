from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)    		# creates a unique name for each application
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

# decorator - act on the function written below 		# forward slash = home page (address)


@app.route('/')
def home():
	return render_template('home.jinja2', posts=posts)
	# return f"Hello, world! {posts}";


@app.route('/post/<int:post_id>')
def post(post_id):
	post = posts.get(post_id)
	if not post:						# post = None if not found
		return render_template('404.html', message="A post with id {} is not found.".format(post_id))
	return render_template('post.html', post = post)		# to access properties and replace content
	# return f"Post: {post['title']}, content: \n\n{post['content']}"


@app.route('/post/create/', methods=['GET', 'POST'])						#get request
def create():
	if request.method == 'POST':
		title = request.form.get('title')
		content = request.form.get('content')
		post_id = len(posts)
		posts[post_id] = { 'id': post_id, 'title': title, 'content': content}

		return redirect(url_for('post', post_id=post_id))
	return render_template('create.jinja2')


if __name__ == '__main__':
	app.run(debug=True)			# debug -> changes remotely whenever we change anything in this page
















# GET - browser sends when they access the page
# http://127.0.0.1:5000/post/form?title=Post+29&content=This+is+my+blog+post+29


# @app.route('/post/form')
# def myform():
# 	return render_template('create.jinja2')



# @app.route('/powersupply',methods=['GET'])
# def get_powersupply_status():
# 	# url= "https://10.132.117.184/api/?type=op&key=LUFRPT14MW5xOEo1R09KVlBZNnpnemh0VHRBOWl6TGM9bXcwM3JHUGVhRlNiY0dCR0srNERUQT09&cmd=/api/?type=op&cmd=<show><system><environmentals><power><slot>s0</slot></power></environmentals></system></show>"
# 	url = "https://keleshev.com/yaml-quick-introduction"
# 	response = requests.get(url, verify=False)
# 	if ( response.status_code == 200):
# 		return "Connection established"
# 	else:
# 		return "Failure in Connection"
