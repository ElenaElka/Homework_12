import json

from flask import Flask, render_template, request

app = Flask(__name__)

users_list = []

with open('settings.json') as f:
    settings = json.load(f)
with open('candidates.json') as f:
    candidates = json.load(f)


@app.route('/')
def sample():
    return render_template('sample.html', **settings)


@app.route('/candidate/<int:id>')
def information(id):
    for candidate in candidates:
        if candidate['id'] == id:
            return render_template('candidate.html', **candidate)


@app.route('/list')
def candidate_list():
   return render_template('list.html', candidates = candidates)


@app.route('/search/')
def search_name():
    name = request.args.get('name')
    if name:
        for candidate in candidates:
            if name in str.lower(candidate['name']):
                users_list.append(candidate['name'])
    return render_template('search.html', users_list=users_list, users_count=len(users_list))


@app.route('/skill/<skill>')
def search_skill(skill):
   limit = 0
   for candidate in candidates:
      if skill in str.lower(candidate['skills']):
         users_list.append(candidate['name'])
         limit += 1
         if settings['limit'] == limit:
            return render_template('search.html', users_list=users_list, users_count=len(users_list))

app.run()
