from flask import Flask, render_template, redirect, url_for
from utils import gears


eanmble = Flask(__name__)


@eanmble.route("/")
def index():
    """ AS of now this only brings up the home page. A statistics filled page that only shows the days predictions
        Reminder:  do remind anyone using or viewing the site that the development process is in beta"""
    # render the index html page. maybe later we can first go through a database
    title = "Eanmble Home Page"


    csv_file_path = "Book1.csv"
    main_list = list()
    for row in gears.read_csv_file(csv_file_path):
        # append it to a 2d list and pass it into the template file
        main_list.append(row)

    return render_template('index.html', title=title, array=main_list)


@eanmble.route('/admin')
def admin_index():
    """ones a person logs in the application determines if the person is worthy of an admin
     and if found worthy he his directed to the admin.html template which contains links to such
     things such as adding_predictions"""
    return render_template('admin.html')


@eanmble.route('/fill_predictions', methods='[POST, GET]')
def fill_predictions():
    """defines the tools by whihc the administrator can edit and add new predictions """
    pass
if __name__ == "__main__":
    eanmble.run(debug=True)