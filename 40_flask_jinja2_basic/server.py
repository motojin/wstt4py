from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    p_str = "abc"
    p_lst = ["list1", "list2", "list3"]
    p_dic = {"name":"Young", "age":"23"}
    p_bln = True
    return render_template('index.html', p_str=p_str, p_lst=p_lst, p_dic=p_dic, p_bln=p_bln)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
