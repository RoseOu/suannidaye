#coding:utf-8

from flask import request,jsonify,render_template,Response
from app import app,db
import random,json
from .models import Suan

@app.route('/suan/',methods=["GET","POST"])
def suan():
    suan = int(request.get_json().get('suan'))
    direction = int(request.get_json().get('direction'))
    result_list = [s for s in Suan.query.filter_by(suan=suan).all()]
    result=""
    if result_list != []:
        result = random.choice(result_list)
    return jsonify({
        "result":result
        })

@app.route('/add/', methods=["GET","POST"])
def add():
    if request.method == 'POST':
        suan=request.form.get('suan')
        result=request.form.get('result')
        suan1=Suan(suan=suan,result=result)
        db.session.add(suan1)
        db.session.commit()
    return render_template('add.html')

@app.route('/show/', methods=["GET"])
def show():
    results=[r for r in Suan.query.all()]
    all_suan = [{
        "id":i.id,
        "suan":i.suan,
        "result":i.result
        } for i in results]
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
