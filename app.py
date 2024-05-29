import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cyLhTu$Z3gg3$QVj?`IS"UrrH9;3&P_O+LSR(b.RTn9?:V4h;I'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_model(model_id):
    conn = get_db_connection()
    model = conn.execute('SELECT * FROM models WHERE id = ?',
                        (model_id,)).fetchone()
    conn.close()
    if model is None:
        abort(404)
    return model


@app.route('/')
def index():
    conn = get_db_connection()
    models = conn.execute('SELECT * FROM models').fetchall()
    conn.close()
    return render_template('index.html', models=models)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        version = request.form['version']

        if not title:
            flash('Name is required!')
        elif not content:
            flash('Description is required!')
        elif not version:
            flash('Version is required')
        else:
          conn = get_db_connection()
          conn.execute('INSERT INTO models (m_name, m_description, m_version) VALUES (?, ?, ?)',
                        (title, content, version))
          conn.commit()
          conn.close()
          return redirect(url_for('index'))

    return render_template('create.html')

# ...

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    model = get_model(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        version = request.form['version']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        elif not version:
            flash('Version is required')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE models SET m_name = ?, m_description = ?, m_version = ?'
                         ' WHERE id = ?',
                         (title, content, version, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', model=model)

# ...

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    model = get_model(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM models WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(model['m_name']))
    return redirect(url_for('index'))

if __name__ == '__main__':
  print("Before app.run(debug=True)")
  app.run(debug=True)
  print("After app.run(debug=True)")