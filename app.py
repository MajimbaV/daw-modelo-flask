from flask import Flask, render_template, redirect, request
from bd import *

app = Flask(__name__)


@app.route('/')
def mainTitles():
    allTitles = tblTitles.listGames()
    return render_template('maintitles.html', titles=allTitles)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        dataItem = request.form.to_dict()
        tblTitles.newGame(dataItem.get("JPtitle"), dataItem.get("WEtitle"), dataItem.get("JPyear"), dataItem.get("WEyear"), dataItem.get("Platforms"))
        return redirect('/')
    return render_template('form_maintitles.html', entry=None, title="Adcionar Entrada" )

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        dataItem = request.form.to_dict()
        tblTitles.updateGames(id, dataItem.get("JPtitle"), dataItem.get("WEtitle"), dataItem.get("JPyear"), dataItem.get("WEyear"), dataItem.get("Platforms"))
        return redirect('/')
    entry = tblTitles.searchGame(id)
    return render_template('form_maintitles.html', entry=entry, title="Editar Entrada" )

@app.route('/delete/<int:id>')
def delete(id):
    tblTitles.deleteGame(id)
    return redirect('/')


if __name__ == '__main__':
    app.run()
