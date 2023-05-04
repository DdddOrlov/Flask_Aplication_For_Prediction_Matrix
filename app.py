import flask
from flask import render_template
import pickle
import sklearn

app = flask.Flask(__name__, template_folder='template')

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])

def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('model4.pkl', 'rb') as f:
            loaded_model = pickle.load(f)
            with open('scaler_y.pkl', 'rb') as s:
                scaler = pickle.load(s)

        button1 = float(flask.request.form['Прочность при растяжении'])
        button2 = float(flask.request.form['Плотность, кг/м3'])
        button3 = float(flask.request.form['Модуль упругости, ГПа'])
        button4 = float(flask.request.form['Количество отвердителя, м.%'])
        button5 = float(flask.request.form['Содержание эпоксидных групп,%_2'])
        button6 = float(flask.request.form['Температура вспышки, С_2'])
        button7 = float(flask.request.form['Поверхностная плотность, г/м2'])
        button8 = float(flask.request.form['Модуль упругости при растяжении, ГПа'])
        button9 = float(flask.request.form['Потребление смолы, г/м2'])
        button10 = float(flask.request.form['Угол нашивки, град'])
        button11 = float(flask.request.form['Шаг нашивки'])
        button12 = float(flask.request.form['Плотность нашивки'])

        y_pred = loaded_model.predict([[button1, button2, button3, button4, button5, button6,
                                        button7, button8, button9, button10, button11, button12]])
        pred = scaler.inverse_transform(y_pred)
        pred = pred[0,0]
        return render_template('main.html', result=pred)

if __name__ == '__main__':
    app.run()
