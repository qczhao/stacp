from flask import Flask,jsonify,abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

#@app.route('/')
@app.route('/api/v1/tasks/<int:task_id>',methods=['Get'])

#def get_tasks():
#    return jsonify({'tasks':tasks})

def get_tasks(task_id):
    ftask = filter(lambda t:t['id'] == task_id,tasks)
    aaa = list(ftask)
    if len(aaa) == 0:
        abort(403)
    #return print(list(ftask))
    return jsonify({'task' : len(list(ftask))})


def index():
    return "Hello World!"

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()