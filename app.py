from flask import Flask,render_template,request

app1=Flask(__name__)

@app1.route('/')
def Home():
    return render_template('Home.html')


@app1.route('/number_items', methods=['POST'])

def number_items():
    global n
    form_data = dict()
    n=int(request.form['Number'])
    # return 'Hello Word'
    return render_template('items.html',n=n,form_data=form_data)

@app1.route('/calculate',methods=['POST'])
def calculate():
    total=0
    form_data=request.form.to_dict()
    for key,value in request.form.items():
        if key.startswith('item_price'):
            print(value)
            total=total+int(value)

    return render_template('items.html',n=n,total=str(total),form_data=form_data)

    # return str(total)


if __name__=="__main__":
    app1.run("0.0.0.0",port=5000)

