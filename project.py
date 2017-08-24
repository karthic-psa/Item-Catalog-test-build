from flask import Flask, render_template, redirect, url_for, request, flash 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(rid=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.rid)
    return render_template('menu.html', restaurant=restaurant, items=items)
    #output = ''
    #for i in items:
        #output += i.name
        #output += '</br>'
        #output += i.price
        #output += '</br>'
        #output += i.description
        #output += '</br>'
        #output += '</br>'
    #return output

# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/',methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editMItem = session.query(MenuItem).filter_by(mid=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editMItem.name = request.form['name']
        session.add(editMItem)
        session.commit()
        flash("Item has been edited")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, MenuID=menu_id, item=editMItem)


# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete',methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    delMItem = session.query(MenuItem).filter_by(mid=menu_id).one()
    if request.method == 'POST':
        session.delete(delMItem)
        session.commit()
        flash("Item has been deleted")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

    else:
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, MenuID=menu_id, item=delMItem)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)