def display_employee(**details):
    print(type(details))
    """ for key, value in details.items():
        print(f"{key}: {value}") """


display_employee(
                name="Rahul",
                department="IT",
                experience=4,
                location="Bengaluru"
            )