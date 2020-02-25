import sys
from flask import Flask, render_template, url_for, Markup


app = Flask(__name__)

#see: https://junxiandoc.readthedocs.io/en/latest/docs/flask/flask_template.html
@app.context_processor
def utility_processor():
    def render(view,permitted_roles,linkname,request):
        if app.config.get('my_role') in permitted_roles:

            class_attribute = "class='inactive'"

            link = "<a " + class_attribute + " href='" + url_for(view) + "'>" + linkname + "</a>"
            return Markup(link)
        else:
            return "A link would appear here but it requires " + str(permitted_roles) \
                + " and the current logged in user is a " + app.config.get('my_role')
    return dict(render=render)



@app.route('/')
def home():
    # print (app.config.get('my_role'))
    return render_template('index.html')

@app.route('/course_page')
def course_page():
    return render_template('course_page.html')

@app.route('/admin_page')
def admin_page():
    return render_template('admin_page.html')

@app.route('/admin_page/create_user')
def admin_page_create_user():
    return render_template('admin_page_create_user.html')

if __name__ == '__main__':
    app.config['my_role'] = sys.argv[1]
    app.run()