from flask import Flask, request, render_template
import requests as r

app = Flask(__name__)

url = 'http://127.0.0.1:5000'

@app.route('/')
def uncss():
    if request.args.get('l') != None:
        link = request.args.get('l')
        if link.startswith('http') != True:
            link = 'https://' + link
            html = r.get(link).text.replace('<link rel="stylesheet"', '')
            fixed = html.replace('<a href=', f'<a href="{url}/?l=')
            fixed2 = fixed.replace(f'<a href="{url}/?l="', '<a href="{url}/?l=')
            print(f'Fixed HTML: {fixed2}')
            return fixed2
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run()