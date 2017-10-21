#coding:utf-8

from flask import request,jsonify,render_template,Response
from app import app,db
import random,json
from .models import Suan

@app.route('/suan/',methods=["GET","POST"])
def suan():
    relation = request.get_json().get('relation')
    list_rela = [int(l) for l in relation]
    relation = "".join([str(l) for l in list_rela])
    direction = int(request.get_json().get('direction'))
    sex = int(request.get_json().get('sex'))
    result = ""
    me=""
    status=0
    if len(list_rela)==1:
        status=4
    else:
        i=0
        while i<len(list_rela)-1:
            if (list_rela[i]==8 and list_rela[i+1]==8) or (list_rela[i]==9 and list_rela[i+1]==9):
                result=u"看你大爷"
                me=u"看你大爷"
                status=1
                break
            elif ((list_rela[i] in [0,2,4,6]) and list_rela[i+1]==8) or ((list_rela[i] in [1,3,5,7]) and list_rela[i+1]==9):
                result=u"看你大爷"
                me=u"看你大爷"
                status=3
                break
            elif len(list_rela)==2 and \
                ((list_rela[i] in [0,1,6,7] and list_rela[i+1] in [0,1,6,7]) or (list_rela[i] in [2,3,4,5] and list_rela[i+1] in [2,3,4,5])):
                status=2
                break
            i=i+1
    if status in [0,2]:
        suan_list = [s for s in Suan.query.filter_by(sex=sex).filter_by(direction=direction).filter_by(relation=relation).all()]
        if suan_list != []:
            suan = random.choice(suan_list)
            result=suan.result,
            me=suan.me
        else:
            result=u"看你大爷"
            me=u"看你大爷"
            status=4
    return jsonify({
        "result":result,
        "me":me,
        "status":status
        })

@app.route('/add/', methods=["GET","POST"])
def add():
    if request.method == 'POST':
        relation = request.form.get('relation')
#        direction = request.form.get('direction')
        sex = request.form.get('sex')
        result = request.form.get('result')
        me = request.form.get('me')
        suan1 = Suan(relation=relation,direction=0,sex=sex,result=result,me=me)
        suan2 = Suan(relation=relation,direction=1,sex=sex,result=result,me=me)
        db.session.add(suan1)
        db.session.add(suan2)
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

@app.route('/test/', methods=["POST"])
def test():
    test=request.get_json().get('test')
    return jsonify({
        'test':test
        })
