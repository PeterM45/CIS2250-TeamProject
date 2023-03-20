from flask import Flask, request

app = Flask(__name__)


def run_alberta():
    exec(open('./alberta/alberta.py').read())

def run_australia():
    exec(open('./australia/australia.py').read())

def run_britishColumbia():
    exec(open('./britishColumbia/britishColumbia.py').read())


@app.route('/')
def index():
  return '''
        <form method="post" action="/run-script">
            <button type="submit" name="script" value="alberta">Run Alberta</button>
            <button type="submit" name="script" value="australia">Run Australia</button>
            <button type="submit" name="script" value="britishColumbia">Run British Columbia</button>
        </form>
    '''


@app.route('/run-script', methods=['POST'])
def handle_form_submission():
    script = request.form['script']
    if script == 'alberta':
        run_alberta()
    elif script == 'australia':
        run_australia()
    elif script == 'britishColumbia':
        run_britishColumbia()
    # Add elif clauses for the remaining 6 scripts here...
    return '''
          <button onclick="window.location.href='/';">Back</button> 
          <h2>Script has been run!</h2>
          '''


if __name__ == '__main__':
    app.run()

