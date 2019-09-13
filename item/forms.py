from wtforms import StringField,TextAreaField,SubmitField
from flask_wtf import FlaskForm

class ProductForm(FlaskForm):
	name=StringField("name")
	description=TextAreaField("Description")
	submit=SubmitField("Add Item")