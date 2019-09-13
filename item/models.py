from item import db

class Item(db.Model):
	id=db.Column(db.Integer(),primary_key=True)
	name=db.Column(db.Text())
	description=db.Column(db.Text())


	def __repr__(self):
		return '{}'.format(self.item)