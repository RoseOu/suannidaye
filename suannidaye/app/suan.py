#coding:utf-8

from flask import request,jsonify,render_template,Response
from app import app,db
import random,json
from .models import Suan

@app.route('/suan/',methods=["GET","POST"])
def suan():
    relation = int(request.get_json().get('relation'))
    direction = int(request.get_json().get('direction'))
    sex = int(request.get_json().get('sex'))
    suan_list = [s for s in Suan.query.filter_by(sex=sex).filter_by(direction=direction).filter_by(relation=relation).all()]
    result = ""
    me=""
    if suan_list != []:
        suan = random.choice(suan_list)
    return jsonify({
        "result":suan.result,
        "me":suan.me
        })

@app.route('/add/', methods=["GET","POST"])
def add():
    if request.method == 'POST':
        relation = request.form.get('relation')
        direction = request.form.get('direction')
        sex = request.form.get('sex')
        result = request.form.get('result')
        me = request.form.get('me')
        suan1 = Suan(relation=relation,direction=direction,sex=sex,result=result,me=me)
        db.session.add(suan1)
        db.session.commit()
    return render_template('add.html')

@app.route('/show/', methods=["GET"])
def show():
    suans=[s for s in Suan.query.all()]
    all_suan = [{
        "id":i.id,
        "direction":i.direction,
        "sex":i.sex,
        "relation":i.relation,
        "result":i.result,
        "me":i.me,
    } for i in suans]
    return jsonify({
        "all_suan":all_suan
    })

@app.route('/delete/', methods=["GET","POST"])
def delete():
    if request.method == 'POST':
        suan_id = request.form.get('id')
        suan = Suan.query.filter_by(id=suan_id).first()
        db.session.delete(suan)
        db.session.commit()
    return render_template('delete.html')

