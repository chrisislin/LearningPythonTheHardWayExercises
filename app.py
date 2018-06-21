import web
urls = (
	'/hello', 'Index'
	)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def GET(self):
		render = web.template.render('templates/', base="layout")
		return render.hello_form()

	def POST(self):
		form = web.input(name = "Nobody", greet = "Hello")
		greeting = "Hello, %s, %s" %(form.greet, form.name)
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()