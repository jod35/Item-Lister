from item import app,db
from flask import redirect,request,render_template,flash
from item.forms import ProductForm
from item.models import Item

@app.route('/')
def index():
	items=Item.query.all()
	if not items:
		flash("Please add some")
	form=ProductForm()
	return render_template('index.html',
	                          form=form,
							  items=items )

@app.route('/additem',methods=['POST'])
def AddItem():
	form=ProductForm()
	name=request.form.get('name')
	description=request.form.get('description')
	new_item=Item(name=name,description=description)
	db.session.add(new_item)
	db.session.commit()
	return redirect('/')

@app.route('/delete/<int:id>')
def deleteItem(id):
	item_to_be_deleted=Item.query.get_or_404(id)
	db.session.delete(item_to_be_deleted)
	db.session.commit()
	return redirect('/')
	
      
