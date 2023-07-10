from flask import Flask, render_template #,send_from_directory
from flaskWT import ContactForm
from flask_bootstrap import Bootstrap
# import cv2
# import os
# from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)

Bootstrap(app)
# configuring flask app 
app.config['SECRET_KEY']="qwjcipijfpqjijmef" #csrf token generation
# app.config['UPLOADED_PHOTOS_DEST']='uploads' #flask will store uploaded files

# photos = UploadSet("photos",IMAGES)
# configure_uploads(app,photos)

# @app.route("/uploads/<filename>")
# def photo(filename):
#     image_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename)
#     image = cv2.imread(image_path)
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Grayscale', gray_image)
#     cv2.waitKey(0)  
#     cv2.destroyAllWindows()
#     return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    form = ContactForm()
    if form.validate_on_submit():
        if form.email.data=="admin@email.com" and form.password.data=="12345678":
            # filename=photos.save(form.photo.data)
            # file_url=url_for("photo",filename=filename)
            return render_template("success.html")#,file_url=file_url)
        else:
            # file_url=None
            return render_template("denied.html")
    return render_template("login.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)