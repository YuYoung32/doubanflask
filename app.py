import sqlite3
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from io import BytesIO
import base64
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index.html')
def home():
    return index()


@app.route('/movie.html')
def movie():
    datalist = []
    con = sqlite3.connect("outputDatabase.db")
    cur = con.cursor()
    sql = "select * from filmData"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html", movies=datalist)


@app.route('/score.html')
def score():
    scorenum = []
    scorecnt = []
    con = sqlite3.connect("outputDatabase.db")
    cur = con.cursor()
    sql = "select score, count(score) from filmData group by score"
    data = cur.execute(sql)
    for item in data:
        scorenum.append("{:.1f}".format(item[0]))
        scorecnt.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html", scorecnt=scorecnt, scorenum=scorenum)


@app.route('/word.html')
def word():
    words = ""
    con = sqlite3.connect("outputDatabase.db")
    cur = con.cursor()
    sql = "select introduction from filmData"
    data = cur.execute(sql)
    for item in data:
        words = words + item[0]
    cur.close()
    con.close()

    cut = jieba.cut(words)
    cutwords = " ".join(cut)

    img = Image.open("tree.jpg")
    img_array = np.array(img)
    wc = WordCloud(
        background_color="white",
        mask=img_array,
        font_path="simhei.ttf"
    )
    wc.generate(cutwords)

    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig("wordc.jpg", dpi=500)
    # sio = BytesIO
    # fig.savefig(sio, format='png', bbox_inches='tight', pad_inches=0.0)
    # fig.savefig()
    # data = base64.encodebytes(sio.getvalue()).decode()
    # src = 'data:image/png;base64,' + str(data)
    return render_template("word.html")


@app.route('/team.html')
def team():
    return render_template("team.html")


@app.route('/raw')
def raw():
    return render_template("mytemp.html")


if __name__ == '__main__':
    app.run()
