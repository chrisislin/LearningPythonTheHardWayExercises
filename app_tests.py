from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
	#check 404
	resp = app.request("/")
	assert_response(resp, status = "404")

	#GET to /hello
	resp = app.request("hello")
	assert_response(resp)

	#default
	resp = app.request("/hello", method = "POST")
	assert_response(resp, contains = "Nobody")

	#test expected value
	data = {'name':'Chris', 'greet':'Game'}
	resp = app.request("/hello", method="POST", data=data)
	assert_response(resp, contains = "Chris")