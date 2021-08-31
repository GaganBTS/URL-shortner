import argparse

import pywebio as pw
import bitly_api
import pywebio.output

API_KEY = 'key'
def shorten():
 pywebio.session.set_env(title='URL Shortener')

 bitly = bitly_api.Connection(access_token=API_KEY)
 url = pywebio.input.input('Enter the URL')
 try:
  response = bitly.shorten(url)
 except:
     pywebio.output.put_error('Invalid URL')
 else:
     pywebio.output.put_html(f'<div style = "text-align:center; font-size:200%"><h1>Your Shortened URL is</h1>\n<a  href={response["url"]}>{response["url"]}</a></div>')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=7700)
    args =parser.parse_args()
    pywebio.start_server(shorten,port=args.port)
