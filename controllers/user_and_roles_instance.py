with app.app_context():
    admin_role= roles.query.filter_by(role_name='admin').first()
    if not admin_role:
        admin_role = roles(role_name='admin')
        db.session.add(admin_role)
        db.session.commit()

    user_role = roles(role_name='user')
    db.session.add(user_role)
    db.session.commit()

    admin_user = User(username='admin',
    password='321684',
    email='sayedjohny959@gmail.com',
    role_id=1)

    db.session.add(admin_user)
    db.session.commit()

    print("Dne")

